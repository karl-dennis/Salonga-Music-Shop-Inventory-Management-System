import customtkinter as ctk
from CTkDataVisualizingWidgets import *

class calendarView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, 
                        #  width=400, height=352, 
                         fg_color='transparent', corner_radius=7)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        # Add your widgets here
        inner_frame = ctk.CTkFrame(self, width=268, height=200, fg_color='#F7F7F7')
        inner_frame.pack_propagate(0)
        inner_frame.pack()

        calendar_widget = CTkCalendar(inner_frame, width=268, height=200)
        calendar_widget.pack(side="left", padx=20, pady=20)
        