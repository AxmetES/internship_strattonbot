import sqlite3
from datetime import datetime

class DatabaseManager:
    def __init__(self, db_file='example.db'):
        self.db_file = db_file

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_file)
        return self.conn.cursor()

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.commit()
        self.conn.close()