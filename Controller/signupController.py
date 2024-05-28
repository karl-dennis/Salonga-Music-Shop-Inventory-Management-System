from Model.signupModel import *
from View.signupView import *

class signupController:
    def __init__(self):
        self.model = signupModel()
        self.view = signupView(self)

    def main(self):
        self.view.main()
    
    def on_button_click(self, usernameValue, passwordValue):
        # print(f'button clicked, the value is: {usernameValue} for user and {passwordValue} for password')
        result = self.model.signup(usernameValue, passwordValue)
      