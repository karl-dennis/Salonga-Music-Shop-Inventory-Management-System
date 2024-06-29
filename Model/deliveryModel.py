import sqlite3
import random
import string
from tkinter import messagebox
class deliveryModel:
    def __init__(self):
        self.connectDatabase = None
        self.cursor = None
        self.connect_database()
        self.create_delivery_table()
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

    def create_delivery_table(self):
        try:
            create_table_query_delivery = '''CREATE TABLE IF NOT EXISTS delivery(
                delivery_id TEXT PRIMARY KEY,
                products_ordered TEXT NOT NULL,
                sub_total REAL NOT NULL,
                date TEXT NOT NULL,
                status TEXT NOT NULL
            )'''
            self.cursor.execute(create_table_query_delivery)
        except sqlite3.Error as e:
            print('Error:', e)

    def save_delivery(self, totalPrice, products_ordered, date, status):

        try:
            # print(f"In model\nName: {name}, Contact: {contact}, Total Price: {totalPrice}, Date: {date}, Time: {status}")
            # for row in products_ordered:
            # print(f"Product: {row['name']}, Brand: {row['brand']}, Quantity: {row['quantity']}, Price: {row['price']}")
            print("Adding Delivery")
            delivery_id = self.generate_unique_id()
            self.cursor.execute('''INSERT INTO delivery (delivery_id, products_ordered, sub_total, date, status)
                                VALUES (?, ?, ?, ?, ?)''', (delivery_id, products_ordered, totalPrice, date, status))
            self.connectDatabase.commit()
            messagebox.showinfo('Success', 'Delivery Saved')
        except sqlite3.Error as e:
            print('Error:', e)

    def generate_unique_id(self):
        while True:
            letters = ''.join(random.choices(string.ascii_uppercase, k=3))
            digits = ''.join(random.choices(string.digits, k=4))
            unique_id = letters + digits

            self.cursor.execute('''SELECT delivery_id FROM delivery WHERE delivery_id = ?''', (unique_id,))
            if not self.cursor.fetchone():
                return unique_id