import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class graphSalesView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, 
                        #  width=400, height=352, 
                         fg_color='transparent', corner_radius=7)
        self.controller = controller
        self.create_widgets()
        
    def create_widgets(self):
        # Add your widgets here
        inner_frame = ctk.CTkFrame(self, width=432, height=280, fg_color='#F7F7F7')
        inner_frame.pack_propagate(0)
        inner_frame.pack()
        
        self.plot(inner_frame)
        
        label = ctk.CTkLabel(inner_frame, text="Sales Graph", font=('Inter Medium', 12), text_color='#2E2E2E',
                             width=80, height=14)
        label.place(x=13, y=12)
        
        view_all = ctk.CTkButton(inner_frame, text="View All", font=("Inter Medium", 12, 'underline'), 
                                            text_color="#2E8EC4", fg_color='transparent', hover_color='#F7F7F7',
                                            width=60, height=14)
        view_all.place(x=362, y=9)
        
        

    def plot(self, inner_frame):
        categories = ['A', 'B', 'C', 'D', 'E']
        values = [23, 45, 56, 78, 33]

        fig, ax = plt.subplots(figsize=(3.5, 3.5))
        fig.set_facecolor("#F7F7F7")
        ax.set_facecolor("#F7F7F7")
        
        ax.pie(values, labels=categories, autopct='%1.1f%%', startangle=90, colors=plt.cm.tab20.colors)
        ax.axis('equal')
        ax.set_title('Donut Chart')
        
        center_circle = plt.Circle((0, 0), 0.7, color='white', fc='white', linewidth=1.25)
        ax.add_artist(center_circle)
        
        canvas = FigureCanvasTkAgg(fig, master=inner_frame)
        canvas.draw()
        canvas.get_tk_widget().place(x=80, y=20)
        