import sqlite3
from tkinter import messagebox

class deliveryTwoModel:
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

    # def fetch_products(self):
    #     try:
    #         self.cursor.execute('''SELECT product_image, product_name, product_brand, product_type, product_quantity, product_price
    #         FROM products''')
    #
    #         data = self.cursor.fetchall()
    #         infos = [list(row) for row in data]
    #         return infos
    #     except sqlite3.Error as e:
    #         print('Error: ', e)

    def create_delivery_table(self):
        try:
            create_table_query_delivery = '''CREATE TABLE IF NOT EXISTS delivery(
                delivery_id TEXT PRIMARY KEY,
                products_ordered TEXT NOT NULL,
                sub_total REAL NOT NULL,
                date TEXT NOT NULL,
                timestamp TEXT NOT NULL,
                status TEXT NOT NULL
            )'''
            self.cursor.execute(create_table_query_delivery)
        except sqlite3.Error as e:
            print('Error:', e)

    def fetch_delivery(self):
        try:
            # print("adding transaction")
            self.cursor.execute('''SELECT * FROM delivery''')

            transaction_data = self.cursor.fetchall()

            return transaction_data
        except sqlite3.Error as e:
            print('Error:', e)

    def update_delivery_status(self, delivery_id, new_status):
        # Update the status of the selected delivery
        self.cursor.execute('UPDATE delivery SET status = ? WHERE delivery_id = ?', (new_status, delivery_id))
        self.connectDatabase.commit()
        messagebox.showinfo('Success', 'Status Updated')