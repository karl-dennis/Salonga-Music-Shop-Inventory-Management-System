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

    def save_button_clicked(self, product_name, type, brand, quantity, price):
        # For debugging purposes
        print('In controller')
        print(f'Product Name: {product_name}')
        print(f'Product Type: {type}')
        print(f'Product Brand: {brand}')
        print(f'Product Quantity: {quantity}')
        print(f'Product Price: {price}')
        self.model.add_products(product_name,type,brand,quantity,price)
