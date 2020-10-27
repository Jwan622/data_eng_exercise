from app.constants import RECORD_KEY_TO_TABLE_NAME, RECORD_KEY_TO_COLUMNS
from app.connection import connect
import psycopg2


def write(key, records):
    records_list_template = ','.join(['%s'] * len(records))
    insert_query = f"insert into {RECORD_KEY_TO_TABLE_NAME[key]} {RECORD_KEY_TO_COLUMNS[key]} values {records_list_template}"
    connection = connect()
    try:
        cursor = connection.cursor()
        print(f"Inserting records into {RECORD_KEY_TO_TABLE_NAME[key]} table")
        cursor.execute(insert_query, records)
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"there was an error: {error}")
    finally:
        if connection is not None:
            cursor.close()
            connection.commit()
            connection.close()
