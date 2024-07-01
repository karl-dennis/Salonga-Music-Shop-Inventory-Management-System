import sqlite3
import customtkinter as ctk
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class graphSalesView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color='transparent', corner_radius=7)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        # Add your widgets here
        self.inner_frame = ctk.CTkFrame(self, width=432, height=280, fg_color='#F7F7F7')
        self.inner_frame.pack_propagate(0)
        self.inner_frame.pack(fill='both', expand=True)

        self.plot(self.inner_frame)

        label = ctk.CTkLabel(self.inner_frame, text="Sales Graph", font=('Inter Medium', 12), text_color='#2E2E2E')
        label.place(relx=0.03, rely=0.05)

        view_all = ctk.CTkButton(self.inner_frame, text="View All", font=("Inter Medium", 12, 'underline'),
                                 text_color="#2E8EC4", fg_color='transparent', hover_color='#F7F7F7')
        view_all.place(relx=0.85, rely=0.03)

    def plot(self, inner_frame):
        conn = sqlite3.connect('salonga_music_shop.db')
        query = '''
            SELECT date, SUM(revenue) as total_revenue
            FROM transactions
            GROUP BY date
            ORDER BY date
        '''
        # Execute the query and store the result in a DataFrame
        data = pd.read_sql_query(query, conn)
        conn.close()

        # Set the Seaborn style and palette
        sns.set(style="whitegrid", palette="tab10")

        fig, ax = plt.subplots()
        fig.set_facecolor("#F7F7F7")
        ax.set_facecolor("#F7F7F7")

        # Plot the line chart
        sns.lineplot(data=data, x='date', y='total_revenue', marker='o', ax=ax)

        # Customize the plot
        ax.set_title('Daily Revenue')
        ax.set_xlabel('Date')
        ax.set_ylabel('Total Revenue')
        ax.grid(True, color='white')

        # Display the plot in a Tkinter canvas
        canvas = FigureCanvasTkAgg(fig, master=inner_frame)
        canvas.draw()
        # Set the plot size to be slightly smaller than the frame
        canvas.get_tk_widget().place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)