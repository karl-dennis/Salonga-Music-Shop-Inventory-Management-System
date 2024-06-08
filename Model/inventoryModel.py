import sqlite3

class inventoryModel:
    def __init__(self):
        self.connectDatabase = None
        self.cursor = None
        self.connect_database()
        self.create_table_products()
        self.create_table_stock()

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
                product_price INTEGER,
                category TEXT
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

# if __name__ == '__main__':
#     model = InventoryModel()
