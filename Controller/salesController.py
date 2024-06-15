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
