import customtkinter as ctk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class inventoryView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, 
                        #  width=428, height=352, 
                         fg_color='#FFF', corner_radius=0)
        self.controller = controller
        self.create_widgets()
        self.plot()
        
    def create_widgets(self):
        # Add your widgets here
        inner_frame = ctk.CTkFrame(self, width=387, height=231, fg_color='#F7F7F7')
        inner_frame.pack_propagate(0)
        inner_frame.pack()
        
        label = ctk.CTkLabel(inner_frame, text="Stock Graph", font=('Consolas', 14, 'bold'), text_color='#2D2D2D')
        label.pack(padx=20, pady=20)

    def plot(self):
        # generate random numbers for the plot
        x,y,s,c = np.random.rand(4,100)

        # generate the figure and plot object which will be linked to the root element
        fig, ax = plt.subplots()
        fig.set_size_inches(3,2)
        ax.scatter(x,y,s*50,c)
        ax.axis("off")
        fig.subplots_adjust(left=0, right=1, bottom=0, top=1, wspace=0, hspace=0)
        canvas = FigureCanvasTkAgg(fig, self)
        canvas.draw()
        canvas.get_tk_widget().place(x=140, y=100)