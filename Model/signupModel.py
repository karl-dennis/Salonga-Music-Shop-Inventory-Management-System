import sqlite3
import tkinter as tk
from tkinter import messagebox
import bcrypt

class signupModel:
    def __init__(self):
        self.connectDatabase = None
        self.cursor = None
        self.create_database()
        self.create_table()

    def signup(self, username, password):
        try:
            # Check if username already exists
            self.cursor.execute('''SELECT username FROM accounts WHERE username=?''', (username,))
            if self.cursor.fetchone() is not None:
                messagebox.showerror('Warning!', 'Username already exists.')
            else:
                # Hash the password
                encoded_password = password.encode('utf-8')
                hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())

                # Insert username and hashed password into the database
                self.cursor.execute('''INSERT INTO accounts (username, password) VALUES (?, ?)''', (username, hashed_password))
                self.connectDatabase.commit()
                print('Success: User signed up successfully.')
                messagebox.showinfo('Success!', 'User signed up successfully.')

        except sqlite3.Error as e:
            print('Error:', e)

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
            self.cursor.execute(self.create_table_query)
        except sqlite3.Error as e:
            print('Error:', e)
