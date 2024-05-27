from Model.signupModel import *
from View.signupView import *

class signupController:
    def __init__(self):
        self.model = signupModel()
        self.view = signupView(self)

    def main(self):
        self.view.main()
    
    def on_button_click(self, entryValue):
        print(f'button clicked, the value is: {entryValue}')
