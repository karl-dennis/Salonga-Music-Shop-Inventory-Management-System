from Model.deliveryModel import deliveryModel
from View.deliveryView import deliveryView
import tkinter as tk
from tkinter import messagebox

class deliveryController:
    def __init__(self, parent):
        self.model = deliveryModel()
        self.view = deliveryView(parent, self)
        
    def main(self):
        self.view.base_frame()
