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
    if len(show_data) == 0:
        file = open('log/db_log.txt', 'a')
        file.write(f'**show_data is empty, in {datetime.datetime.today()}!\n')
        file.close()
        return

    query = "SELECT * FROM data WHERE name ILIKE %s"
    cursor.execute(query, ('%' + show_data[0] + '%',))
    records = cursor.fetchall()
    for record in records:
        data_show_var.append(record)



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


out_number = []


def update_query(row_index):
    update_query_postreSQL = """
    UPDATE 
        data 
    SET 
        number = %s 
    WHERE 
        id = %s;"""
    number = str(out_number[0])
    print(number)
    cursor.execute(update_query_postreSQL, (number, row_index+1))
    conn.commit()

    out_number.clear()


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
insert_number = []


def select_exporter():
    try:
        query = f"SELECT number FROM data WHERE id = %s"
        cursor.execute(query, insert_number[0])
        records = cursor.fetchall()
        for item in records:
            selected_number.append(item)
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
            zero_number.append(item)
    except Exception as ex:
        file0 = open('log/db_log.txt', 'a')
        file0.write(f'**data dos"nt exist. error {ex} in {datetime.datetime.today()}!\n')
        file0.close()


def __search_del__():
    for item in show_data:
        show_data.remove(item)
    for item in data_show_var:
        data_show_var.remove(item)


def organization():
    query = """
        SELECT *
        FROM data  
        ORDER BY CAST(id AS INTEGER);
    """

    cursor.execute(query)
    rows = cursor.fetchall()

    for i, row in enumerate(rows, start=1):
        update_query = """
            UPDATE data
            SET id = %s
            WHERE id = %s;
        """
        cursor.execute(update_query, (i, row[0]))

    conn.commit()


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
