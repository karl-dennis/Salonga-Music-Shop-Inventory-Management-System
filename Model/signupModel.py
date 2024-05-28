import sqlite3

class signupModel:
    def __init__(self):
        self.connectDatabase = None
        self.cursor = None
    
    def signup(self, username, password):
        try:
            self.create_database()
            self.create_table()
            self.cursor.execute('''INSERT INTO accounts(username, password) VALUES (?, ?)''', (username, password))
            self.connectDatabase.commit()
            print('Success: User signed up successfully.')
        except sqlite3.Error as e:
            print('Error:', e)
        finally:
            self.disconnect_database()
    
    def create_database(self):
        try:
            self.connectDatabase = sqlite3.connect('salonga_music_shop.db')
            self.cursor = self.connectDatabase.cursor()
        except sqlite3.Error as e:
            print('Error:', e)
    
    def create_table(self):
        try:
            self.create_table_query = '''CREATE TABLE IF NOT EXISTS accounts(
            username TEXT, password TEXT
            )'''
            self.connectDatabase.execute(self.create_table_query)
        except sqlite3.Error as e:
            print('Error:', e)
    
    def disconnect_database(self):
        if self.connectDatabase:
            self.connectDatabase.close()