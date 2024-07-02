import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import customtkinter as ctk
import sqlite3
import pandas as pd
import seaborn as sns

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

    def plot(self, inner_frame):
        conn = sqlite3.connect('salonga_music_shop.db')

        query = "SELECT product_type, product_quantity FROM products"
        df = pd.read_sql_query(query, conn)
        conn.close()

        data = df.groupby('product_type').sum().reset_index()

        fig, ax = plt.subplots(figsize=(5, 3.5))

        sns.set_theme(style="whitegrid")

        sns.barplot(x='product_quantity', y='product_type', data=data, palette="viridis", ax=ax)

        ax.set_title('Stocks by Category', fontsize=14)
        ax.set_xlabel('Stocks', fontsize=14)
        # ax.set_ylabel('Categories', fontsize=12)
        ax.set_ylabel('')

        fig.set_facecolor("#F7F7F7")
        ax.set_facecolor("#F7F7F7")
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        ax.tick_params(axis='y', labelsize=11,  direction='out')
        plt.subplots_adjust(left=0.18, bottom=0.15, right=0.95)

        canvas = FigureCanvasTkAgg(fig, master=inner_frame)
        canvas.draw()
        canvas.get_tk_widget().place(x=0, y=10, width=650, height=350)
        
        
if __name__ == "__main__":   
    root = ctk.CTk()
    root.geometry("520x292")
    ctk.set_appearance_mode('light')

    inventory_view = inventoryView(root, None)
    inventory_view.pack(expand=True, fill='both')

    root.mainloop()