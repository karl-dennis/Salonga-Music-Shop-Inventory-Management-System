from Model.loginModel import loginModel
from View.loginView import loginView
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

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
                self.model.send_email(username)
                otp = self.model.get_otp()

                print(otp)  # Debugging: Print the OTP to check its value and type

                input_otp = simpledialog.askinteger("OTP", "Input OTP")

                if input_otp is not None:  # Ensure the user doesn't cancel the dialog
                    # Convert OTP to the same type for comparison
                    try:
                        otp = int(otp)
                    except ValueError:
                        messagebox.showerror("Error", "OTP format is invalid.")
                        return

                    if input_otp == otp:
                        messagebox.showinfo('Success', 'Login Successful')
                        from Controller.dashboardController import dashboardController
                        self.view.destroy()
                        dashboard_controller = dashboardController()
                        dashboard_controller.main()
                    else:
                        messagebox.showerror("Warning", "Invalid Input")
                else:
                    messagebox.showerror("Warning", "OTP input cancelled")
            else:
                messagebox.showerror('Warning', 'Invalid login credentials')
        else:
            messagebox.showerror('Warning!', 'Enter all data')

    def forgot_pass(self):
        from Controller.verifyEmailController import verifyEmailController
        self.view.destroy()
        verifyEmail_controller = verifyEmailController()
        verifyEmail_controller.main()