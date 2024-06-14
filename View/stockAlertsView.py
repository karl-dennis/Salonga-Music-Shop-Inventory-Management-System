import customtkinter as ctk

class stockAlertsView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, 
                        #  width=400, height=352, 
                         fg_color='transparent', corner_radius=7)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        # Add your widgets here
        inner_frame = ctk.CTkFrame(self, width=360, height=280, fg_color='#F7F7F7')
        inner_frame.pack_propagate(0)
        inner_frame.pack()
        
        label = ctk.CTkLabel(inner_frame, text="Sales History", font=('Inter Medium', 12), text_color='#2E2E2E',
                             width=80, height=14)
        label.place(x=13, y=12)
        
        view_all = ctk.CTkButton(inner_frame, text="View All", font=("Inter Medium", 12, 'underline'), 
                                            text_color="#2E8EC4", fg_color='transparent', hover_color='#F7F7F7',
                                            width=60, height=14)
        view_all.place(x=290, y=9)