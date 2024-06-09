from Model.resetPassModel import resetPassModel
from View.resetPassView import resetPassView

class resetPassController:
    def __init__(self):
        self.model = resetPassModel()
        self.view = resetPassView(self)
        
    def main(self):
        self.view.main()

    def show_verifyEmail(self):
        from Controller.verifyEmailController import verifyEmailController
        self.view.destroy()
        verifyEmail_controller = verifyEmailController()
        verifyEmail_controller.main()

    def show_login(self):
        from Controller.loginController import loginController
        self.view.destroy()
        login_controller = loginController()
        login_controller.main()