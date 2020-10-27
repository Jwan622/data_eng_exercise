import psycopg2


def connection():
    print("connecting to database...")
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        host="localhost",
        port="8000",
        password="password"
    )
    return conn
