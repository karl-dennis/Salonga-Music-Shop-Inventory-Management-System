import sqlite3

class productModel:
    def __init__(self):
        self.connectDatabase = None
        self.cursor = None
        self.connect_database()
        self.create_table_products()

        # self.create_brand_table()
        # self.create_table_stock()

    def connect_database(self):
        try:
            self.connectDatabase = sqlite3.connect('salonga_music_shop.db')
            self.cursor = self.connectDatabase.cursor()
        except sqlite3.Error as e:
            print('Error:', e)

    def create_table_products(self):
        try:
            create_table_query_products = '''CREATE TABLE IF NOT EXISTS products(
                product_id INTEGER PRIMARY KEY,
                product_name TEXT,
                product_brand TEXT,
                product_type TEXT,
                product_quantity INTEGER,
                product_price REAL NOT NULL
            )'''
            self.cursor.execute(create_table_query_products)
        except sqlite3.Error as e:
            print('Error:', e)

    def create_table_stock(self):
        try:
            create_table_query_stocks = '''CREATE TABLE IF NOT EXISTS stock_items(
                stock_id INTEGER PRIMARY KEY,
                product_id INTEGER,
                FOREIGN KEY (product_id) REFERENCES products (product_id)
            )'''
            self.cursor.execute(create_table_query_stocks)
        except sqlite3.Error as e:
            print('Error:', e)

    def create_brand_table(self):
        try:
            create_table_query_stocks = '''CREATE TABLE IF NOT EXISTS brands(
                brand)'''
            self.cursor.execute(create_table_query_stocks)
        except sqlite3.Error as e:
            print('Error:', e)

    def add_products(self, name, type, brand, quantity, price):
        # Debugging purposes
        print('In model')
        print(f'Product Name: {name}')
        print(f'Product Type: {type}')
        print(f'Product Brand: {brand}')
        print(f'Product Quantity: {quantity}')
        print(f'Product Price: {price}')

        product_data = (name, brand, type, quantity,price)

        try:
            self.cursor.execute('''INSERT INTO products (product_name, product_brand, product_type, product_quantity, product_price)
            VALUES (?, ?, ?, ?, ?)''', product_data)

            self.connectDatabase.commit()
        except sqlite3.Error as e:
            print('Error:', e)




