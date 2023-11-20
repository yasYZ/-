import psycopg2
import datetime

in_val = []
in_sender = []
in_cat = []
in_Num = []
in_Name = []
in_Situation = ['در انبار']
Up_Situation = []
input_id = []
user_id = []
out_number = []
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
    created_at TEXT NOT NULL,
    sender TEXT NOT NULL 
);
"""
cursor.execute(create_post_table_postgres)

date = datetime.datetime.today()

try:
    def data_saving():
        write_query = f""" INSERT INTO data(name, category, value, number, situation, created_at, sender)
         VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        values = (in_Name[0], in_cat[0], in_val[0], in_Num[0], in_Situation[0], date, in_sender[0])
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
        for item in in_sender:
            in_sender.remove(item)
except Exception as ex:
    file = open('log/db_log.txt', 'a')
    file.write(f'**data dose"nt save because {ex} in {datetime.datetime.today()}!\n')
    file.close()

data_show_var = []
show_data = []


def data_show():
    query = "SELECT * FROM data WHERE name ILIKE '%{}%'".format(show_data[0])
    cursor.execute(query)
    records = cursor.fetchall()
    for record in records:
        data_show_var.append(record)
        print(record)
    for item in show_data:
        show_data.remove(item)


show_all_val = []


# def show_all_values():
#     try:
#         cursor.execute(f"SELECT name FROM data")
#         records = cursor.fetchall()
#         for item in records:
#             show_all_val.append(item)
#     except Exception as ex:
#         file0 = open('log/db_log.txt', 'a')
#         file0.write(f'**data dos"nt exist. error {ex} in {datetime.datetime.today()}!\n')
#         file0.close()


row_data = []


def select_row():
    try:
        cursor.execute(f"SELECT * FROM data")
        records = cursor.fetchall()
        for item in records:
            row_data.append(item)
    except Exception as ex:
        file0 = open('log/db_log.txt', 'a')
        file0.write(f'**data dos"nt exist. error {ex} in {datetime.datetime.today()}!\n')
        file0.close()


def del_all_showed_data():
    for item in row_data:
        row_data.remove(item)
    for item in show_all_val:
        show_all_val.remove(item)


def update_query(row_index):
    update_query_postreSQL = f"""
    UPDATE 
        data 
    SET 
        number = '{out_number[0]}' 
    WHERE id = %s;"""
    number = str(row_index + 1)
    cursor.execute(update_query_postreSQL, number)
    conn.commit()
    for item in out_number:
        out_number.remove(item)


def change_situation(row_index):
    update_situation = f"""
    UPDATE
        data
    SET 
        situation = 'اتمام موجودی'
    WHERE id = %s;
    """
    number = str(row_index + 1)
    cursor.execute(update_situation, number)
    conn.commit()


selected_number = []


def select_exporter():
    try:
        cursor.execute(f"SELECT number FROM data")
        records = cursor.fetchall()
        for item in records:
            selected_number.append(item[0])
    except Exception as ex:
        file0 = open('log/db_log.txt', 'a')
        file0.write(f'**data dos"nt exist. error {ex} in {datetime.datetime.today()}!\n')
        file0.close()


zero_number = []


def find_number_val():
    try:
        cursor.execute(f"SELECT number FROM data WHERE number LIKE '{0}'")
        records = cursor.fetchall()
        for item in records:
            zero_number.append(item[0])
    except Exception as ex:
        file0 = open('log/db_log.txt', 'a')
        file0.write(f'**data dos"nt exist. error {ex} in {datetime.datetime.today()}!\n')
        file0.close()


# __situation__ = []
# def find_situation_val():
#     try:
#         cursor.execute(f"SELECT * FROM data WHERE number LIKE '{'اتمام موجودی'}'")
#         records = cursor.fetchall()
#         for item in records:
#             __situation__.append(item[0])
#     except Exception as ex:
#         file0 = open('log/db_log.txt', 'a')
#         file0.write(f'**data dos"nt exist. error {ex} in {datetime.datetime.today()}!\n')
#         file0.close()

# change for updated versions....
# conn.commit()


# coming soon 2.0 version
