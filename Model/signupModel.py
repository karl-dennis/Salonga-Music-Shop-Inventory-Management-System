import sqlite3
import tkinter as tk
from tkinter import messagebox
import bcrypt

class signupModel:
    def __init__(self):
        self.connectDatabase = None
        self.cursor = None
        self.create_database()
        self.create_table_employees()
        self.create_table_accounts()

    def signup(self, username, password, firstName, lastName, birthday, email):
        try:
            # Check if username already exists
            self.cursor.execute('''SELECT username FROM accounts WHERE username=?''', (username,))
            if self.cursor.fetchone() is not None:
                messagebox.showerror('Warning!', 'Username already exists.')
                return
            
            # Hash the password
            encoded_password = password.encode('utf-8')
            hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt()).decode('utf-8')

            # Insert data into employees table first
            employeesData = (firstName, lastName, birthday, email)
            self.cursor.execute('''INSERT INTO employees (first_name, last_name, birthday, email_address) 
                VALUES (?, ?, ?, ?)''', employeesData)
            
            # Get the last inserted employee_id
            employee_id = self.cursor.lastrowid
            
            # Insert data into accounts table
            accountsData = (employee_id, username, hashed_password)
            self.cursor.execute('''INSERT INTO accounts (employee_id, username, password) 
                VALUES (?, ?, ?)''', accountsData)
            
            # Commit the transaction
            self.connectDatabase.commit()

            print('Success: User signed up successfully.')
            messagebox.showinfo('Success!', 'User signed up successfully.')

        except sqlite3.Error as e:
            # Rollback in case of any error
            self.connectDatabase.rollback()
            messagebox.showerror('Error!', f'An error occurred: {e}')
            print('Error:', e)
        
        finally:
            # Ensure cursor and connection are closed
            self.cursor.close()
            self.connectDatabase.close()

    def create_database(self):
        try:
            self.connectDatabase = sqlite3.connect('salonga_music_shop.db')
            self.cursor = self.connectDatabase.cursor()
        except sqlite3.Error as e:
            print('Error:', e)

    def create_table_accounts(self):
        try:
            create_table_query_accounts = '''CREATE TABLE IF NOT EXISTS accounts(
            employee_id INTEGER NOT NULL, username TEXT, password TEXT,
            FOREIGN KEY(employee_id) REFERENCES employees(employee_id)
            )'''
            self.cursor.execute(create_table_query_accounts)
        except sqlite3.Error as e:
            print('Error:', e)
    
    def create_table_employees(self):
        try:
            create_table_query_employees = '''CREATE TABLE IF NOT EXISTS employees(
            employee_id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, birthday TEXT, email_address TEXT
            )'''
            self.cursor.execute(create_table_query_employees)
        except sqlite3.Error as e:
            print('Error:', e)