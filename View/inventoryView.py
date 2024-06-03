import customtkinter as ctk

class inventoryView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, width=428, height=352, fg_color='#FFF', corner_radius=0)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        # Add your widgets here
        label = ctk.CTkLabel(self, text="Inventory View", font=('Consolas', 14, 'bold'), text_color='#2D2D2D')
        label.pack(padx=20, pady=20)