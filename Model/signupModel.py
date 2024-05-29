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

    def signup(self, username, password, firstName, lastName, birthday, email):
        try:
            # Check if username already exists
            self.cursor.execute('''SELECT username FROM accounts WHERE username=?''', (username,))
            if self.cursor.fetchone() is not None:
                messagebox.showerror('Warning!', 'Username already exists.')
            else:
                # Hash the password
                encoded_password = password.encode('utf-8')
                hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt()).decode('utf-8')

                # Insert username and hashed password into the database
                data = (username, hashed_password, firstName, lastName, birthday, email)
                self.cursor.execute('''INSERT INTO accounts (username, password, first_name, last_name, birthday, email_address) VALUES (?, ?, ?, ?, ?, ?)''', data)
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
            employee_id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, birthday TEXT, email_address TEXT, username TEXT, password TEXT
            )'''
            self.cursor.execute(self.create_table_query)
        except sqlite3.Error as e:
            print('Error:', e)