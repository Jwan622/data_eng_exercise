import psycopg2
import app.constants

def connection():
    print("connecting to database...")
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        host="localhost",
        port="8000",
        password="password"
    )
    try:
        cursor = conn.cursor()
        print("Connected!\n")
        cursor.execute("SELECT * FROM {table_name}")
        # retrieve the records from the database
        records = cursor.fetchall()
        for i, record in records:
            print("\n", type(record))
            print(record)

    except (Exception, psycopg2.DatabaseError) as error:
        print("there was an error")
        print(error)
    finally:
        if conn is not None:
            cursor.execute(
                "SELECT table_schema,table_name FROM information_schema.tables WHERE table_schema = 'public' ORDER BY table_schema,table_name")
            rows = cursor.fetchall()
            for row in rows:
                print("dropping table: ", row[1])
                cursor.execute("drop table " + row[1] + " cascade")
            cursor.close()
            conn.commit()
            conn.close()
