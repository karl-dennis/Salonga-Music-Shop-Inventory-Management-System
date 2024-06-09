from Model.verifyEmailModel import verifyEmailModel
from View.verifyEmailView import verifyEmailView

class verifyEmailController:
    def __init__(self):
        self.model = verifyEmailModel()
        self.view = verifyEmailView(self)
        
    def main(self):
        self.view.main()
    
    def show_login(self):
        from Controller.loginController import loginController
        self.view.destroy()
        login_controller = loginController()
        login_controller.main()
    
    def show_resetPass(self):
        from Controller.resetPassController import resetPassController
        self.view.destroy()
        resetPass_controller = resetPassController()
        resetPass_controller.main()