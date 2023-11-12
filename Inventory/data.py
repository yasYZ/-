import psycopg2
import datetime

in_val = []
in_cat = []
in_Num = []
in_Name = []
Situation = []
Up_Situation = []
input_id = []
user_id = []

create_post_table_postgres = """
CREATE TABLE IF NOT EXISTS data (
    id  SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT NOT NULL ,
    value TEXT NOT NULL,
    number INTEGER NOT NULL,
    situation TEXT NOT NULL,
    created_at DATE NOT NULL
);
"""


def create_db_connection(database, user, host, port, password):
    connection = None
    try:
        connection = psycopg2.connect(
            database=database, user=user, host=host,
            port=port, password=password
        )
        file_obj = open("log/log.txt", "w")
        file_obj.write(f"""connect to post data base is successfully error[0] by {user_id} user, in {datetime.datetime.today()}""")
        file_obj.close()
    except Exception as ex:
        print(ex)
        return connection


cursor = psycopg2.cursor()


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print('query ok')
    except Exception as ex:
        print(ex)


post_connection = create_db_connection(
    database='postgres', user='postgres', password='1234qwer',
    host='localhost', port=5432)


execute_query(post_connection, create_post_table_postgres)
