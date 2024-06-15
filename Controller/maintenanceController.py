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
        