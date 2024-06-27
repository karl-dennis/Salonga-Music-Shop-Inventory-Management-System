import sqlite3
class deliveryModel:
    def __init__(self):
        self.connectDatabase = None
        self.cursor = None
        self.connect_database()
        # self.create_table_products()
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
                product_image BLOB
            )'''
            self.cursor.execute(create_table_query_products)
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
                
            )'''
            self.cursor.execute(create_table_query_transactions)
        except sqlite3.Error as e:
            print('Error:', e)
