import sqlite3

in_val = []
in_cat = []
in_Num = []
in_Name = []


def data_saving():

    db = sqlite3.connect("data.db")
    cursor = db.cursor()

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS data_table(
            Value TEXT,
            Category TEXT,
            Number INTEGER,
            Name TEXT
        )"""
    )

    # insert query
    cursor.execute(
        """INSERT INTO data_table(Value, Category, Number, Name) VALUES(?, ?, ?, ?)""", (str(in_val), str(in_cat), str(in_Num), str(in_Name))
    )
    db.commit()

    db.close()
