from Model.maintenanceModel import maintenanceModel
from View.maintenanceView import maintenanceView
import tkinter as tk
from tkinter import messagebox

class maintenanceController:
    def __init__(self, parent):
        self.model = maintenanceModel()
        self.view = maintenanceView(parent, self)
    
    def main(self):
        self.view.base_frame()
        
    def show_maintenanceOne(self):
        pass
    
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
    
    def get_employees_with_accounts(self):
        print(self.model.fetch_employees_with_accounts())
        return self.model.fetch_employees_with_accounts()

    def save_button_clicked(self, username, password, first_name, last_name, birthdate, email, loa):
        self.model.signup(username, password, first_name, last_name, birthdate, email, loa)

    def update(self, id, username, first_name, last_name, birthdate, email, loa):
        self.model.update(id, username, first_name, last_name, birthdate, email, loa)