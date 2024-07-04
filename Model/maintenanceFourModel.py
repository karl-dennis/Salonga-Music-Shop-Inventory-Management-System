import sqlite3
from tkinter import messagebox


class maintenanceFourModel:
    def __init__(self):
        self.connectDatabase = None
        self.cursor = None
        self.connect_database()
        # self.add_column()
        # self.create_transaction_table()

    def connect_database(self):
        try:
            self.connectDatabase = sqlite3.connect('salonga_music_shop.db')
            self.cursor = self.connectDatabase.cursor()
        except sqlite3.Error as e:
            print('Error:', e)

    def add_column(self):
        try:
            self.cursor.execute('''ALTER TABLE transactions ADD COLUMN status TEXT''')
        except sqlite3.Error as e:
            print('Error: ', e)

    def fetch_data(self):
        try:
            self.cursor.execute('''SELECT transaction_id, customer_name, customer_contact, revenue, date, timestamp, status FROM transactions''')
            result = self.cursor.fetchall()
            infos = [list(row) for row in result]
            return infos
        except sqlite3.Error as e:
            print('Error: ', e)

    def fetch_month_data(self):
        try:
            self.cursor.execute('''SELECT transaction_id, customer_name, customer_contact, revenue, date, timestamp, status, products_ordered FROM transactions''')
            result = self.cursor.fetchall()
            infos = [list(row) for row in result]
            return infos
        except sqlite3.Error as e:
            print('Error: ', e)

    def fetch_overall_data(self):
        try:
            self.cursor.execute('''SELECT transaction_id, customer_name, customer_contact, revenue, date, timestamp, status, products_ordered FROM transactions''')
            result = self.cursor.fetchall()
            infos = [list(row) for row in result]
            return infos
        except sqlite3.Error as e:
            print('Error: ', e)
            
    def update_transaction_status(self, selected_transaction_id, selected_value):
        self.cursor.execute('UPDATE transactions SET status = ? WHERE transaction_id = ?', (selected_value,selected_transaction_id))
        print('in database updating')
        self.connectDatabase.commit()
        messagebox.showinfo('Success', 'Status Updated')