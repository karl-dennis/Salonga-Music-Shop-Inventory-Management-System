import sys

from Model.dashboardModel import dashboardModel
from View.dashboardView import dashboardView
# controller of inventory

import tkinter as tk
from tkinter import messagebox

class dashboardController:
    def __init__(self):
        self.model = dashboardModel()
        self.view = dashboardView(self)
        
    def main(self):
        self.view.main()

    def close_window(self):
        if messagebox.askyesno('Wait','Do you want to Quit?'):
            self.view.quit()
            self.view.destroy()
            print("Cleanup completed. Program terminated.")
        else:
            print('Continuing Program')


    def show_dashboard(self): # Not used
        self.view.destroy()
        self.view = dashboardView(self)
        self.view.main()

    def show_products(self):
        from Controller.productController import productController
        self.view.destroy()
        product_controller = productController()
        product_controller.main()

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


