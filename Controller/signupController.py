from Model.signupModel import signupModel
from View.signupView import signupView
# import tkinter as tk
from tkinter import messagebox
import re

class signupController:
    def __init__(self):
        self.model = signupModel()
        self.view = signupView(self)

    def main(self):
        self.view.main()

    def on_button_click(self, usernameValue, passwordValue, firstNameValue, lastNameValue, birthdayValue, emailValue):
        username_pattern = re.compile(r'^[a-zA-Z0-9]{6,}$')
        password_pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[~`!@#$%^&*()\-_=+{}[\]\\|;:"<>,./?]).+$')

        if usernameValue and passwordValue and firstNameValue and lastNameValue and birthdayValue and emailValue:
            if username_pattern.match(usernameValue):
                if password_pattern.match(passwordValue):
                    result = self.model.signup(usernameValue, passwordValue, firstNameValue, lastNameValue,
                                               birthdayValue, emailValue)
                    self.switch_to_login()
                else:
                    messagebox.showerror('Warning!',
                                         'Password must contain at least one lowercase letter, one uppercase letter, one numeric character, and one special character.')
            else:
                messagebox.showerror('Warning!',
                                     'Username must be at least 6 characters long and contain only alphanumeric characters.')
        else:
            messagebox.showerror('Warning!', 'Enter all data')

    def back_button_on_click(self):
        self.switch_to_login()

    def switch_to_login(self):
        from Controller.loginController import loginController
        self.view.destroy()
        login_controller = loginController()
        login_controller.main()
