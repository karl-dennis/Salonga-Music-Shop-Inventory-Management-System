from Model.inventoryModel import *
from View.inventoryView import *

class inventoryController:
    def __init__(self):
        self.model = inventoryModel()
        self.view = inventoryView(self)
    
    def main(self):
        pass
