import psycopg2
import datetime

in_val = []
in_cat = []
in_Num = []
in_Name = []
in_Situation = ['در انبار']
Up_Situation = []
input_id = []
user_id = []
try:
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="1234qwer",
        port=5432
    )
    file = open('log/db_log.txt', 'a')
    file.write(f'user successfully connect to database {datetime.datetime.today()}\n')
    file.close()
except Exception as ex:
    file = open('log/db_log.txt', 'a')
    file.write(f'**user unsuccessfully connect to database error {ex} in {datetime.datetime.today()}!\n')
    file.close()
    print(ex)

cursor = conn.cursor()


create_post_table_postgres = """
CREATE TABLE IF NOT EXISTS data (
    id  SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT NOT NULL ,
    value TEXT NOT NULL,
    number TEXT NOT NULL,
    situation TEXT NOT NULL,
    created_at TEXT NOT NULL
);
"""
cursor.execute(create_post_table_postgres)

date = datetime.datetime.today()

try:
    def data_saving():
        write_query = f""" INSERT INTO data(name, category, value, number, situation, created_at)
         VALUES (%s, %s, %s, %s, %s, %s)"""
        values = (in_Name, in_cat, in_val, in_Num, in_Situation, date)
        cursor.execute(write_query, values)
        conn.commit()
        file = open('log/db_log.txt', 'a')
        file.write(f'data saved {datetime.datetime.today()}\n')
        file.close()
        for item in in_val:
            in_val.remove(item)
        for item in in_Num:
            in_Num.remove(item)
        for item in in_cat:
            in_cat.remove(item)
        for item in in_Name:
            in_Name.remove(item)
except Exception as ex:
    file = open('log/db_log.txt', 'a')
    file.write(f'**data dose"nt save because {ex} in {datetime.datetime.today()}!\n')
    file.close()


conn.commit()

