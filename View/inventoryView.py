import customtkinter as ctk

class inventoryView(ctk.CTkFrame):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

    def main(self):
        self.mainloop()

    def create_widgets(self):
        # Create a frame to hold the inventory view widgets
        self.inventory_frame = ctk.CTkFrame(self, width=600, height=400, fg_color='#FFFFFF', corner_radius=0)
        self.inventory_frame.pack(fill='both', expand=True)

        # Add your inventory view widgets here, for example:
        self.label = ctk.CTkLabel(self.inventory_frame, text="Inventory View", font=('Consolas', 12, 'bold'), text_color="#2D2D2D")
        self.label.place(x=20, y=20)