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
        
        self.place(x=0, y=0) # Place productView Frame, do not change this
        
        self.show_productReg()
        self.show_productGraph()
        self.show_reports()
        self.show_productTable()
        
    def show_productReg(self):
        self.productRegFrame = ctk.CTkFrame(self.productFrame, width=209, height=594, fg_color='#F7F7F7', corner_radius=7)
        self.productRegFrame.place(x=12, y=10)
        
        
        
        self.label = ctk.CTkLabel(self.productRegFrame, text="Add Products", font=('Inter Medium', 13))
        self.label.place(x=14, y=7)
    
    def show_productGraph(self):
        self.productGraphFrame = ctk.CTkFrame(self.productFrame, width=382, height=232, fg_color='#F7F7F7', corner_radius=7)
        self.productGraphFrame.place(x=231, y=10)
        
        self.label = ctk.CTkLabel(self.productGraphFrame, text="Stock Graph", font=('Inter Medium', 13))
        self.label.place(x=14, y=7)
    
    def show_reports(self):
        self.reportsFrame = ctk.CTkFrame(self.productFrame, width=207, height=232, fg_color='#F7F7F7', corner_radius=7)
        self.reportsFrame.place(x=622, y=10)
        
        self.label = ctk.CTkLabel(self.reportsFrame, text="Reports", font=('Inter Medium', 13))
        self.label.place(x=14, y=7)
    
    def show_productTable(self):
        self.productTableFrame = ctk.CTkFrame(self.productFrame, width=598, height=352, fg_color='#F7F7F7', corner_radius=7)
        self.productTableFrame.place(x=231, y=252)
        
        self.label = ctk.CTkLabel(self.productTableFrame, text="Stock Levels", font=('Inter Medium', 13))
        self.label.place(x=14, y=7)


class App:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Products Page (Test)")
        
        self.product_view = productView(self.root, None)
        self.product_view.pack(fill=ctk.BOTH, expand=True)
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()