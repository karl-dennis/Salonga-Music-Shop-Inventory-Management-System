import sys
from Model.dashboardModel import dashboardModel
from View.dashboardView import dashboardView
from View.productView import productView
import tkinter as tk
from tkinter import messagebox


class dashboardController:
    def __init__(self):
        self.model = dashboardModel()
        self.view = dashboardView(self)
        
    def main(self):
        self.view.main()

    def close_window(self):
        if messagebox.askyesno('Wait', 'Do you want to Quit?'):
            self.view.quit()
            self.view.destroy()
            print("Cleanup completed. Program terminated.")
        else:
            print('Continuing Program')

    def show_dashboard(self): 
        self.view.show_dashboard()

    def show_products(self):
        self.view.clear_base_frame()
        from Controller.productController import productController
        product_controller = productController(self.view.baseFrame)
        product_controller.main()

    def show_sales(self):
        self.view.clear_base_frame()
        from Controller.salesController import salesController
        sales_controller = salesController()
        sales_controller.main()
        
    def show_deliveries(self): 
        self.view.clear_base_frame()
        from Controller.deliveryController import deliveryController
        delivery_controller = deliveryController()
        delivery_controller.main()
        
    def show_maintenance(self): 
        from Controller.maintenanceController import maintenanceController
        maintenance_controller = maintenanceController()
        maintenance_controller.main()


