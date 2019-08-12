import os
import logging
import json
import boto3
import pymysql

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def _response_format(status_code: int = None, state: bool = None, message: str = None,
                     headers: dict = None) -> dict:
    dict_to_return = {
        "statusCode": status_code
    }

    if headers:
        dict_to_return.update({"headers": headers})

    if message:
        body = {
            "state": state,
            "message": message
        }
        dict_to_return.update({"body": json.dumps(body)})
    return dict_to_return


def _send_to_sqs(event, response_headers):
    headers = event['headers']
    user_agent = headers['user-agent']
    ip_v4_address = headers['x-forwarded-for'].split(",")[0]
    event_body = event['body']
    body = json.loads(event_body)

    db_key_list = body.keys()
    if 'data' not in db_key_list or 'schema' not in db_key_list:
        return _response_format(status_code=500, headers=response_headers, state=False, message='유효한 db가 아닙니다')

    rds_connection = pymysql.connect(os.getenv('DB_HOST'), user=os.getenv('DB_USER'),
                                     password=os.getenv('DB_PASSWD'), database=os.getenv('DB_DATABASE'),
                                     connect_timeout=5,
                                     charset='utf8mb4')

    exist_check = False
    with rds_connection.cursor(pymysql.cursors.DictCursor) as cursor:
        for key, item in body['schema'].items():
            if item in ['전화번호', '핸드폰번호']:
                key_to_search = key
                value_to_search = body['data'][key_to_search]
                json_exist_sql_command = f"""
                                SELECT COUNT(*) AS '__count'
                                FROM `landing_page_db` db
                                WHERE landing_id = '{body['landing_id']}' 
                                AND JSON_EXTRACT(db.data, "$.{key_to_search}") = '{value_to_search}'
                            """
                cursor.execute(json_exist_sql_command)
                get_count = cursor.fetchone()
                if get_count['__count'] > 0:
                    exist_check = True
                break

    if exist_check:
        return _response_format(status_code=200, headers=response_headers, state=False, message='이미 등록됐습니다')

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
        return _response_format(status_code=200, headers=response_headers, state=True, message='신청이 완료됐습니다')
    else:
        return _response_format(status_code=500, headers=response_headers, message='신청 실패')


def lambda_handler(event, context):
    response_headers = {
        "Access-Control-Allow-Origin": os.getenv('WHITE_LIST'),
        "Content-Type": "application/json"
    }
    try:
        if event['httpMethod'] == 'OPTIONS':
            del response_headers['Content-Type']
            response_headers.update({
                "Access-Control-Allow-Methods": "POST, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Max-Age": "86400",
                "Content-Length": "0"
            })
            return _response_format(status_code=200, headers=response_headers)
        elif event['httpMethod'] == 'POST':
            if not event['body']:
                return _response_format(status_code=500, headers=response_headers, message='빈 데이터')
            return _send_to_sqs(event, response_headers)
    except Exception as e:
        logger.warning(str(e))
        return _response_format(status_code=500, headers=response_headers, message='서버 오류')
