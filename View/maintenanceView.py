import customtkinter as ctk

class maintenanceView(ctk.CTkFrame):

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
        self.maintenanceBaseFrame = ctk.CTkFrame(self, width=842, height=620, fg_color='#DFDFDF', corner_radius=0)
        self.maintenanceBaseFrame.place(x=0, y=0)
        
        self.place(x=0, y=0) # Place productView Frame, do not change this

        self.show_maintenanceFrame()
            
    def show_maintenanceFrame(self):
        self.maintenanceFrame = ctk.CTkFrame(self.maintenanceBaseFrame, width=820, height=581, fg_color='#F7F7F7', corner_radius=7)
        self.maintenanceFrame.place(x=12, y=15)
        
        self.label = ctk.CTkLabel(self.maintenanceFrame, text="Tab Placeholder", font=('Inter', 13, 'bold'))
        self.label.place(x=14, y=7)
    


class App:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Maintenance Page (Test)")
        
        self.product_view = maintenanceView(self.root, None)
        self.product_view.pack(fill=ctk.BOTH, expand=True)
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()