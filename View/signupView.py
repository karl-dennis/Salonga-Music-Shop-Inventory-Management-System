import tkinter as tk
from tkinter import ttk
from Controller import signupController
class signupView(tk.Tk):

    def __init__(self, controller):
        
        super().__init__()
        self.controller = controller

    def main(self):
        self.mainloop()