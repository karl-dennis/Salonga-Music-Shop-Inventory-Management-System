from Model.signupModel import *
from View.signupView import *
from View.loginView import loginView

class signupController:
    def __init__(self):
        self.model = signupModel()
        self.signup_view = signupView(self)
        self.login_view = loginView(self)

    def main(self):
        self.signup_view.main()
    
    def to_login(self):
        self.login_view.show_login()
        self.signup_view.hide_signup()

    def on_signup_query(self, usernameValue, passwordValue):
        # print(f'button clicked, the value is: {usernameValue} for user and {passwordValue} for password')
        result = self.model.signup(usernameValue, passwordValue)