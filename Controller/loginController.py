from Model.loginModel import *
from View.loginView import *
from View.signupView import signupView

class loginController:
    def __init__(self):
        self.model = loginModel()
        self.login_view = loginView(self)
        self.signup_view = signupView(self)
        
    def main(self):
        self.login_view.main()
    
    def to_signup(self):
        self.signup_view.show_signup()
        self.login_view.hide_login()
        
    def on_login_query(self, username, password):
        # print(f'on controller with username: {username} and password: {password}')
        loginConfirm = self.model.login(username, password)