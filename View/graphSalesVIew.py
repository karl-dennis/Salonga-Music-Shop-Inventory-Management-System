import customtkinter as ctk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class graphSalesView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, 
                        #  width=400, height=352, 
                         fg_color='#FFF', corner_radius=0)
        self.controller = controller
        self.create_widgets()
        self.plot()
        
    def create_widgets(self):
        # Add your widgets here
        inner_frame = ctk.CTkFrame(self, width=387, height=193, fg_color='#F7F7F7')
        inner_frame.pack_propagate(0)
        inner_frame.pack()
        
        label = ctk.CTkLabel(inner_frame, text="Sales Graph", font=('Consolas', 14, 'bold'), text_color='#2D2D2D')
        label.pack(padx=20, pady=20)

    def plot(self):
        categories = ['A', 'B', 'C', 'D', 'E']
        values = [23, 45, 56, 78, 33]

        # Create horizontal bar graph
        fig = Figure(figsize=(4.7, 2.3))
        ax = fig.add_subplot(111)
        ax.barh(categories, values, color='skyblue')

        # Remove gridlines
        ax.grid(False)

        # Add labels and title
        ax.set_xlabel('Values')
        ax.set_ylabel('Categories')
        ax.set_title('Horizontal Bar Graph')

        # Embed the plot into tkinter window
        canvas = FigureCanvasTkAgg(fig, self)
        canvas.draw()
        canvas.get_tk_widget().place(x=0, y=0)
        