from Model.dashboardModel import dashboardModel
from View.dashboardView import dashboardView
import tkinter as tk
from tkinter import messagebox

class dashboardController:
    def __init__(self):
        self.model = dashboardModel()
        self.view = dashboardView(self)
        
    def main(self):
        self.view.main()
        
    def show_dashboard(self): # Not used
        self.view.destroy()
        self.view = dashboardView(self)
        self.view.main()

    def show_products(self):
        from Controller.productController import productController
        self.view.destroy()
        product_controller = productController()
        product_controller.main()

    def show_reports(self):
        from Controller.reportController import reportController
        self.view.destroy()
        report_controller = reportController()
        report_controller.main()