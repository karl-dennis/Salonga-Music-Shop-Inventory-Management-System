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
            self.model.send_email(username)
            if loginConfirm:
                print(loginConfirm)
                messagebox.showinfo('Success', 'Login Successful')
                from Controller.dashboardController import dashboardController
                self.view.destroy()
                dashboard_controller = dashboardController()
                dashboard_controller.main()
        else:
            messagebox.showerror('Warning!','Enter all data')

    
    def forgot_pass(self):
        from Controller.verifyEmailController import verifyEmailController
        self.view.destroy()
        verifyEmail_controller = verifyEmailController()
        verifyEmail_controller.main()