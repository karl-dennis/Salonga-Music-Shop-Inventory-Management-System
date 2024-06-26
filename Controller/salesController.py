from Model.salesModel import salesModel
from View.salesView import salesView
import tkinter as tk
from tkinter import messagebox

class salesController:
    def __init__(self, parent):
        self.model = salesModel()
        self.view = salesView(parent, self)
        
    def main(self):
        self.view.base_frame()
        
    def show_firstPage(self):
        self.view.clear_base_frame()
        self.view.show_firstPage()
        
    def show_secondPage(self):
        self.view.clear_base_frame()
        from Controller.salesTwoController import salesTwoController
        salesTwo_controller = salesTwoController(self.view.baseFrame)
        salesTwo_controller.main()
        
    def set_active_tab(self, tab):
        self.view.active_tab = tab
        self.update_tab()
        
        if tab == 1:
            self.show_firstPage()
        elif tab == 2:
            self.show_secondPage()
                
    def update_tab(self):
        active_text = '#2E2E2E'
        inactive_text ='#9A9A9A'
        
        for i in range(1, 3):
            tab = getattr(self.view, f'selection{i}')
            if i == self.view.active_tab:
                tab.configure(text_color=active_text)
            else:
                tab.configure(text_color=inactive_text)

    def get_product(self):
        return self.model.fetch_products()