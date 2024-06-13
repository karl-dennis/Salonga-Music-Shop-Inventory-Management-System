from Model.verifyEmailModel import verifyEmailModel
from View.verifyEmailView import verifyEmailView
from tkinter import messagebox

class verifyEmailController:
    def __init__(self):
        self.model = verifyEmailModel()
        self.view = verifyEmailView(self)
        
    def main(self):
        self.view.main()

    def set_email(self, email):
        self.model.set_email(email)

    def show_login(self):
        from Controller.loginController import loginController
        self.view.destroy()
        login_controller = loginController()
        login_controller.main()

    def show_resetPass(self):
        input_otp = self.view.get_otp()
        generated_otp = self.model.get_otp()

        if input_otp == generated_otp:
            from Controller.resetPassController import resetPassController
            self.view.destroy()
            resetPass_controller = resetPassController(self.view.get_email_from_view())
            resetPass_controller.main()
        else:
            messagebox.showerror('Warning', 'Incorrect')

    def email(self):
        print(self.view.get_email_from_view())
        return self.view.get_email_from_view()