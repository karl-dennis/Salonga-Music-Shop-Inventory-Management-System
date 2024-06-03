from Model.maintenanceModel import maintenanceModel
from View.maintenanceView import maintenanceView
import tkinter as tk
from tkinter import messagebox

class maintenanceController:
    def __init__(self):
        self.model = maintenanceModel()
        self.view = maintenanceView(self)
        
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

    def show_deliveries(self): 
        from Controller.deliveryController import deliveryController
        self.view.destroy()
        delivery_controller = deliveryController()
        delivery_controller.main()
    
    def show_maintenance(self): # Not used
        self.view.destroy()
        self.view = maintenanceView(self)
        self.view.main()

