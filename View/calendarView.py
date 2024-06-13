import customtkinter as ctk
from CTkDataVisualizingWidgets import CTkCalendar


class calendarView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color='#FFF', corner_radius=0)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        # Add your widgets here
        inner_frame = ctk.CTkFrame(self, width=190, height=110, fg_color='#F7F7F7')
        inner_frame.pack_propagate(0)
        inner_frame.pack(padx=10, pady=10)

        calendar_widget = CTkCalendar(inner_frame,  width=190, height=110)
        calendar_widget.pack(expand=True, fill="both")

