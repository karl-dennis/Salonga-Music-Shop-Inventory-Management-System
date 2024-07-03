
import sys
from Model.dashboardModel import dashboardModel
from View.dashboardView import dashboardView
from View.productView import productView
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class dashboardController:
    def __init__(self, id):
        self.model = dashboardModel()
        self.loa = self.model.get_loa(id)
        self.view = dashboardView(self)
        self.id = id
    
    
    def get_loa(self):
        return self.loa
    
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

    def show_login(self):
        from Controller.loginController import loginController
        
        current_datetime = datetime.now()
        current_time_date_str = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        print(current_time_date_str)
        
        self.view.destroy()
        login_controller = loginController()
        login_controller.main()
    
    def show_products(self):
        self.view.clear_base_frame()
        from Controller.productController import productController
        product_controller = productController(self.view.baseFrame)
        product_controller.main()

    def show_sales(self):
        self.view.clear_base_frame()
        from Controller.salesController import salesController
        sales_controller = salesController(self.view.baseFrame)
        sales_controller.main()
        
    def show_deliveries(self): 
        self.view.clear_base_frame()
        from Controller.deliveryController import deliveryController
        delivery_controller = deliveryController(self.view.baseFrame)
        delivery_controller.main()
        
    def show_maintenance(self): 
        from Controller.maintenanceController import maintenanceController
        maintenance_controller = maintenanceController(self.view.baseFrame)
        maintenance_controller.main()
        
    def show_about(self):
        from Controller.aboutController import aboutController
        about_controller = aboutController(self.view.baseFrame)
        about_controller.main()


