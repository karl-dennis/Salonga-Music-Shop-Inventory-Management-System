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

    def save_button_clicked(self, product_name, type, brand, quantity, price, image, capital_price):
        # For debugging purposes
        # print('In controller')
        # print(f'Product Name: {product_name}')
        # print(f'Product Type: {type}')
        # print(f'Product Brand: {brand}')
        # print(f'Product Quantity: {quantity}')
        # print(f'Product Price: {price}')
        self.model.add_products(product_name,type,brand,quantity,price, image, capital_price)

    def add_brand(self, brand):
        self.model.add_brand(brand)
    def get_brand(self):
        return self.model.fetch_brand()

    def add_type(self, type_name):
        self.model.add_type(type_name)

    def get_type(self):
        return self.model.fetch_type()

    def get_data(self):
        return self.model.fetch_data()