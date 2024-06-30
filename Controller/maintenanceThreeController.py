from Model.maintenanceThreeModel import maintenanceThreeModel
from View.maintenanceThreeView import maintenanceThreeView
import tkinter as tk
from tkinter import messagebox

class maintenanceThreeController:
    def __init__(self, parent):
        self.model = maintenanceThreeModel()
        self.view = maintenanceThreeView(parent, self)
        
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
        pass
        
    def show_maintenanceFour(self):
        self.view.clear_base_frame()
        from Controller.maintenanceFourController import maintenanceFourController
        maintenanceFour_controller = maintenanceFourController(self.view.baseFrame)
        maintenanceFour_controller.main()
        
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
            
    def update_tab(self):
        active_text = '#2E2E2E'
        inactive_text = '#9A9A9A'

        for i in range(1, 5):
            tab = getattr(self.view, f'selection{i}')
            if i == self.view.active_tab:
                tab.configure(text_color=active_text)
            else:
                tab.configure(text_color=inactive_text)
    