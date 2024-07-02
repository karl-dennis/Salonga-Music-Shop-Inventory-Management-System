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
        label.place(x=13, y=7)

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
        sns.set(style="whitegrid", palette="viridis")

        fig, ax = plt.subplots()
        fig.set_facecolor("#F7F7F7")
        ax.set_facecolor("#F7F7F7")
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        # Plotting with Seaborn
        sns.lineplot(data=data, x='date', y='total_revenue', marker='o', ax=ax)

        # Customize labels and title
        ax.set_title('Daily Revenue', fontsize=14)
        ax.set_xlabel('Date', fontsize=12)
        ax.set_ylabel('Total Revenue', fontsize=12)

        # Adjust grid appearance
        ax.grid(False, color='white')
        plt.subplots_adjust(left=0.18, top=0.85, bottom=0.18, right=0.95)


        # Adjust plot canvas within inner_frame
        canvas = FigureCanvasTkAgg(fig, master=inner_frame)
        canvas.draw()
        canvas.get_tk_widget().place(x=5, rely=0.05, relwidth=0.97, relheight=0.93)