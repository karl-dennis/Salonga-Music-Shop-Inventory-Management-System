from Model.resetPassModel import resetPassModel
from View.resetPassView import resetPassView
from Controller.verifyEmailController import *
from tkinter import messagebox
class resetPassController:
    def __init__(self, email):
        self.model = resetPassModel()
        self.view = resetPassView(self)
        self.verifyEmailController = email
        # self.set_email()
        # print(f'Email from last frame: {self.verifyEmailController.email()}')

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
                # print(self.verifyEmailController)
                self.model.resetPass(self.verifyEmailController, newPass)

                from Controller.loginController import loginController
                self.view.destroy()
                login_controller = loginController()
                login_controller.main()
        else:
            messagebox.showerror('Invalid', 'Missing Entries')
