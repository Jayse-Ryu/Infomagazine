import json
import os
import logging
import pymysql

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def _insert_db_to_rds(event):
    body = json.loads(event['Records'][0]['body'])
    landing_id = body['landing_id']
    data = json.dumps(body['data'])
    schema = json.dumps(body['schema'])
    user_agent = body['user_agent']
    ip_v4_address = body['ip_v4_address']
    registered_date = body['registered_date']

    rds_connection = pymysql.connect(os.getenv('DB_HOST'), user=os.getenv('DB_USER'),
                                     password=os.getenv('DB_PASSWD'), database=os.getenv('DB_DATABASE'),
                                     connect_timeout=5,
                                     charset='utf8mb4')

    try:
        with rds_connection.cursor(pymysql.cursors.DictCursor) as cursor:

            insert_sql_command = "INSERT INTO `landing_page_db` (`landing_id`, `data`, `schema`, `user_agent`, `ip_v4_address`, `registered_date`) " \
                                 "VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(insert_sql_command, (landing_id, data, schema, user_agent, ip_v4_address, registered_date))
            rds_connection.commit()
    except Exception as e:
        logger.warning(str(e))
        logger.warning("Fail.")
    else:
        logger.info("Succeed.")
    finally:
        rds_connection.close()


def lambda_handler(event, context):
    _insert_db_to_rds(event)
