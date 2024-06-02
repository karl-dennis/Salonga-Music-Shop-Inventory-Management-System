from Model.productModel import productModel
from View.productView import productView
import tkinter as tk
from tkinter import messagebox

class productController:
    def __init__(self):
        self.model = productModel()
        self.view = productView(self)
        
    def main(self):
        self.view.main()
        
    def show_dashboard(self):
        from Controller.dashboardController import dashboardController
        self.view.destroy()
        dashboard_controller = dashboardController()
        dashboard_controller.main()

    def show_products(self): # Not used
        self.view.destroy()
        self.view = productView(self)
        self.view.main()
        
    def show_reports(self): 
        from Controller.reportController import reportController
        self.view.destroy()
        report_controller = reportController()
        report_controller.main()


