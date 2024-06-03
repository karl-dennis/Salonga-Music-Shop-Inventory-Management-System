from Model.deliveryModel import deliveryModel
from View.deliveryView import deliveryView
import tkinter as tk
from tkinter import messagebox

class deliveryController:
    def __init__(self):
        self.model = deliveryModel()
        self.view = deliveryView(self)
        
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

    def show_reports(self):
        from Controller.reportController import reportController
        self.view.destroy()
        report_controller = reportController()
        report_controller.main()
    
    def show_deliveries(self): # Not used
        self.view.destroy()
        self.view = deliveryView(self)
        self.view.main()

    

