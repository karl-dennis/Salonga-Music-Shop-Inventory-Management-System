import customtkinter as ctk
# from matplotlib.figure import Figure
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class graphSalesView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color='#FFF', corner_radius=0)
        self.controller = controller
        self.create_widgets()
        # self.plot()

    def create_widgets(self):
        # Add your widgets here
        self.inner_frame = ctk.CTkFrame(self, width=390, height=199, fg_color='#F7F7F7')
        self.inner_frame.pack_propagate(0)
        self.inner_frame.pack()

        label = ctk.CTkLabel(self.inner_frame, text="Sales Graph", font=('Consolas', 14, 'bold'), text_color='#2D2D2D')
        label.pack(padx=20, pady=20)


