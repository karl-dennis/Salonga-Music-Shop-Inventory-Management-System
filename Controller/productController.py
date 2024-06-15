from Model.productModel import productModel
from View.productView import productView
import tkinter as tk
from tkinter import messagebox

class productController:
    def __init__(self, parent):
        self.model = productModel()
        self.view = productView(parent, self)
        
    def main(self):
        self.view.base_frame()
                
    def show_dashboard(self):
        from Controller.dashboardController import dashboardController
        self.view.destroy()
        dashboard_controller = dashboardController()
        dashboard_controller.main()

    def show_products(self):
        self.view.destroy()
        self.view = productView(self)
        
    def show_sales(self): 
        from Controller.salesController import salesController
        self.view.destroy()
        report_controller = salesController()
        report_controller.main()

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
