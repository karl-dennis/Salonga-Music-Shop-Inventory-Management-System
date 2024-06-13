import customtkinter as ctk

class statisticView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, 
                        #  width=400, height=352, 
                         fg_color='#FFF', corner_radius=0)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        # Add your widgets here
        inner_frame = ctk.CTkFrame(self, width=210, height=88, fg_color='#F7F7F7')
        inner_frame.pack_propagate(0)
        inner_frame.pack()
        
        label = ctk.CTkLabel(inner_frame, text="Total Revenue", font=('Consolas', 14, 'bold'), text_color='#2D2D2D')
        label.pack(padx=5, pady=5)

        