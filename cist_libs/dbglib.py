import sqlite3
from unittest import result

def find_group_id(group_name: str, grade_t: str, cursor):
    result = cursor.execute(f"SELECT id FROM {grade_t} WHERE name='{group_name}'")
    records = result.fetchone()

    if records:
        return records[0]
    else:
        print("Group not found!")
        return 00000;

def connect_db(db_name):
    try:
        conn = sqlite3.connect(db_name)
        print("Successfully connected to DB!")
        cursor = conn.cursor()
    except sqlite3.Error as e:
        print(f"Error occured while connecting to db: {e}")

    return conn, cursor
