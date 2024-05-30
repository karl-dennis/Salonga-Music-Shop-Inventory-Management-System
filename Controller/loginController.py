from Model.loginModel import loginModel
from View.loginView import loginView
import tkinter as tk
from tkinter import messagebox

class loginController:
    def __init__(self):
        self.model = loginModel()
        self.view = loginView(self)

    def main(self):
        self.view.main()
    
    def on_button_click(self, username, password):
        if username != '' and password != '':
            loginConfirm = self.model.login(username, password)
            if loginConfirm:
                print(loginConfirm)
        else:
            messagebox.showerror('Warning!','Enter all data')

    def switch_to_signup(self):
        from Controller.signupController import signupController
        self.view.destroy()
        signup_controller = signupController()
        signup_controller.main()
