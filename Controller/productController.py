from Model.productModel import productModel
from View.productView import productView
import tkinter as tk
from tkinter import messagebox

class productController:
    def __init__(self, parent):
        self.model = productModel()
        self.view = productView(parent, self)
        
    def main(self):
        self.view.base_frame()
