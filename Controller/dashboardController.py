from Model.dashboardModel import dashboardModel
from View.dashboardView import dashboardView
import tkinter as tk
from tkinter import messagebox

class dashboardController:
    def __init__(self):
        self.model = dashboardModel()
        self.view = dashboardView(self)
        
    def main(self):
        self.view.main()