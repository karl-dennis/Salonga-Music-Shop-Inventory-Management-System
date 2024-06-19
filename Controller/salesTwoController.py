from Model.salesTwoModel import salesTwoModel
from View.salesTwoView import salesTwoView
import tkinter as tk
from tkinter import messagebox

class salesTwoController:
    def __init__(self, parent):
        self.model = salesTwoModel()
        self.view = salesTwoView(parent, self)
        
    def main(self):
        self.view.base_frame()
    
    
    def show_firstPage(self):
        self.view.clear_base_frame()
        from Controller.salesController import salesController
        sales_controller = salesController(self.view.baseFrame)
        sales_controller.main()
        
    def show_secondPage(self):
        pass
        # self.view.show_secondPage()