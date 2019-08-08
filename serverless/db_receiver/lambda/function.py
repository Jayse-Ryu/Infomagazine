import os
import logging
import json
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def _response_format(status_code: int = None, state: bool = True, message: str = None,
                     custom_headers: dict = None) -> dict:
    headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": os.getenv('WHITE_LIST'),
        "Access-Control-Allow-Headers": "Content-Type"
    }
    if custom_headers is not None:
        headers.update(custom_headers)
    body = {
        "state": state,
        "message": message
    }
    return {
        "statusCode": status_code,
        "headers": headers,
        "body": json.dumps(body)
    }


def _db_validate(db):
    return 'data' not in db or 'schema' not in db


def _send_to_sqs(event):
    headers = event['headers']
    user_agent = headers['user-agent']
    ip_v4_address = headers['x-forwarded-for'].split(",")[0]
    event_body = event['body']
    body = json.loads(event_body)

    if _db_validate(body.keys()):
        return _response_format(status_code=500, message='유효한 db가 아닙니다.')

    body_to_send = {
        "landing_id": body['landing_id'],
        "registered_date": body['registered_date'],
        "data": body['data'],
        "schema": body['schema'],
        "user_agent": user_agent,
        "ip_v4_address": ip_v4_address
    }

    session = boto3.session.Session(aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                                    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                                    aws_session_token=os.getenv('AWS_SESSION_TOKEN'),
                                    region_name='ap-northeast-2')
    sqs_client = session.client('sqs')
    response = sqs_client.send_message(
        QueueUrl='https://sqs.ap-northeast-2.amazonaws.com/590908818913/test-sqs',
        DelaySeconds=0,
        MessageBody=json.dumps(body_to_send)
    )
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        return _response_format(status_code=200, message='신청이 완료됐습니다.')
    else:
        return _response_format(status_code=500, state=False, message='오류.')


def lambda_handler(event, context):
    if event['httpMethod'] == 'OPTIONS':
        return _response_format(status_code=200, custom_headers={"Cache-Control": "max-age=31536000"})
    if not event['body']:
        return _response_format(status_code=500, message='입력할 db가 없습니다.')

    return _send_to_sqs(event)
