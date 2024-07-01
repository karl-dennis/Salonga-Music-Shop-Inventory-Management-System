import sqlite3
from datetime import datetime, date

class stockAlertsModel:
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
            
    def fetch_transaction(self):
        try:
            date = datetime.now().strftime('%Y-%m-%d')

            self.cursor.execute("SELECT transaction_id, customer_name, customer_contact, revenue, timestamp FROM transactions WHERE date LIKE ? ORDER BY timestamp DESC",
                                (date,))
            transaction_data = self.cursor.fetchall()

            # Print fetched data for debugging
            # print("Fetched transactions:", transaction_data)
            data = [list(row) for row in transaction_data]
            return data

        except sqlite3.Error as e:
            print('Error:', e)
            return None