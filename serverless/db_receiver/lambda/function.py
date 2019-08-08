import os
import logging
import json
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def _response_format(status_code: int = None, state: bool = None, message: str = None,
                     headers: dict = None) -> dict:
    dict_to_return = {
        "statusCode": status_code,
        "headers": headers,
    }

    if state:
        body = {
            "state": state,
            "message": message
        }
        dict_to_return.update({"body": json.dumps(body)})
    return dict_to_return


def _db_validate(db):
    return 'data' not in db or 'schema' not in db


def _send_to_sqs(event, response_headers):
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
        response_headers.update({
            "Content-Type": "application/json",
        })
        return _response_format(status_code=200, headers=response_headers, state=True, message='신청이 완료됐습니다.')
    else:
        return _response_format(status_code=500, headers=response_headers, state=False, message='오류.')


def lambda_handler(event, context):
    request_headers = event['headers']
    origin = request_headers['origin']
    response_headers = {
        "Access-Control-Allow-Origin": os.getenv('WHITE_LIST'),
    }
    if event['httpMethod'] == 'OPTIONS':
        if origin == os.getenv('WHITE_LIST'):
            response_headers.update({
                "Access-Control-Allow-Methods": "POST, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Max-Age": "86400",
                "Content-Length": "0"
            })
            return _response_format(status_code=200, headers=response_headers)
        else:
            return _response_format(status_code=403, headers=response_headers)
    elif event['httpMethod'] == 'POST':
        if origin == os.getenv('WHITE_LIST'):
            if not event['body']:
                return _response_format(status_code=500, message='빈 데이터를 보내고 있습니다.')
            return _send_to_sqs(event, response_headers)
        else:
            return _response_format(status_code=403, headers=response_headers, state=False, message='접근 제한')
