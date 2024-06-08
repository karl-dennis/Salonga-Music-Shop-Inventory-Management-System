from Model.resetPassModel import resetPassModel
from View.resetPassView import resetPassView

class resetPassController:
    def __init__(self):
        self.model = resetPassModel()
        self.view = resetPassView(self)
        
    def main(self):
        self.view.main()