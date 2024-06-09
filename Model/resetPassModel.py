import sqlite3
from tkinter import messagebox


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
            messagebox.showerror('Warning', 'Email Addressssss does not exist')
            return False
        if result:
            return result[0]

    def resetPass(self, email, new_password):
        employee_id = self.get_employee_id(email)
        if not employee_id:
            return False

        try:
            self.cursor.execute('''UPDATE accounts SET password = ? WHERE employee_id = ?''',
                                (new_password, employee_id))
            self.connection.commit()
            messagebox.showinfo('Success', 'Password has been reset successfully')
            return True
        except sqlite3.Error as e:
            print('Error:', e)
            messagebox.showerror('Error', 'Failed to reset password')
            return False
