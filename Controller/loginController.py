from Model.loginModel import *
from View.loginView import *

class loginController:
    def __init__(self):
        self.model = loginModel()
        self.view = loginView(self)
        
    def main(self):
        self.view.main()
        
    