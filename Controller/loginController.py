from Model.loginModel import loginModel
from View.loginView import loginView

class loginController:
    def __init__(self):
        self.model = loginModel()
        self.view = loginView(self)

    def main(self):
        self.view.main()
    
    def on_button_click(self, username, password):
        loginConfirm = self.model.login(username, password)
        if loginConfirm:
            # Add logic for successful login, e.g., navigating to the main app window
            pass

    def switch_to_signup(self):
        from Controller.signupController import signupController
        self.view.destroy()
        signup_controller = signupController()
        signup_controller.main()
