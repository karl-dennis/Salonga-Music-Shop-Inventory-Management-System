from Model.salesModel import salesModel
from View.salesView import salesView
import tkinter as tk
from tkinter import messagebox

class salesController:
    def __init__(self):
        self.model = salesModel()
        self.view = salesView(self)
        
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

    def show_sales(self): # Not used
        self.view.destroy()
        self.view = salesView(self)
        self.view.main()

    def show_deliveries(self): 
        from Controller.deliveryController import deliveryController
        self.view.destroy()
        delivery_controller = deliveryController()
        delivery_controller.main()
    
    def show_maintenance(self): 
        from Controller.maintenanceController import maintenanceController
        self.view.destroy()
        maintenance_controller = maintenanceController()
        maintenance_controller.main()

