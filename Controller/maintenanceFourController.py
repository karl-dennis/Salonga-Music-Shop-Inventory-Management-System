from Model.maintenanceFourModel import maintenanceFourModel
from View.maintenanceFourView import maintenanceFourView
import tkinter as tk
from tkinter import messagebox

class maintenanceFourController:
    def __init__(self, parent):
        self.model = maintenanceFourModel()
        self.view = maintenanceFourView(parent, self)
        
    def main(self):
        self.view.base_frame()
        
    def show_maintenanceOne(self):
        self.view.clear_base_frame()
        from Controller.maintenanceController import maintenanceController
        maintenance_controller = maintenanceController(self.view.baseFrame)
        maintenance_controller.main()
    
    def show_maintenanceTwo(self):
        self.view.clear_base_frame()
        from Controller.maintenanceTwoController import maintenanceTwoController
        maintenanceTwo_controller = maintenanceTwoController(self.view.baseFrame)
        maintenanceTwo_controller.main()
    
    def show_maintenanceThree(self):
        self.view.clear_base_frame()
        from Controller.maintenanceThreeController import maintenanceThreeController
        maintenanceThree_controller = maintenanceThreeController(self.view.baseFrame)
        maintenanceThree_controller.main()
        
    def show_maintenanceFour(self):
        pass
    
    def show_maintenanceFive(self):
        self.view.clear_base_frame()
        from Controller.maintenanceFiveController import maintenanceFiveController
        maintenanceFive_controller = maintenanceFiveController(self.view.baseFrame)
        maintenanceFive_controller.main()
    
    def set_active_tab(self, tab):
        self.view.active_tab = tab
        self.update_tab()

        if tab == 1:
            self.show_maintenanceOne()
        elif tab == 2:
            self.show_maintenanceTwo()
        elif tab == 3:
            self.show_maintenanceThree()
        elif tab == 4:
            self.show_maintenanceFour()
        elif tab == 5:
            self.show_maintenanceFive()
        
    def update_tab(self):
        active_text = '#2E2E2E'
        inactive_text = '#9A9A9A'

        for i in range(1, 6):
            tab = getattr(self.view, f'selection{i}')
            if i == self.view.active_tab:
                tab.configure(text_color=active_text)
            else:
                tab.configure(text_color=inactive_text)

    def get_data(self):
        return self.model.fetch_data()

    def get_month_data(self):
        return self.model.fetch_month_data()

    def get_overall_data(self):
        return self.model.fetch_overall_data()
    
    def update_transaction_status(self, selected_transaction_id, selected_value):
        print(selected_transaction_id, selected_value)
        self.model.update_transaction_status(selected_transaction_id, selected_value)
    