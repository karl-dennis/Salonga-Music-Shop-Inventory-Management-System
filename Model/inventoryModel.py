import sqlite3
class inventoryModel:
    def __init__(self):
        self.connectDatabase = None
        self.cursor = None

        self.createDatabase()
        self.create_product_table()

    def createDatabase(self):
        try:
            self.connectDatabase = sqlite3.connect('salonga_music_shop.db')
            self.cursor = self.connectDatabase.cursor()
        except sqlite3.Error as e:
            print('Error:', e)

    def create_product_table(self):
        try:
            create_table_query_products = '''CREATE TABLE IF NOT EXISTS products(
            product_id INTEGER PRIMARY KEY, product_name TEXT, product_price INTEGER, stock_level INTEGER, category TEXT
            )'''
            self.cursor.execute(create_table_query_products)
        except sqlite3.Error as e:
            print('Error:', e)
