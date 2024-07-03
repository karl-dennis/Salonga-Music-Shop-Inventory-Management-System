import sqlite3
from datetime import datetime

class statisticModel:
    def __init__(self):
        self.connectDatabase = None
        self.cursor = None
        self.connect_database()

    def connect_database(self):
        try:
            self.connectDatabase = sqlite3.connect('salonga_music_shop.db')
            self.cursor = self.connectDatabase.cursor()
        except sqlite3.Error as e:
            print('Error:', e)
            
    def fetch_revenue(self):
        try:
            start_of_month = datetime.now().replace(day=1).strftime('%Y-%m-%d')
            end_of_month = datetime.now().strftime('%Y-%m-%d')

            self.cursor.execute("""
                SELECT SUM(revenue) 
                FROM transactions 
                WHERE date BETWEEN ? AND ?
            """, (start_of_month, end_of_month))
            revenue_data = self.cursor.fetchone()

            total_revenue = revenue_data[0] if revenue_data[0] is not None else 0

            return total_revenue

        except sqlite3.Error as e:
            print('Error:', e)
            return 0
