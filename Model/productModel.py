import sqlite3
import random
import string
import io
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt


class productModel:
    def __init__(self):
        self.connectDatabase = None
        self.cursor = None
        self.connect_database()
        self.create_table_products()

        self.create_brand_table()
        self.create_table_stock()

        self.create_product_type_table()

    def connect_database(self):
        try:
            self.connectDatabase = sqlite3.connect('salonga_music_shop.db')
            self.cursor = self.connectDatabase.cursor()
        except sqlite3.Error as e:
            print('Error:', e)

    def create_table_products(self):
        try:
            create_table_query_products = '''CREATE TABLE IF NOT EXISTS products(
                product_id TEXT PRIMARY KEY,
                product_name TEXT,
                product_brand TEXT,
                product_type TEXT,
                product_quantity INTEGER,
                product_price REAL NOT NULL,
                status TEXT NOT NULL,
                product_image BLOB,
                capital_price REAL NOT NULL
            )'''
            self.cursor.execute(create_table_query_products)
        except sqlite3.Error as e:
            print('Error:', e)

    def create_table_stock(self):
        try:
            create_table_query_stocks = '''CREATE TABLE IF NOT EXISTS stock_items(
                stock_id TEXT PRIMARY KEY,
                product_id TEXT,
                FOREIGN KEY (product_id) REFERENCES products (product_id)
            )'''
            self.cursor.execute(create_table_query_stocks)
        except sqlite3.Error as e:
            print('Error:', e)
    
    def create_brand_table(self):
        try:
            create_table_query_stocks = '''CREATE TABLE IF NOT EXISTS brands(
                brand TEXT NOT NULL)'''
            self.cursor.execute(create_table_query_stocks)
        except sqlite3.Error as e:
            print('Error:', e)

    def create_product_type_table(self):
        try:
            create_table_query_type = '''CREATE TABLE IF NOT EXISTS product_type(
                product_type TEXT NOT NULL)'''
            self.cursor.execute(create_table_query_type)
        except sqlite3.Error as e:
            print('Error:', e)

    def add_products(self, name, product_type, brand, quantity, price, image):
        quantity = int(quantity)
        price = float(price)

        # Determine status based on quantity
        status = 'Available' if quantity > 5 else 'Low Stock' if quantity > 0 else 'No Stock'

        product_id = self.generate_unique_id()
        stock_ids = [self.generate_unique_id() for _ in range(quantity)]

        # Convert image data to bytes if needed
        if isinstance(image, Image.Image):
            with io.BytesIO() as output:
                image.save(output, format='PNG')
                image_data = output.getvalue()
        else:
            image_data = image

        product_data = [product_id, name, brand, product_type, quantity, price, status, image_data]

        try:
            # Insert the new product into the products table
            self.cursor.execute('''INSERT INTO products (product_id, product_name, product_brand, product_type, product_quantity, product_price, status, product_image)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', product_data)
            self.connectDatabase.commit()

            # Insert the initial stock entries into the stock_items table
            stock_data = [(stock_id, product_id) for stock_id in stock_ids]
            self.cursor.executemany('''INSERT INTO stock_items (stock_id, product_id)
                        VALUES (?, ?)''', stock_data)
            self.connectDatabase.commit()

            print(f"Product added with ID: {product_id}")
            print(f"{quantity} stock items added for product ID: {product_id}")

        except sqlite3.Error as e:
            print('Error:', e)

    def fetch_data(self):
        self.cursor.execute('''SELECT product_id, product_name, product_brand, product_type, 
                                              product_quantity, product_price, status 
                                       FROM products''')
        data = self.cursor.fetchall()
        converted_data = [list(row) for row in data]
        return converted_data

    def generate_unique_id(self):
        while True:
            letters = ''.join(random.choices(string.ascii_uppercase, k=3))
            digits = ''.join(random.choices(string.digits, k=4))
            unique_id = letters + digits

            self.cursor.execute('''SELECT product_id FROM products WHERE product_id = ?''', (unique_id,))
            if not self.cursor.fetchone():
                return unique_id

    def add_brand(self, new_brand):
        print(f"Adding brand: {new_brand}")
        try:
            self.cursor.execute('''INSERT INTO brands (brand) VALUES (?)''', (new_brand,))
            self.connectDatabase.commit()
            print("Brand added successfully")
        except sqlite3.OperationalError as e:
            print(f"SQLite error: {e}")

    def add_type(self, product_type):
        try:
            self.cursor.execute('''INSERT INTO product_type (product_type) VALUES (?)''', (product_type,))
            self.connectDatabase.commit()
            print("Type added successfully")
        except sqlite3.OperationalError as e:
            print(f"SQLite error: {e}")

    def fetch_brand(self):
        self.cursor.execute('''SELECT * FROM brands''')
        brands = self.cursor.fetchall()
        print(brands)
        return [brand[0] for brand in brands]

    def fetch_type(self):
        self.cursor.execute('''SELECT * FROM product_type''')
        product_type_list = self.cursor.fetchall()
        return [product_types[0] for product_types in product_type_list]