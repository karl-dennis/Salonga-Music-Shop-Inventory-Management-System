import sqlite3
import bcrypt

class loginModel:
    def __init__(self):
        self.connectDatabase()
    
    def login(self, username, password):
        try:
            # Retrieve the stored hashed password for the given username
            self.cursor.execute('''SELECT password FROM accounts WHERE username=?''', (username,))
            result = self.cursor.fetchone()
            
            if result is None:
                print('Error: Username does not exist.')
                return False
            
            stored_hashed_password = result[0]
            
            # Verify the provided password against the stored hashed password
            if bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password.encode('utf-8')):
                print('Success: User logged in successfully.')
                return True
            else:
                print('Error: Incorrect password.')
                return False

        except sqlite3.Error as e:
            print('Error:', e)
            return False
    
    def connectDatabase(self):
        try:
            self.connectDatabase = sqlite3.connect('salonga_music_shop.db')
            self.cursor = self.connectDatabase.cursor()
        except sqlite3.Error as e:
            print('Error:', e)
