import customtkinter as ctk
from PIL import Image
from datetime import datetime

class statisticView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, 
                         fg_color='transparent', bg_color='transparent', corner_radius=7)
        self.controller = controller
        self.total_revenue = 0
        self.create_widgets()

    def create_widgets(self):
        inner_frame = ctk.CTkFrame(self, width=268, height=75, fg_color='#F7F7F7', 
                                   bg_color='transparent', border_width=3, border_color='#5089B5', 
                                   corner_radius=7)
        inner_frame.pack_propagate(0)
        inner_frame.pack()
        
        icon = ctk.CTkImage(light_image=Image.open("./assets/revenue.png"),
                            size=(40,40))
        my_icon = ctk.CTkLabel(inner_frame, text="", image=icon)
        my_icon.place(x=19, y=15)
        
        current_month_year = datetime.now().strftime('%B %Y')  # Format: Month Year, e.g., May 2024
        
        self.label_title = ctk.CTkLabel(inner_frame, text=f"Revenue ({current_month_year})", font=('Inter', 17, 'bold'), text_color='#5089B5', fg_color='transparent')
        self.label_title.place(x=65, y=13)
        
        self.label_revenue = ctk.CTkLabel(inner_frame, text=f'₱{self.total_revenue:,.2f}', font=('Inter Medium', 15), text_color='#5089B5', fg_color='transparent', height=20)
        self.label_revenue.place(x=65, y=36)

        self.set_total_revenue(self.controller.model.fetch_revenue())

    def set_total_revenue(self, total_revenue):
        self.total_revenue = total_revenue
        self.label_revenue.configure(text=f'₱{self.total_revenue:,.2f}')
        print(self.total_revenue)  # Debugging print statement
