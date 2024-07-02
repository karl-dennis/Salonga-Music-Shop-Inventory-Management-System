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
            """ [date, timestamp, username, employeeID, role] """

            create_table_query_user_log = '''CREATE TABLE IF NOT EXISTS user_log(
            date TEXT,
            timestamp TEXT,
            username TEXT,
            employee_id TEXT,
            role TEXT,
            FOREIGN KEY(employee_id) REFERENCES employees(employee_id)
            )'''
            self.cursor.execute(create_table_query_user_log)
        except sqlite3.Error as e:
            print('Error:', e)

    def log_event(self, username, employee_id, role):
        try:
            timestamp = datetime.now().strftime('%H:%M:%S')
            date = datetime.now().strftime('%Y-%m-%d')
            log_query = '''INSERT INTO user_log (date, timestamp, username, employee_id, role) VALUES (?, ?, ?, ?, ?)'''
            self.cursor.execute(log_query, (date, timestamp, username, employee_id, role))
            self.connectDatabase.commit()
        except sqlite3.Error as e:
            print('Error:', e)

    def fetch_event(self):
        try:
            self.cursor.execute('''SELECT * FROM user_log''')
            result = self.cursor.fetchall()
            return result
        except sqlite3.Error as e:
            print('Error', e)
            
    # def user_login(self, employee_id):
    #     self.log_event(employee_id, 'login')

    def user_logout(self, employee_id):
        self.log_event(employee_id, 'logout')