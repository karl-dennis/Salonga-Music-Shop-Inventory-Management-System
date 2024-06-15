import customtkinter as ctk

class deliveryView(ctk.CTkFrame):

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
        self.deliveryBaseFrame = ctk.CTkFrame(self, width=842, height=620, fg_color='#DFDFDF', corner_radius=0)
        self.deliveryBaseFrame.place(x=0, y=0)
        
        self.place(x=0, y=0) # Place productView Frame, do not change this

        self.show_deliveryFrame()
        self.show_orderFrame()
            
    def show_deliveryFrame(self):
        self.deliveryFrame = ctk.CTkFrame(self.deliveryBaseFrame, width=522, height=583, fg_color='#F7F7F7', corner_radius=7)
        self.deliveryFrame.place(x=12, y=15)
        
        self.label = ctk.CTkLabel(self.deliveryFrame, text="Tab Placeholder", font=('Inter', 13, 'bold'))
        self.label.place(x=14, y=7)
    
    def show_orderFrame(self):
        self.orderFrame = ctk.CTkFrame(self.deliveryBaseFrame, width=285, height=583, fg_color='#F7F7F7', corner_radius=7)
        self.orderFrame.place(x=546, y=15)
        
        self.label = ctk.CTkLabel(self.orderFrame, text="Order #0001", font=('Inter', 15, 'bold'), text_color='#2E2E2E')
        self.label.place(x=95, y=12)


class App:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Delivery Page (Test)")
        
        self.product_view = deliveryView(self.root, None)
        self.product_view.pack(fill=ctk.BOTH, expand=True)
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()