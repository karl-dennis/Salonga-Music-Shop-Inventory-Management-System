from Model.salesModel import salesModel
from View.salesView import salesView
import tkinter as tk
from tkinter import messagebox

class salesController:
    def __init__(self, parent):
        self.model = salesModel()
        self.view = salesView(parent, self)
        
    def main(self):
        self.view.base_frame()
        
    def show_firstPage(self):
        self.view.show_firstPage()
        
    def show_secondPage(self):
        pass
        # self.view.clear_sales_frame()
        # from Controller.salesTwoController import salesTwoController
        # salesTwo_controller = salesTwoController(self.view.salesFrame)
        # salesTwo_controller.main()
