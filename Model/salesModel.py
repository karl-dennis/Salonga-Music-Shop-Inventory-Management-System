import sqlite3
import random
import string
from tkinter import messagebox
import json
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
            availability = 'For Sale'
            self.cursor.execute('''SELECT product_image, product_name, product_brand, product_type, product_quantity, product_price
            FROM products WHERE availability = ?''', (availability,))

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

    # def save_transaction(self, name, contact, totalPrice, products_ordered, date, timestamp):
    #     # print(f"In model\nName: {name}, Contact: {contact}, Total Price: {totalPrice}, Date: {date}, Time: {timestamp}")
    #     # for row in products_ordered:
    #     #     print(f"Product: {row['name']}, Brand: {row['brand']}, Quantity: {row['quantity']}, Price: {row['price']}")
    #     try:
    #         # print("adding transaction")
    #         transaction_id = self.generate_unique_id()
    #         status = 'Active'
    #         self.cursor.execute('''INSERT INTO transactions (transaction_id, customer_name, customer_contact, products_ordered, revenue, date, timestamp, status)
    #                             VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', (transaction_id, name, contact, products_ordered, totalPrice, date, timestamp, status))
    #
    #         self.connectDatabase.commit()
    #         messagebox.showinfo('Success', 'Transaction Successful')
    #     except sqlite3.Error as e:
    #         print('Error:', e)

    def save_transaction(self, name, contact, totalPrice, products_ordered, date, timestamp):
        try:

            transaction_id = self.generate_unique_id()

            # Begin transaction
            self.cursor.execute("BEGIN TRANSACTION")

            status = 'Active'
            # Insert transaction details into transactions table
            self.cursor.execute('''INSERT INTO transactions (transaction_id, customer_name, customer_contact, products_ordered, revenue, date, timestamp,status)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                                (transaction_id, name, contact, products_ordered, totalPrice, date, timestamp, status))


            convert_json = json.loads(products_ordered)
            # Update product quantities in products table
            # print(products_ordered)
            for product in convert_json:
                product_name = product['name']
                quantity_sold = product['quantity']

                # Retrieve current quantity from products table
                self.cursor.execute('''SELECT product_quantity FROM products WHERE product_name = ?''', (product_name,))
                current_quantity = self.cursor.fetchone()[0]

                # Calculate new quantity after sale
                new_quantity = current_quantity - quantity_sold

                # Update quantity in products table
                self.cursor.execute('''UPDATE products SET product_quantity = ? WHERE product_name = ?''',
                                    (new_quantity, product_name))

            # Commit the transaction
            self.connectDatabase.commit()

            # Display success message
            messagebox.showinfo('Success', 'Transaction Successful')

        except sqlite3.Error as e:
            # Rollback transaction if there's an error
            self.connectDatabase.rollback()
            print('Error:', e)
    def generate_unique_id(self):
        while True:
            letters = ''.join(random.choices(string.ascii_uppercase, k=3))
            digits = ''.join(random.choices(string.digits, k=4))
            unique_id = letters + digits

            self.cursor.execute('''SELECT transaction_id FROM transactions WHERE transaction_id = ?''', (unique_id,))
            if not self.cursor.fetchone():
                return unique_id