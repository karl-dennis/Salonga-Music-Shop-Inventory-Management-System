import sqlite3
import bcrypt
from tkinter import messagebox
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from Model.maintenanceTwoModel import *


class loginModel:
    def __init__(self):
        self.connectDatabase()
        self.maintenance = maintenanceTwoModel()
    
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
                print(type(username))
                self.cursor.execute('''SELECT employee_id FROM accounts WHERE username=?''', (username,))
                id = self.cursor.fetchone()
                print(id)
                emp_id = id[0]
                print(emp_id)
                self.cursor.execute('''SELECT level_of_access FROM employees WHERE employee_id=?''', (emp_id,))
                role = self.cursor.fetchone()
                print(role)
                self.maintenance.log_event(username, emp_id, role[0])
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

    def _generate_otp(self):
        length = 6
        self.otp = ''
        for _ in range(length):
            self.otp += str(random.randint(0, 9))
        return self.otp

    def send_email(self, username):
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        self.server.login('salongamusic40@gmail.com', 'ebef pjjt eovv dkwe')
        # 'ykqz ccoh cmpa rrii' - kurt app password

        employee_id = self.get_id_account(username)

        if employee_id:
            # Create the email
            msg = MIMEMultipart()
            msg['From'] = 'salongamusic40@gmail.com'
            msg['To'] = employee_id
            msg['Subject'] = 'Your OTP Code'

            body = self._generate_otp()
            msg.attach(MIMEText(body, 'plain'))

            # Send the email
            self.server.send_message(msg)
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

    def get_otp(self):
        return self.otp