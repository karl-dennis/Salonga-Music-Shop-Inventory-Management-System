from Model.loginModel import *
from View.loginView import *
from View.signupView import *

class loginController:
    def __init__(self):
        self.model = loginModel()
        self.login_view = loginView(self)
        self.signup_view = signupView(self)
        
    def main(self):
        self.login_view.main()
    
    def to_signup(self):
        self.signup_view.signupFrame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, relwidth=0.7, relheight=0.7)
        self.login_view.loginFrame.place_forget()
        self.signup_view.deiconify()
        self.login_view.withdraw()

    
    def on_button_click(self, username, password):
        # print(f'on controller with username: {username} and password: {password}')
        loginConfirm = self.model.login(username, password)