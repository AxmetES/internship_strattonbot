from datetime import datetime

from db import DatabaseManager

def create_table():
    with DatabaseManager() as cursor:
        try:
            cursor.execute('''CREATE TABLE IF NOT EXISTS message (id INTEGER PRIMARY KEY, message TEXT, time DATETIME)''')
        except Exception as e:
            print(f"Error creating table: {e}")

def insert_message(message, timestamp):
    message_date = datetime.utcfromtimestamp(timestamp)
    with DatabaseManager() as cursor:
        cursor.execute("INSERT INTO message (message, time) VALUES (?, ?)", (message, message_date))

def get_messages():
    with DatabaseManager() as cursor:
        cursor.execute("SELECT * FROM message")
        return cursor.fetchall()