import customtkinter as ctk
import tkcalendar as tkc
from tkinter import ttk

class calendarView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color='transparent', corner_radius=7)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        inner_frame = ctk.CTkFrame(self, width=268, height=200, fg_color='#F7F7F7')
        inner_frame.pack_propagate(0)
        inner_frame.pack()

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("CalendarButton.TButton", relief="flat")
        
        self.calendar = tkc.Calendar(inner_frame, font=("Inter", 13),
                                     firstweekday='sunday', showweeknumbers=True,
                                     background='#F7F7F7', foreground='#393939',
                                     headersbackground='#92A3AA', headersforeground='#FFFFFF',
                                     selectbackground='#5089B5', selectforeground='#FFFFFF',
                                     normalbackground='#FFFFFF', normalforeground='#6D6D6D',
                                     weekendbackground='#FFFFFF', weekendforeground='#6D6D6D',
                                     othermonthbackground='#E6E6E6', othermonthforeground='#BFBFBF',
                                     othermonthwebackground='#E6E6E6', othermonthweforeground='#BFBFBF',
                                     bordercolor='#92A3AA', width=268, height=200,
                                     style="CalendarButton.TButton") 
        
        self.calendar.pack(fill="both", expand=True, padx=5, pady=5)
        self.calendar.bind("<<CalendarSelected>>", self.on_click)
        
    def on_click(self, event):
        selected_date = self.calendar.get_date()
        print("Selected date:", selected_date)