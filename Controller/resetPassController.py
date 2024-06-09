from Model.resetPassModel import resetPassModel
from View.resetPassView import resetPassView
from Controller.verifyEmailController import *
from tkinter import messagebox
class resetPassController:
    def __init__(self):
        self.model = resetPassModel()
        self.view = resetPassView(self)
        self.verifyEmailController = verifyEmailController()
        # self.set_email()
        # print(self.verifyEmailController.email()) #it will get the users email which will link us to the users account

    def main(self):
        self.view.main()

    def show_verifyEmail(self):
        from Controller.verifyEmailController import verifyEmailController
        self.view.destroy()
        verifyEmail_controller = verifyEmailController()
        verifyEmail_controller.main()

    def show_login(self, newPass, compPass):
        if newPass != '' and compPass != '':
            if compPass != newPass:
                messagebox.showerror('Error', 'New Password and Confirm Password do not match')
                return
            elif newPass == compPass:
                self.model.resetPass(self.set_email(), newPass)

                from Controller.loginController import loginController
                self.view.destroy()
                login_controller = loginController()
                login_controller.main()
        else:
            messagebox.showerror('Invalid', 'Missing Entries')
    def set_email(self):
        self.model.get_employee_id(self.verifyEmailController.email())