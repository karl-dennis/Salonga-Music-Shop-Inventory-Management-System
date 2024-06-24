import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import customtkinter as ctk

class inventoryView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color='transparent', corner_radius=7)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        inner_frame = ctk.CTkFrame(self, width=520, height=292, fg_color='#F7F7F7')
        inner_frame.pack_propagate(0)
        inner_frame.pack()

        self.plot(inner_frame)
        
        label = ctk.CTkLabel(inner_frame, text="Stock Graph", font=('Inter Medium', 12), text_color='#2E2E2E',
                             width=80, height=14)
        label.place(x=13, y=12)
        
        view_all = ctk.CTkButton(inner_frame, text="View All", font=("Inter Medium", 12, 'underline'), 
                                            text_color="#2E8EC4", fg_color='transparent', hover_color='#F7F7F7',
                                            width=60, height=14)
        view_all.place(x=450, y=9)

    def plot(self, inner_frame):
        categories = ['Brass', 'Woodwind', 'Percussion', 'String']
        stocks = [[10, 5, 5, 2], [15, 10, 5, 3], [10, 10, 5, 4], [20, 10, 5, 2]]  # Sublists represent subgroups of bars for each category

        fig = plt.figure(figsize=(5, 3.5))
        
        ax = fig.add_subplot(111)
        x = np.arange(len(categories))
        width = 0.2  # Width of each bar group

        # Plotting each subgroup of bars for each category
        for i, sublist in enumerate(stocks):
            ax.bar(x + width*i, sublist, width=width, label=f'Subgroup {i+1}')
            
        fig.set_facecolor("#F7F7F7")
        ax.set_facecolor("#F7F7F7")
        ax.set_xlabel('Categories')
        ax.set_ylabel('Stocks')
        ax.set_title('Stocks by Category')
        ax.set_xticks(x + width*(len(stocks)-1)/2)
        ax.set_xticklabels(categories)
        ax.legend()
        

        canvas = FigureCanvasTkAgg(fig, master=inner_frame)
        canvas.draw()
        canvas.get_tk_widget().place(x=90, y=10)
