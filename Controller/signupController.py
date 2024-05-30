from Model.signupModel import signupModel
from View.signupView import signupView
import tkinter as tk
from tkinter import messagebox

class signupController:
    def __init__(self):
        self.model = signupModel()
        self.view = signupView(self)

    def main(self):
        self.view.main()

    def on_button_click(self, usernameValue, passwordValue, firstNameValue, lastNameValue, birthdayValue, emailValue):
        if usernameValue != '' and passwordValue != '' and firstNameValue != '' and lastNameValue != '' and birthdayValue != '' and emailValue != '':
            result = self.model.signup(usernameValue, passwordValue, firstNameValue, lastNameValue, birthdayValue, emailValue)
            self.switch_to_login()
        else:
            messagebox.showerror('Warning!','Enter all data')

    def back_button_on_click(self):
        self.switch_to_login()

    def switch_to_login(self):
        from Controller.loginController import loginController
        self.view.destroy()
        login_controller = loginController()
        login_controller.main()
