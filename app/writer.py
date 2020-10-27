from app.constants import RECORD_KEY_TO_TABLE_NAME, RECORD_KEY_TO_COLUMNS
from app.connection import connect
import psycopg2


def write(key, records):
    records_list_template = ','.join(['%s'] * len(records))
    insert_query = f"insert into {RECORD_KEY_TO_TABLE_NAME[key]} {RECORD_KEY_TO_COLUMNS[key]} values {records_list_template}"
    connection = connect()
    try:
        cursor = connection.cursor()
        print(f"INSERTING RECORDS INTO {RECORD_KEY_TO_TABLE_NAME[key]} TABLE")
        cursor.execute(insert_query, records)
        # retrieve the records from the database
        records = cursor.fetchall()
        for i, record in records:
            print(f"LOADED RECORD: {record}")

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"there was an error: {error}")
    finally:
        if connection is not None:
            cursor.execute(
                "SELECT table_schema,table_name FROM information_schema.tables WHERE table_schema = 'public' ORDER BY table_schema,table_name")
            rows = cursor.fetchall()
            for row in rows:
                print("dropping table: ", row[1])
                cursor.execute("drop table " + row[1] + " cascade")
            cursor.close()
            connection.commit()
            connection.close()
