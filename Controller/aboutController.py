from Model.aboutModel import aboutModel
from View.aboutView import aboutView
import tkinter as tk
from tkinter import messagebox

class aboutController:
    def __init__(self, parent):
        self.model = aboutModel()
        self.view = aboutView(parent, self)
        
    def main(self):
        self.view.base_frame()
        
    def show_aboutOne(self):
        pass
    
    def show_aboutTwo(self):
        self.view.clear_base_frame()
        from Controller.aboutTwoController import aboutTwoController
        aboutTwo_controller = aboutTwoController(self.view.baseFrame)
        aboutTwo_controller.main()
    
    def set_active_tab(self, tab):
        self.view.active_tab = tab
        self.update_tab()

        if tab == 1:
            self.show_aboutOne()
        elif tab == 2:
            self.show_aboutTwo()
 
            
    def update_tab(self):
        active_text = '#2E2E2E'
        inactive_text = '#9A9A9A'

        for i in range(1, 3):
            tab = getattr(self.view, f'selection{i}')
            if i == self.view.active_tab:
                tab.configure(text_color=active_text)
            else:
                tab.configure(text_color=inactive_text)
    
        