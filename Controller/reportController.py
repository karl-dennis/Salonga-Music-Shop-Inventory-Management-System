from Model.reportModel import reportModel
from View.reportView import reportView
import tkinter as tk
from tkinter import messagebox

class reportController:
    def __init__(self):
        self.model = reportModel()
        self.view = reportView(self)
        
    def main(self):
        self.view.main()
        
    def show_dashboard(self):
        from Controller.dashboardController import dashboardController
        self.view.destroy()
        dashboard_controller = dashboardController()
        dashboard_controller.main()

    def show_products(self):
        from Controller.productController import productController
        self.view.destroy()
        product_controller = productController()
        product_controller.main()

    def show_reports(self): # Not used
        self.view.destroy()
        self.view = reportView(self)
        self.view.main()

    def show_deliveries(self): 
        from Controller.deliveryController import deliveryController
        self.view.destroy()
        delivery_controller = deliveryController()
        delivery_controller.main()
    

