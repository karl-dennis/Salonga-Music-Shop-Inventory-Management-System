import customtkinter as ctk
from PIL import Image

class statisticView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, 
                        #  width=400, height=352, 
                        fg_color='transparent', corner_radius=7)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        # Add your widgets here
        inner_frame = ctk.CTkFrame(self, width=268, height=75, fg_color='#F7F7F7')
        inner_frame.pack_propagate(0)
        inner_frame.pack()
        
        label = ctk.CTkLabel(inner_frame, text="Revenue (May 2024)", font=('Inter', 17, 'bold'), text_color='#5089B5')
        label.place(x=0, y=0)
        
        label = ctk.CTkLabel(inner_frame, text="₱18,049", font=('Inter Medium', 16), text_color='#5089B5', bg_color='transparent')
        label.place(x=0, y=0)

        icon = ctk.CTkImage(light_image=Image.open("./assets/revenue.png"),
                            size=(40,40))
        my_icon = ctk.CTkLabel(inner_frame, text="", image=icon)
        my_icon.place(x=0, y=0)