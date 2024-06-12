import sqlite3
from tkinter import messagebox
import bcrypt

class resetPassModel:
    def __init__(self):
        self.connectDatabase()

    def connectDatabase(self):
        try:
            self.connection = sqlite3.connect('salonga_music_shop.db')
            self.cursor = self.connection.cursor()
        except sqlite3.Error as e:
            print('Error:', e)

    def get_employee_id(self, email):
        self.cursor.execute('''SELECT employee_id FROM employees WHERE email_address = ?''', (email,))
        result = self.cursor.fetchone()
        if result is None:
            messagebox.showerror('Warning', 'Email Address does not exist')
            return False
        if result:
            return result[0]

    def resetPass(self, id, new_password):
        employee_id = self.get_employee_id(id)
        print(employee_id)
        if not employee_id:
            return False

        try:
            hash = self.hash_password(new_password)
            self.cursor.execute('''UPDATE accounts SET password = ? WHERE employee_id = ?''',
                                (hash, employee_id))
            self.connection.commit()
            messagebox.showinfo('Success', 'Password has been reset successfully')
            return True
        except sqlite3.Error as e:
            print('Error:', e)
            messagebox.showerror('Error', 'Failed to reset password')
            return False

    def hash_password(self, password):
        encoded_password = password.encode('utf-8')
        hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt()).decode('utf-8')
        return hashed_password
