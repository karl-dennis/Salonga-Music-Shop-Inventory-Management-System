from Model.loginModel import *
from View.loginView import *

class loginController:
    def __init__(self):
        self.model = loginModel()
        self.view = loginView(self)
        
    def main(self):
        self.view.main()
    
    def on_button_click(self, username, password):
        # print(f'on controller with username: {username} and password: {password}')
        loginConfirm = self.model.login(username, password)