import sqlite3
from datetime import datetime


class maintenanceTwoModel:
    def __init__(self):
        self.connectDatabase = None
        self.cursor = None
        self.create_database()
        self.create_table_user_log()

    def create_database(self):
        try:
            self.connectDatabase = sqlite3.connect('salonga_music_shop.db')
            self.cursor = self.connectDatabase.cursor()
        except sqlite3.Error as e:
            print('Error:', e)
    def create_table_user_log(self):
        try:
            create_table_query_user_log = '''CREATE TABLE IF NOT EXISTS user_log(
            employee_id TEXT,
            event TEXT,
            timestamp TEXT,
            FOREIGN KEY(employee_id) REFERENCES employees(employee_id)
            )'''
            self.cursor.execute(create_table_query_user_log)
        except sqlite3.Error as e:
            print('Error:', e)

    def log_event(self, employee_id, event):
        try:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log_query = '''INSERT INTO user_log (employee_id, event, timestamp) VALUES (?, ?, ?)'''
            self.cursor.execute(log_query, (employee_id, event, timestamp))
            self.connectDatabase.commit()
        except sqlite3.Error as e:
            print('Error:', e)

    def user_login(self, employee_id):
        self.log_event(employee_id, 'login')

    def user_logout(self, employee_id):
        self.log_event(employee_id, 'logout')