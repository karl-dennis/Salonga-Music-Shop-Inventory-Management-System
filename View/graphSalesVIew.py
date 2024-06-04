import customtkinter as ctk

class graphSalesView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, width=400, height=352, fg_color='#FFF', corner_radius=0)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        # Add your widgets here
        label = ctk.CTkLabel(self, text="Graph of Sales View", font=('Consolas', 14, 'bold'), text_color='#2D2D2D')
        label.pack(padx=5, pady=5)

        inner_frame = ctk.CTkFrame(self, width=300, height=200, fg_color='#F0F0F0')
        inner_frame.pack(padx=5, pady=5)
