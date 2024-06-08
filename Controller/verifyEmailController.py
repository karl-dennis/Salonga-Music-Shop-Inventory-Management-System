from Model.verifyEmailModel import verifyEmailModel
from View.verifyEmailView import verifyEmailView

class verifyEmailController:
    def __init__(self):
        self.model = verifyEmailModel()
        self.view = verifyEmailView(self)
        
    def main(self):
        self.view.main()