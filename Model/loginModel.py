import sqlite3
import bcrypt
import tkinter as tk
from tkinter import messagebox
import random
import smtplib


class loginModel:
    def __init__(self):
        self.connectDatabase()
    
    def login(self, username, password):
        try:
            # Retrieve the stored hashed password for the given username
            self.cursor.execute('''SELECT password FROM accounts WHERE username=?''', (username,))
            result = self.cursor.fetchone()
            
            if result is None:
                messagebox.showerror('Invalid', 'Username does not exist')
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

    def generate_otp(self):
        length = 6
        self.otp = ''
        for _ in range(length):
            self.otp += str(random.randint(0, 9))
        return self.otp
    
    def send_email(self, username):
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        self.server.login('salongamusic40@gmail.com', 'ebef pjjt eovv dkwe')

        employee_id = self.get_id_account(username)

        if employee_id:
                self.server.sendmail('salongamusic40@gmail.com', employee_id, self.generate_otp())
                print(employee_id)
        else:
            print("Error: Failed to get employee ID")

    # getting id from accounts table
    def get_id_account(self, username):
        try:
            self.cursor.execute('''SELECT employee_id FROM accounts WHERE username=?''', (username,))
            result = self.cursor.fetchone()
            
            if result is None:
                messagebox.showerror('Invalid', 'Username does not exist')
                return False
            if result:
                return self.get_id_employee(result[0])
            
        except sqlite3.Error as e:
            print('Error:', e)
            return False
    
    # getting id from employee table
    def get_id_employee(self, employee_id):
        try:
            self.cursor.execute('''SELECT email_address FROM employees WHERE employee_id=?''', (employee_id,))
            result = self.cursor.fetchone()
            if result:
                return result[0]
            else:
                return False

        except sqlite3.Error as e:
            print('Error:', e)
            return False



