import sqlite3
import string
import random
from tkinter import messagebox
import bcrypt

class maintenanceModel:
    def __init__(self):
        self.connectDatabase = None
        self.cursor = None
        self.create_database()
        self.create_table_employees()
        self.create_table_accounts()

    def signup(self, username, password, first_name, last_name, birthdate, email, loa):
        try:
            # Check if username already exists
            self.cursor.execute('''SELECT username FROM accounts WHERE username=?''', (username,))
            if self.cursor.fetchone() is not None:
                messagebox.showerror('Warning!', 'Username already exists.')
                return

            # Hash the password
            encoded_password = password.encode('utf-8')
            hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt()).decode('utf-8')

            unique_id = self.generate_unique_id()
            status = 'Active'

            # Insert data into employees table first
            employeesData = (unique_id, first_name, last_name, birthdate, email, loa, status)
            # print(employeesData)
            self.cursor.execute('''INSERT INTO employees (employee_id, first_name, last_name, birthday, email_address, level_of_access, status) 
                VALUES (?, ?, ?, ?, ?, ?, ?)''', employeesData)

            # Get the last inserted employee_id
            # employee_id = self.cursor.lastrowid

            # Insert data into accounts table
            accountsData = (unique_id, username, hashed_password)
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
            employee_id TEXT NOT NULL, username TEXT, password TEXT,
            FOREIGN KEY(employee_id) REFERENCES employees(employee_id)
            )'''
            self.cursor.execute(create_table_query_accounts)
        except sqlite3.Error as e:
            print('Error:', e)

    def create_table_employees(self):
        try:
            create_table_query_employees = '''CREATE TABLE IF NOT EXISTS employees(
            employee_id TEXT PRIMARY KEY, first_name TEXT, last_name TEXT, birthday TEXT, email_address TEXT, level_of_access TEXT, status TEXT
            )'''
            self.cursor.execute(create_table_query_employees)
        except sqlite3.Error as e:
            print('Error:', e)

    def fetch_employees_with_accounts(self):
        try:
            self.create_database()
            fetch_query = '''
            SELECT employees.employee_id, employees.first_name, employees.last_name, employees.birthday, employees.email_address,
                   accounts.username, employees.level_of_access, employees.status
            FROM employees
            LEFT JOIN accounts ON employees.employee_id = accounts.employee_id
            '''
            self.cursor.execute(fetch_query)
            results = self.cursor.fetchall()
            employees_with_accounts = []
            for row in results:
                employee = [
                    row[0],  # employee_id
                    row[5],  # username
                    row[1],  # first_name
                    row[2],  # last_name
                    row[3],  # birthday
                    row[4],  # email
                    row[6],  # loa
                    row[7]   # status
                ]
                employees_with_accounts.append(employee)
            return employees_with_accounts
        except sqlite3.Error as e:
            print('Error:', e)
            return []

    def generate_unique_id(self):
        while True:
            letters = ''.join(random.choices(string.ascii_uppercase, k=3))
            digits = ''.join(random.choices(string.digits, k=4))
            unique_id = letters + digits

            self.cursor.execute('''SELECT delivery_id FROM delivery WHERE delivery_id = ?''', (unique_id,))
            if not self.cursor.fetchone():
                return unique_id

    def update(self, id, username, first_name, last_name, birthdate, email, loa):
        # Assuming your table name is 'users' and the primary key is 'user_id'
        update_query = """
            UPDATE employees 
            SET first_name = ?, last_name = ?, birthday = ?, email_address = ?, level_of_access = ?
            WHERE employee_id = ?
        """

        update_accounts = """UPDATE accounts SET username = ? WHERE employee_id = ?"""

        # Execute the update query
        self.cursor.execute(update_query, (first_name, last_name, birthdate, email, loa, id))
        self.cursor.execute(update_accounts, (username, id))
        self.connectDatabase.commit()