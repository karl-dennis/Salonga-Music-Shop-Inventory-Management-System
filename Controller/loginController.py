from Model.loginModel import loginModel
from View.loginView import loginView
import tkinter as tk
from tkinter import messagebox, simpledialog
import customtkinter as ctk
from Controller.dashboardController import dashboardController
from Controller.verifyEmailController import verifyEmailController
import sys

class loginController:
    def __init__(self):
        self.model = loginModel()
        self.view = loginView(self)
        self.emp_id = None  # Initialize emp_id attribute
        self.login_attempts = 0
        self.max_attempts = 3

    def main(self):
        self.view.main()

    def on_button_click(self, username, password):
        if self.login_attempts >= self.max_attempts:
            messagebox.showerror('Error', 'Maximum login attempts exceeded.')
            sys.exit()

        if username and password:  # Ensure both username and password are provided
            login_success, self.emp_id = self.model.login(username, password)

            if login_success:
                self.model.send_email(username)
                otp = self.model.get_otp()

                print(otp)  # Debugging: Print the OTP to check its value and type

                dialog = ctk.CTkInputDialog(text="Input OTP:", title="OTP")
                dialog.geometry("200x150")
                input_otp = dialog.get_input()

                if input_otp is not None:  # Ensure the user doesn't cancel the dialog
                    try:
                        input_otp = int(input_otp)
                    except ValueError:
                        messagebox.showerror("Error", "Invalid OTP format.")
                        return

                    if input_otp == int(otp):
                        messagebox.showinfo('Success', 'Login Successful')
                        self.view.destroy()
                        dashboard_controller = dashboardController(self.emp_id)
                        dashboard_controller.main()
                    else:
                        messagebox.showerror("Warning", "Invalid OTP")
                else:
                    messagebox.showerror("Warning", "OTP input cancelled")
            else:
                self.login_attempts += 1
                if self.login_attempts >= self.max_attempts:
                    messagebox.showerror('Error', 'Maximum login attempts exceeded.')
                    sys.exit()
                else:
                    messagebox.showerror('Warning', 'Invalid login credentials')
        else:
            messagebox.showerror('Warning!', 'Enter all data')

    def forgot_pass(self):
        self.view.destroy()
        verifyEmail_controller = verifyEmailController()
        verifyEmail_controller.main()

# Example usage:
# Initialize an instance of loginController and call main()
# controller = loginController()
# controller.main()
