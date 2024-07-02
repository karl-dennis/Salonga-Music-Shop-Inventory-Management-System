import sqlite3
from datetime import datetime, date

class salesTwoModel:
    def __init__(self):
        self.connectDatabase = None
        self.cursor = None
        self.connect_database()
        # self.create_transaction_table()

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

    def fetch_transaction(self):
        try:
            date = datetime.now().strftime('%Y-%m-%d')

            self.cursor.execute('''SELECT transaction_id, customer_name, customer_contact, products_ordered, revenue, date, timestamp 
                                   FROM transactions WHERE date LIKE ? ORDER BY timestamp DESC''',
                                (date,))
            transaction_data = self.cursor.fetchall()

            # Print fetched data for debugging
            # print("Fetched transactions:", transaction_data)

            return transaction_data

        except sqlite3.Error as e:
            print('Error:', e)
            return None

    def search_transactions(self, query):
        try:
            # Adjust the query to your database schema and search criteria
            search_query = f"%{query}%"
            self.cursor.execute(
                "SELECT * FROM transactions WHERE customer_name LIKE ? OR customer_contact LIKE ? OR date LIKE ?",
                (search_query, search_query, search_query,))
            filtered_transactions = self.cursor.fetchall()

            return filtered_transactions

        except sqlite3.Error as e:
            print('Error:', e)
            return None
    # def save_transaction(self, name, contact, totalPrice, products_ordered, date, timestamp):
    #     # print(f"In model\nName: {name}, Contact: {contact}, Total Price: {totalPrice}, Date: {date}, Time: {timestamp}")
    #     # for row in products_ordered:
    #     #     print(f"Product: {row['name']}, Brand: {row['brand']}, Quantity: {row['quantity']}, Price: {row['price']}")
    #     try:
    #         print("adding transaction")
    #         transaction_id = self.generate_unique_id()
    #         self.cursor.execute('''INSERT INTO transactions (transaction_id, customer_name, customer_contact, products_ordered, revenue, date, timestamp)
    #                             VALUES (?, ?, ?, ?, ?, ?, ?)''',
    #                             (transaction_id, name, contact, products_ordered, totalPrice, date, timestamp))
    #
    #         self.connectDatabase.commit()
    #         messagebox.showinfo('Success', 'Transaction Successful')
    #     except sqlite3.Error as e:
    #         print('Error:', e)