from Model.salesTwoModel import salesTwoModel
from View.salesTwoView import salesTwoView
import tkinter as tk
from tkinter import messagebox

class salesTwoController:
    def __init__(self, parent):
        self.model = salesTwoModel()
        self.view = salesTwoView(parent, self)
        
    def main(self):
        self.view.base_frame()
    
    
    def show_firstPage(self):
        self.view.clear_base_frame()
        from Controller.salesController import salesController
        sales_controller = salesController(self.view.baseFrame)
        sales_controller.main()
        
    def show_secondPage(self):
        pass
        # self.view.show_secondPage()
    
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

    def fetch_transaction(self):
        return self.model.fetch_transaction()

    def perform_search(self, query):
        filtered_transactions = self.model.search_transactions(query)
        return filtered_transactions