import customtkinter as ctk
from PIL import Image
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import messagebox
from CTkTable import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import io

class productView(ctk.CTkFrame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.name_entry = tk.StringVar()
        self.quantity = tk.StringVar()
        self.price = tk.StringVar()
        self.search_query = tk.StringVar()
        self.image_data = None

        self.configure(width=842, height=620, fg_color='#DFDFDF', corner_radius=0)
        ctk.set_appearance_mode("light")
        
        self.importIcon = ctk.CTkImage(light_image=Image.open('./assets/import.png'), size=(80,73))

        self.custom_styles()
        self.base_frame()

    def custom_styles(self):
        pass

    def base_frame(self):
        self.productFrame = ctk.CTkFrame(self, width=842, height=620, fg_color='#DFDFDF', corner_radius=0)
        self.productFrame.place(x=0, y=0)
        
        self.place(x=0, y=0) # Place productView Frame, do not change this
        
        self.show_productReg()
        self.show_productGraph()
        self.show_reports()
        self.show_productTable()
        self.search_bar()
        
        self.productFrame.bind('<Button-1>', lambda event: self.productFrame.focus_set())
        self.productTableFrame.bind('<Button-1>', lambda event: self.productTableFrame.focus_set())
        self.productRegFrame.bind('<Button-1>', lambda event: self.productRegFrame.focus_set())
        self.productGraphFrame.bind('<Button-1>', lambda event: self.productGraphFrame.focus_set())
        self.reportsFrame.bind('<Button-1>', lambda event: self.reportsFrame.focus_set())
        
    def show_productReg(self):
        self.icon = ctk.CTkImage(light_image=Image.open('./assets/plus.png'), size=(15,15)) # Icon implementation
        
        self.productRegFrame = ctk.CTkFrame(self.productFrame, width=209, height=594, fg_color='#F7F7F7', corner_radius=7)
        self.productRegFrame.place(x=12, y=10)
        
        self.imageFrame = ctk.CTkFrame(self.productRegFrame, width=128, height=128, fg_color='transparent')
        self.imageFrame.place(x=40, y=44)
        
        self.imageButton = ctk.CTkButton(self.imageFrame, image=self.importIcon, text='', width=128, height=128,
                                         border_width=2.5, border_color='#B8B8B8', corner_radius=7,
                                         fg_color='#FFFFFF', bg_color='#F7F7F7',
                                         hover_color='#FFFFFF', command=self.select_image,
                                         anchor='center')
        self.imageButton.place(x=0, y=0)
        
        self.nameFrame = ctk.CTkFrame(self.productRegFrame, width=160, height=56, fg_color='transparent')
        self.nameFrame.place(x=24, y=186)
        
        self.nameLabel = ctk.CTkLabel(self.nameFrame, text='Product Name', font=('Inter Medium', 12), text_color='#595959',
                                       width=106, height=26, bg_color='transparent', anchor='w')
        self.nameLabel.place(x=5, y=0)
        
        self.nameEntry = ctk.CTkEntry(self.nameFrame, width=160, height=30, corner_radius=7, 
                                       bg_color='transparent', fg_color='#FAFAFA',
                                       border_color='#CACACA', border_width=2,
                                       font=('Inter Medium', 12), text_color='#595959', textvariable=self.name_entry)
        self.nameEntry.place(x=0, y=26)

        self.brandFrame = ctk.CTkFrame(self.productRegFrame, width=160, height=56, fg_color='transparent')
        self.brandFrame.place(x=24, y=250)
        
        self.brandButton = ctk.CTkButton(self.brandFrame, image=self.icon, text='', width=15, height=15, 
                                        fg_color='transparent', hover_color='#F7F7F7', anchor='center', command=self.brand_button_clicked)
        self.brandButton.place(x=36, y=1)
        
        self.brandLabel = ctk.CTkLabel(self.brandFrame, text='Brand', font=('Inter Medium', 12), text_color='#595959',
                                          width=34, height=26, bg_color='transparent', anchor='w')
        self.brandLabel.place(x=5, y=0)
        
        self.brandDropdown = ctk.CTkComboBox(self.brandFrame, 
                                            values=self.controller.get_brand(), # Insert values here
                                            width=160, height=30, corner_radius=7,
                                            bg_color='transparent', fg_color='#FAFAFA',
                                            border_color='#CACACA', border_width=2, state='readonly', 
                                            font=('Inter Medium', 12), text_color='#595959',
                                            dropdown_font=('Inter Medium', 12), dropdown_text_color='#595959', 
                                            dropdown_fg_color='#FAFAFA', dropdown_hover_color='#e4e4e4',
                                            button_color='#CACACA',)
        self.brandDropdown.set('Select')
        self.brandDropdown.place(x=0, y=26)
        
        self.typeFrame = ctk.CTkFrame(self.productRegFrame, width=160, height=56, fg_color='transparent')
        self.typeFrame.place(x=24, y=314)
                
        self.typeButton = ctk.CTkButton(self.typeFrame, image=self.icon, text='', width=15, height=15, 
                                        fg_color='transparent', hover_color='#F7F7F7', anchor='center', command=self.type_button_clicked)
        self.typeButton.place(x=80, y=1)
        
        self.typeLabel = ctk.CTkLabel(self.typeFrame, text='Product Type', font=('Inter Medium', 12), text_color='#595959',
                                          width=80, height=26, bg_color='transparent', anchor='w')
        self.typeLabel.place(x=5, y=0)
        
        self.typeDropdown = ctk.CTkComboBox(self.typeFrame, 
                                            values=self.controller.get_type(), # Insert values here
                                            width=160, height=30, corner_radius=7,
                                            bg_color='transparent', fg_color='#FAFAFA',
                                            border_color='#CACACA', border_width=2, state='readonly', 
                                            font=('Inter Medium', 12), text_color='#595959',
                                            dropdown_font=('Inter Medium', 12), dropdown_text_color='#595959', 
                                            dropdown_fg_color='#FAFAFA', dropdown_hover_color='#e4e4e4',
                                            button_color='#CACACA')
        self.typeDropdown.set('Select')
        self.typeDropdown.place(x=0, y=26)
        
        self.quantityFrame = ctk.CTkFrame(self.productRegFrame, width=160, height=56, fg_color='transparent')
        self.quantityFrame.place(x=24, y=378)
        
        self.quantityLabel = ctk.CTkLabel(self.quantityFrame, text='Initial Quantity', font=('Inter Medium', 12), text_color='#595959',
                                          width=106, height=26, bg_color='transparent', anchor='w')
        self.quantityLabel.place(x=5, y=0)
        
        self.quantityEntry = ctk.CTkEntry(self.quantityFrame, width=160, height=30, corner_radius=7, 
                                       bg_color='transparent', fg_color='#FAFAFA',
                                       border_color='#CACACA', border_width=2,
                                       font=('Inter Medium', 12), text_color='#595959', textvariable=self.quantity)
        self.quantityEntry.place(x=0, y=26)
        
        self.priceFrame = ctk.CTkFrame(self.productRegFrame, width=160, height=56, fg_color='transparent')
        self.priceFrame.place(x=24, y=442)
        
        self.priceLabel = ctk.CTkLabel(self.priceFrame, text='Price', font=('Inter Medium', 12), text_color='#595959',
                                       width=106, height=26, bg_color='transparent', anchor='w')
        self.priceLabel.place(x=5, y=0)
        
        self.priceEntry = ctk.CTkEntry(self.priceFrame, width=160, height=30, corner_radius=7, 
                                       bg_color='transparent', fg_color='#FAFAFA',
                                       border_color='#CACACA', border_width=2,
                                       font=('Inter Medium', 12), text_color='#595959', textvariable=self.price)
        self.priceEntry.place(x=0, y=26)
        
        self.buttonFrame = ctk.CTkFrame(self.productRegFrame, width=160, height=26, bg_color='transparent', fg_color='transparent')
        self.buttonFrame.place(x=24, y=532)    
        
        self.clearButton = ctk.CTkButton(self.buttonFrame, width=72, height=26, bg_color='transparent', 
                                         fg_color='#E2E2E2', hover_color='#D5D5D5', corner_radius=7,
                                         text='Clear', font=('Consolas', 12), text_color='#595959', 
                                         command=self.clear_form)
        self.clearButton.place(x=0, y=0)
        
        self.saveButton = ctk.CTkButton(self.buttonFrame, width=72, height=26,  bg_color='transparent',
                                        fg_color='#1FB2E7', hover_color='#2193BC', corner_radius=7,
                                        text='Save', font=('Consolas', 12), text_color='#F7F7F7', command=self.save_button_clicked
                                        )
        self.saveButton.place(x=88, y=0)
        
        self.label = ctk.CTkLabel(self.productRegFrame, text="Add Products", font=('Inter Medium', 13), text_color='#2E2E2E')
        self.label.place(x=14, y=7)
        
    def show_productGraph(self):
        self.productGraphFrame = ctk.CTkFrame(self.productFrame, width=382, height=232, fg_color='#F7F7F7', corner_radius=7)
        self.productGraphFrame.place(x=231, y=10)
        
        self.label = ctk.CTkLabel(self.productGraphFrame, text="Stock Graph", font=('Inter Medium', 13), text_color='#2E2E2E')
        self.label.place(x=14, y=7)

        self.innerFrame = ctk.CTkFrame(self.productGraphFrame, width=362, height=192, fg_color='#F7F7F7',
                                       corner_radius=5)
        self.innerFrame.place(x=10, y=35)

        # Call the plot method and pass the inner frame
        self.plot(self.innerFrame)

    def plot(self, inner_frame):
        categories = ['Brass', 'Woodwind', 'Percussion', 'String']
        stocks = [[10, 5, 5, 2], [15, 10, 5, 3], [10, 10, 5, 4], [20, 10, 5, 2]]  # Sublists represent subgroups of bars for each category

        fig = plt.figure(figsize=(4, 2.5))

        ax = fig.add_subplot(111)
        x = np.arange(len(categories))
        width = 0.1  # Width of each bar group

        # Plotting each subgroup of bars for each category
        for i, sublist in enumerate(stocks):
            ax.bar(x + width * i, sublist, width=width, label=f'Subgroup {i + 1}')

        fig.set_facecolor("#F7F7F7")
        ax.set_facecolor("#F7F7F7")
        ax.set_xlabel('Categories')
        ax.set_ylabel('Stocks')
        ax.set_title('Stocks by Category')
        ax.set_xticks(x + width * (len(stocks) - 1) / 2)
        ax.set_xticklabels(categories)
        ax.legend()

        canvas = FigureCanvasTkAgg(fig, master=inner_frame)
        canvas.draw()
        canvas.get_tk_widget().place(x=90, y=10)  # Adjust x and y to position the plot correctly within the inner frame

    def show_reports(self):
        self.reportsFrame = ctk.CTkFrame(self.productFrame, width=207, height=232, fg_color='#F7F7F7', corner_radius=7)
        self.reportsFrame.place(x=622, y=10)
        
        self.label = ctk.CTkLabel(self.reportsFrame, text="Reports", font=('Inter Medium', 13), text_color='#2E2E2E')
        self.label.place(x=14, y=7)
    
    def show_productTable(self):
        self.productTableFrame = ctk.CTkFrame(self.productFrame, width=598, height=352, fg_color='#F7F7F7',
                                              corner_radius=7)
        self.productTableFrame.place(x=231, y=252)

        self.label = ctk.CTkLabel(self.productTableFrame, text="Stock Levels", font=('Inter Medium', 13),
                                  text_color='#2E2E2E')
        self.label.place(x=14, y=7)

        table_values = self.controller.get_data()
        # print(self.controller.get_data())

        self.tableFrame = ctk.CTkFrame(self.productTableFrame, width=577, height=297, fg_color='#F7F7F7',
                                       corner_radius=0)
        self.tableFrame.place(x=12, y=55)
        
        column_titles = ["Product ID", "Product", "Type", "Brand", "Price", "Qty", "Status"]
        column_widths = [99, 101, 92, 87, 69, 60, 65]
        x_position = 0
        for column, (title, width) in enumerate(zip(column_titles, column_widths)):
            self.columnLabel = ctk.CTkLabel(
                self.productTableFrame, 
                width=column_widths[column], 
                height=25, 
                text=title, 
                fg_color='#F7F7F7',
                font=('Inter Semibold', 12),
                text_color='#9E9E9E',
                corner_radius=0, 
                anchor='w'
            )
            self.columnLabel.place(x=15+x_position, y=30)
            x_position += width
            
        self.columnLine = ctk.CTkFrame(self.productTableFrame, width=598, height=2, fg_color='#D2D2D2')
        self.columnLine.place(x=0, y=53)

        self.table = CTkTable(master=self.tableFrame, column=7, padx=0, pady=0, font=('Inter Medium', 12))
        if not table_values:
            required_rows = 0
        else:
            required_rows = len(table_values)
        
        current_rows = self.table.rows # Subtract 1 for the header row
        for _ in range(required_rows - current_rows):
            self.table.add_row([''] * 7)  # Add empty rows to meet the required row count

        # Inserting a Row
        for row, row_values in enumerate(table_values):
            for column, value in enumerate(row_values):
                # print(f"Inserting value '{value}' into row {row + 1}, column {column}")
                self.table.insert(row, column, value)

        cell_widths = [98, 96, 91, 86, 70, 60, 65]
        # Configuring the rest of the rows
        for row in range(0, self.table.rows):
            for column in range(self.table.columns): 
                self.table.frame[row, column].configure(width=cell_widths[column], height=25,
                                                        fg_color='#F7F7F7', text_color='#868686',
                                                        corner_radius=0, anchor='w')

            if table_values:
                quantity = int(table_values[row - 1][4])  # 5th Column = Quantity
                if quantity == 0:
                    status = "No Stock"
                    status_color = "#D92929"
                elif 1 <= quantity <= 5:
                    status = "Low Stock"
                    status_color = "#E9AC07"
                else:
                    status = "Available"
                    status_color = "#329932"

                self.table.insert(row, 6, status)
                self.table.frame[row, 6].configure(text_color=status_color) # Status color
                self.table.frame[row, 4].configure(text_color='#5e5e5e') # Quantity color
        
                self.rowLine = ctk.CTkFrame(self.productTableFrame, width=598, height=2, fg_color='#dbdbdb') # Row divider
                self.rowLine.place(x=0, y=78 + (row - 1) * 25)

        self.table.place(x=0, y=0)
          
    def search_bar(self):
        self.searchFrame = ctk.CTkFrame(self.productTableFrame, width=160, height=22, fg_color='transparent')
        self.searchFrame.place(x=430, y=8) 
        
        self.search_query.set('Search')
        
        self.searchEntry = ctk.CTkEntry(self.searchFrame, width=160, height=22,
                                        fg_color='#FAFAFA', border_color='#BCBCBC', 
                                        border_width=2, corner_radius=10, font=('Inter Medium', 11), 
                                        text_color='#959595', textvariable=self.search_query)
        self.searchEntry.place(x=0, y=0) 
        
        def on_entry_click(event):
            if self.searchEntry.get() == 'Search':
                self.searchEntry.delete(0, tk.END)  # Delete all the text in the entry

        def on_focus_out(event):
            if self.searchEntry.get() == '':
                self.search_query.set('Search')

        self.searchEntry.bind('<FocusIn>', on_entry_click)
        self.searchEntry.bind('<FocusOut>', on_focus_out)    
        
        def perform_search():
            query = self.search_query.get()
            if query.strip() != '':
                query = self.search_query.get()
                
                """Insert model/controller here"""
                
                print(f"Performing search for: {query}")
            
        self.searchEntry.bind('<Return>', lambda event: perform_search())

    def select_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])

        if file_path:
            selected_image = Image.open(file_path)
            img_width, img_height = 110, 110
            aspect_ratio = selected_image.width / selected_image.height

            if aspect_ratio > 1:
                # If width > height
                new_width = img_width
                new_height = int(img_width / aspect_ratio)
            else:
                # If width < height
                new_height = img_height
                new_width = int(img_height * aspect_ratio)

            resized_image = selected_image.resize((new_width, new_height))
            print(f"New image size: {new_width}x{new_height}")
            new_image = ctk.CTkImage(light_image=resized_image, size=(new_width, new_height))

            self.imageButton.configure(image=new_image)

            # Store the binary image data
            with io.BytesIO() as output:
                resized_image.save(output, format='PNG')
                self.image_data = output.getvalue()

            # Store the selected image reference
            self.selected_image = new_image
        else:
            # Defaults to import icon if none is selected
            self.imageButton.configure(image=self.importIcon)
    
    def clear_form(self):
        self.imageButton.configure(image=self.importIcon)
        self.nameEntry.delete(0, 'end')
        self.brandDropdown.set('Select')
        self.typeDropdown.set('Select')
        self.quantityEntry.delete(0, 'end')
        self.priceEntry.delete(0, 'end')

    def brand_button_clicked(self):
        # Function to handle brand input dialog
        brand_name = simpledialog.askstring("Enter Brand", "Enter the brand name:")
        self.controller.add_brand(brand_name)

        self.update_brand_dropdown()

    def update_brand_dropdown(self):
        brands = self.controller.get_brand()
        return self.brandDropdown.configure(values=brands)

    def type_button_clicked(self):
        type_name = simpledialog.askstring("Product Type", "Enter the Product Type:")
        self.controller.add_type(type_name)

        self.update_type_dropdown()

    def update_type_dropdown(self):
        product_type = self.controller.get_type()
        return self.typeDropdown.configure(values=product_type)
    def save_button_clicked(self):
        product_name = self.name_entry.get()
        type = self.typeDropdown.get()
        brand = self.brandDropdown.get()
        quantity = self.quantity.get()
        price = self.price.get()
        image = self.image_data
        self.controller.save_button_clicked(product_name,type,brand,quantity,price,image)
        messagebox.showinfo('Success', 'Product Added Successfully')
        self.clear_form()

        self.show_productTable()

# class App:
#     def __init__(self):
#         self.root = ctk.CTk()
#         self.root.title("Products Page (Test)")

#         self.product_view = productView(self.root, None)
#         self.product_view.pack(fill=ctk.BOTH, expand=True)

#     def run(self):
#         self.root.mainloop()

# if __name__ == "__main__":
#     app = App()
#     app.run()