import customtkinter as ctk

class salesView(ctk.CTkFrame):

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
        self.salesFrame = ctk.CTkFrame(self, width=842, height=620, fg_color='#DFDFDF', corner_radius=0)
        self.salesFrame.place(x=0, y=0)
        
        self.place(x=0, y=0) # Place productView Frame, do not change this
        
        self.show_revenue()
        self.show_salesReg()
        self.show_salesGraph()
        self.show_reports()
        self.show_salesTable()
    
    def show_revenue(self):
        from PIL import Image
        self.revenueFrame = ctk.CTkFrame(self.salesFrame, width=210, height=58, fg_color='#F7F7F7', 
                                         bg_color='transparent', border_width=3, border_color='#5089B5',
                                         corner_radius=7)
        self.revenueFrame.place(x=12, y=10)
        
        self.icon = ctk.CTkImage(light_image=Image.open("./assets/revenue.png"), size=(30,30))
        self.my_icon = ctk.CTkLabel(self.revenueFrame, text="", image=self.icon)
        self.my_icon.place(x=13, y=10)
        
        self.label = ctk.CTkLabel(self.revenueFrame, text="Revenue (May 2024)", font=('Inter', 13, 'bold'), 
                                  text_color='#5089B5', fg_color='transparent',
                                  width=145, height=15, anchor='w')
        self.label.place(x=50, y=13)
        
        self.label = ctk.CTkLabel(self.revenueFrame, text="₱18,049", font=('Inter Medium', 12), 
                                  text_color='#5089B5', fg_color='transparent', 
                                  width=130, height=12, anchor='w')
        self.label.place(x=50, y=26)
    
    def show_salesReg(self):
        self.salesRegFrame = ctk.CTkFrame(self.salesFrame, width=209, height=526, fg_color='#F7F7F7', corner_radius=7)
        self.salesRegFrame.place(x=12, y=79)
        
        self.label = ctk.CTkLabel(self.salesRegFrame, text="Record New Sale", font=('Inter Medium', 13))
        self.label.place(x=14, y=7)
    
    def show_salesGraph(self):
        self.salesGraphFrame = ctk.CTkFrame(self.salesFrame, width=382, height=232, fg_color='#F7F7F7', corner_radius=7)
        self.salesGraphFrame.place(x=231, y=10)
        
        self.label = ctk.CTkLabel(self.salesGraphFrame, text="Sales Graph", font=('Inter Medium', 13))
        self.label.place(x=14, y=7)
    
    def show_reports(self):
        self.reportsFrame = ctk.CTkFrame(self.salesFrame, width=207, height=232, fg_color='#F7F7F7', corner_radius=7)
        self.reportsFrame.place(x=622, y=10)
        
        self.label = ctk.CTkLabel(self.reportsFrame, text="Reports", font=('Inter Medium', 13))
        self.label.place(x=14, y=7)
    
    def show_salesTable(self):
        self.salesTableFrame = ctk.CTkFrame(self.salesFrame, width=598, height=352, fg_color='#F7F7F7', corner_radius=7)
        self.salesTableFrame.place(x=231, y=252)
        
        self.label = ctk.CTkLabel(self.salesTableFrame, text="Sales History", font=('Inter Medium', 13))
        self.label.place(x=14, y=7)


class App:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Sales Page (Test)")
        
        self.product_view = salesView(self.root, None)
        self.product_view.pack(fill=ctk.BOTH, expand=True)
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()