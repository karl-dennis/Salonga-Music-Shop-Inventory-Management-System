import customtkinter as ctk


class productView(ctk.CTkFrame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(width=842, height=620, fg_color='#DFDFDF', corner_radius=0)
        ctk.set_appearance_mode("light")
        
        self.custom_styles()
        self.base_frame()

    def custom_styles(self):
        pass

    def base_frame(self):
        self.productFrame = ctk.CTkFrame(self, width=842, height=620, fg_color='#DFDFDF', corner_radius=0)
        self.productFrame.place(x=0, y=0)
        
        self.label = ctk.CTkLabel(self.productFrame, text="Product View", font=('Consolas', 18, 'bold'))
        self.label.place(x=20, y=20)
        self.place(x=0, y=0) # Place productView Frame
        
    def show_productReg(self):
        pass