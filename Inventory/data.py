import sqlite3

in_val = []
in_cat = []
in_Num = []
in_Name = []
Situation = []
Up_Situation = []
input_id = []

db = sqlite3.connect("data.db")
cursor = db.cursor()

cursor.execute(
    """CREATE TABLE IF NOT EXISTS data_table(
        Value TEXT,
        Category TEXT,
        Number INTEGER,
        Name TEXT,
        Situation TEXT
    )"""
)


def data_saving():
    """insert query"""
    cursor.execute(
        """INSERT INTO data_table(Value, Category, Number, Name, Situation) VALUES(?, ?, ?, ?, ?)""", (str(in_val), str(in_cat), str(in_Num), str(in_Name), str(Situation))
    )
    db.commit()


def update_data():
    """update query"""
    cursor.execute(
        db.execSQL("UPDATE DB_TABLE SET YOUR_COLUMN='newValue' WHERE id=6 ")
    )
    db.commit()
    db.close()


data_saving()
