import sqlite3
import datetime
import uuid
import random
import string
from tkinter import messagebox
class salesModel:
    def __init__(self):
        self.connectDatabase = None
        self.cursor = None
        self.connect_database()
        self.create_transaction_table()
    def connect_database(self):
        try:
            self.connectDatabase = sqlite3.connect('salonga_music_shop.db')
            self.cursor = self.connectDatabase.cursor()
        except sqlite3.Error as e:
            print('Error:', e)

    def fetch_products(self):
        try:
            self.cursor.execute('''SELECT product_image, product_name, product_brand, product_type, product_quantity, product_price
            FROM products''')

            data = self.cursor.fetchall()
            infos = [list(row) for row in data]
            return infos
        except sqlite3.Error as e:
            print('Error: ', e)

    def create_transaction_table(self):
        try:
            create_table_query_transactions = '''CREATE TABLE IF NOT EXISTS transactions(
                transaction_id TEXT PRIMARY KEY,
                customer_name TEXT NOT NULL,
                customer_contact INTEGER NOT NULL,
                products_ordered TEXT NOT NULL,
                revenue REAL NOT NULL,
                date TEXT NOT NULL,
                timestamp TEXT NOT NULL
            )'''
            self.cursor.execute(create_table_query_transactions)
        except sqlite3.Error as e:
            print('Error:', e)

    def save_transaction(self, name, contact, totalPrice, products_ordered, date, timestamp):
        # print(f"In model\nName: {name}, Contact: {contact}, Total Price: {totalPrice}, Date: {date}, Time: {timestamp}")
        # for row in products_ordered:
        #     print(f"Product: {row['name']}, Brand: {row['brand']}, Quantity: {row['quantity']}, Price: {row['price']}")
        try:
            print("adding transaction")
            transaction_id = self.generate_unique_id()
            self.cursor.execute('''INSERT INTO transactions (transaction_id, customer_name, customer_contact, products_ordered, revenue, date, timestamp)
                                VALUES (?, ?, ?, ?, ?, ?, ?)''', (transaction_id, name, contact, products_ordered, totalPrice, date, timestamp))

            self.connectDatabase.commit()
            messagebox.showinfo('Success', 'Transaction Successful')
        except sqlite3.Error as e:
            print('Error:', e)

    def generate_unique_id(self):
        while True:
            letters = ''.join(random.choices(string.ascii_uppercase, k=3))
            digits = ''.join(random.choices(string.digits, k=4))
            unique_id = letters + digits

            self.cursor.execute('''SELECT transaction_id FROM transactions WHERE transaction_id = ?''', (unique_id,))
            if not self.cursor.fetchone():
                return unique_id
