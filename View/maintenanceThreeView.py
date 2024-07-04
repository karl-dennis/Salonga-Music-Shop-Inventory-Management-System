from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import customtkinter as ctk
from PIL import Image
import io
from tkinter import filedialog
from tkinter import messagebox
from CTkTable import *
import shutil
import os
import datetime

class maintenanceThreeView(ctk.CTkFrame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(width=842, height=620, fg_color='#DFDFDF', corner_radius=0)
        ctk.set_appearance_mode("light")

        self.active_tab = 3
        self.name_entry = ctk.StringVar()
        self.quantity = ctk.StringVar()
        self.price = ctk.StringVar()
        self.capital_price = ctk.StringVar()
        self.image_data = None
        self.search_query = ctk.StringVar()
        self.availability_var = ctk.StringVar()

        self.importIcon = ctk.CTkImage(light_image=Image.open('./assets/import.png'), size=(36, 33))

        self.custom_styles()
        self.base_frame()

    def custom_styles(self):
        pass

    def base_frame(self):
        self.baseFrame = ctk.CTkFrame(self, width=842, height=620, fg_color='#DFDFDF', corner_radius=0)
        self.baseFrame.place(x=0, y=0)

        self.place(x=0, y=0)  # Place productView Frame, do not change this

        self.show_maintenanceThree()
        self.show_productReg()
        self.show_productTable()
        
        generate_report_btn = ctk.CTkButton(self.baseFrame, text="Generate PDF Report",
                                            font=('Consolas', 12), text_color='#F7F7F7', bg_color='#F7F7F7',
                                            fg_color='#1FB2E7', hover_color='#2193BC', corner_radius=8,
                                            command=self.generate_pdf_report)
        generate_report_btn.place(x=247, y=570)

    def show_maintenanceThree(self):
        self.maintenanceThreeFrame = ctk.CTkFrame(self.baseFrame, width=820, height=51, fg_color='#F7F7F7',
                                                  corner_radius=7)
        self.maintenanceThreeFrame.place(x=11, y=15)

        self.tabFrame = ctk.CTkFrame(self.maintenanceThreeFrame, width=820, height=51, bg_color='#DFDFDF',
                                     fg_color='#F7F7F7', corner_radius=7)
        self.tabFrame.place(x=0, y=0)

        self.selection1 = ctk.CTkButton(self.tabFrame, width=115, height=18, text='Manage Users',
                                        font=('Inter', 13, 'bold'), text_color='#9A9A9A',
                                        fg_color='#F7F7F7', hover_color='#F7F7F7',
                                        command=lambda: self.controller.set_active_tab(1))
        self.selection1.place(x=9, y=14)

        self.selection2 = ctk.CTkButton(self.tabFrame, width=115, height=18, text='User Logs',
                                        font=('Inter', 13, 'bold'), text_color='#9A9A9A',
                                        fg_color='#F7F7F7', hover_color='#F7F7F7',
                                        command=lambda: self.controller.set_active_tab(2))
        self.selection2.place(x=140, y=14)

        self.selection3 = ctk.CTkButton(self.tabFrame, width=115, height=18, text='Manage Products',
                                        font=('Inter', 13, 'bold'), text_color='#2E2E2E',
                                        fg_color='#F7F7F7', hover_color='#F7F7F7')
        self.selection3.place(x=271, y=14)

        self.selection4 = ctk.CTkButton(self.tabFrame, width=115, height=18, text='Manage Sales',
                                        font=('Inter', 13, 'bold'), text_color='#9A9A9A',
                                        fg_color='#F7F7F7', hover_color='#F7F7F7',
                                        command=lambda: self.controller.set_active_tab(4))
        self.selection4.place(x=402, y=14)

        self.selection5 = ctk.CTkButton(self.tabFrame, width=115, height=18, text='Backup & Restore',
                                        font=('Inter', 13, 'bold'), text_color='#9A9A9A',
                                        fg_color='#F7F7F7', hover_color='#F7F7F7', command=self.show_systemDialog)
        self.selection5.place(x=533, y=14)

        self.system_dialog = None

        self.tabLine = ctk.CTkFrame(self.tabFrame, width=78, height=4, fg_color='#5089B5', corner_radius=7)
        self.tabLine.place(x=290, y=39)

    def show_productReg(self):
        self.productRegFrame = ctk.CTkFrame(self.baseFrame, width=210, height=526, fg_color='#F7F7F7', corner_radius=7)
        self.productRegFrame.place(x=12, y=79)

        self.label = ctk.CTkLabel(self.productRegFrame, width=174, height=16, text="Manage Products", font=('Inter Medium', 13), text_color='#2E2E2E', anchor='w')
        self.label.place(x=14, y=7)

        self.imageFrame = ctk.CTkFrame(self.productRegFrame, width=58, height=58, fg_color='transparent')
        self.imageFrame.place(x=76, y=27)

        self.imageButton = ctk.CTkButton(self.imageFrame, image=self.importIcon, text='', width=58, height=58,
                                         border_width=2.5, border_color='#B8B8B8', corner_radius=7,
                                         fg_color='#FFFFFF', bg_color='#F7F7F7',
                                         hover_color='#FFFFFF', command=self.select_image,
                                         anchor='center')
        self.imageButton.place(x=0, y=0)

        self.nameFrame = ctk.CTkFrame(self.productRegFrame, width=160, height=56, fg_color='transparent')
        self.nameFrame.place(x=25, y=85)

        self.nameLabel = ctk.CTkLabel(self.nameFrame, text='Product Name', font=('Inter Medium', 12), text_color='#595959',
                                       width=106, height=26, bg_color='transparent', anchor='w')
        self.nameLabel.place(x=5, y=0)

        self.nameEntry = ctk.CTkEntry(self.nameFrame, width=160, height=30, corner_radius=7,
                                       bg_color='transparent', fg_color='#FAFAFA',
                                       border_color='#CACACA', border_width=2,
                                       font=('Inter Medium', 12), text_color='#595959', textvariable=self.name_entry)

        self.nameEntry.place(x=0, y=26)

        self.brandFrame = ctk.CTkFrame(self.productRegFrame, width=160, height=56, fg_color='transparent')
        self.brandFrame.place(x=25, y=141)

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
        self.typeFrame.place(x=25, y=197)

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
        self.quantityFrame.place(x=25, y=253)

        self.quantityLabel = ctk.CTkLabel(self.quantityFrame, text='Initial Quantity', font=('Inter Medium', 12), text_color='#595959',
                                          width=106, height=26, bg_color='transparent', anchor='w')
        self.quantityLabel.place(x=5, y=0)

        self.quantityEntry = ctk.CTkEntry(self.quantityFrame, width=160, height=30, corner_radius=7,
                                       bg_color='transparent', fg_color='#FAFAFA',
                                       border_color='#CACACA', border_width=2,
                                       font=('Inter Medium', 12), text_color='#595959', textvariable=self.quantity)
        self.quantityEntry.place(x=0, y=26)

        self.sellingPriceFrame = ctk.CTkFrame(self.productRegFrame, width=160, height=56, fg_color='transparent')
        self.sellingPriceFrame.place(x=25, y=309)

        self.sellingPriceLabel = ctk.CTkLabel(self.sellingPriceFrame, text='Price', font=('Inter Medium', 12), text_color='#595959',
                                       width=106, height=26, bg_color='transparent', anchor='w')
        self.sellingPriceLabel.place(x=5, y=0)


        self.sellingPriceEntry = ctk.CTkEntry(self.sellingPriceFrame, width=160, height=30, corner_radius=7,
                                       bg_color='transparent', fg_color='#FAFAFA',
                                       border_color='#CACACA', border_width=2,
                                       font=('Inter Medium', 12), text_color='#595959', textvariable=self.price)
        self.sellingPriceEntry.place(x=0, y=26)

        self.capitalPriceFrame = ctk.CTkFrame(self.productRegFrame, width=160, height=56, fg_color='transparent')
        self.capitalPriceFrame.place(x=25, y=365)

        self.capitalPriceLabel = ctk.CTkLabel(self.capitalPriceFrame, text='Capital Price', font=('Inter Medium', 12), text_color='#595959',
                                       width=106, height=26, bg_color='transparent', anchor='w')
        self.capitalPriceLabel.place(x=5, y=0)


        self.capitalPriceEntry = ctk.CTkEntry(self.capitalPriceFrame, width=160, height=30, corner_radius=7,
                                       bg_color='transparent', fg_color='#FAFAFA',
                                       border_color='#CACACA', border_width=2,
                                       font=('Inter Medium', 12), text_color='#595959', textvariable=self.capital_price)
        self.capitalPriceEntry.place(x=0, y=26)

        self.availabilityFrame = ctk.CTkFrame(self.productRegFrame, width=160, height=56, fg_color='transparent')
        self.availabilityFrame.place(x=25, y=421)

        self.availabilityLabel = ctk.CTkLabel(self.availabilityFrame, text='Availability', font=('Inter Medium', 12), text_color='#595959',
                                          width=80, height=26, bg_color='transparent', anchor='w')
        self.availabilityLabel.place(x=5, y=0)

        self.availabilityDropdown = ctk.CTkComboBox(self.availabilityFrame,
                                            values=['For Sale', 'VOID'], # Insert values here
                                            width=160, height=30, corner_radius=7,
                                            bg_color='transparent', fg_color='#FAFAFA',
                                            border_color='#CACACA', border_width=2, state='readonly',
                                            font=('Inter Medium', 12), text_color='#595959',
                                            dropdown_font=('Inter Medium', 12), dropdown_text_color='#595959',
                                            dropdown_fg_color='#FAFAFA', dropdown_hover_color='#e4e4e4',
                                            button_color='#CACACA', variable=self.availability_var)
        self.availabilityDropdown.set('Select')
        self.availabilityDropdown.place(x=0, y=26)

        self.buttonFrame = ctk.CTkFrame(self.productRegFrame, width=160, height=28, bg_color='transparent', fg_color='transparent')
        self.buttonFrame.place(x=25, y=487)

        self.clearButton = ctk.CTkButton(self.buttonFrame, width=72, height=28, bg_color='transparent',
                                         fg_color='#E2E2E2', hover_color='#D5D5D5', corner_radius=7,
                                         text='Clear', font=('Consolas', 12), text_color='#595959',
                                         command=self.clear_form)
        self.clearButton.place(x=0, y=0)

        self.saveButton = ctk.CTkButton(self.buttonFrame, width=72, height=28,  bg_color='transparent',
                                        fg_color='#1FB2E7', hover_color='#2193BC', corner_radius=7,
                                        text='Save', font=('Consolas', 12), text_color='#F7F7F7', command=self.save_button_clicked
                                        )
        self.saveButton.place(x=88, y=0)

    def show_productTable(self):
        self.productTableFrame = ctk.CTkFrame(self.baseFrame, width=596, height=526, fg_color='#F7F7F7',
                                              corner_radius=7)
        self.productTableFrame.place(x=235, y=79)

        self.label = ctk.CTkLabel(self.productTableFrame, text="Stock Levels", font=('Inter Medium', 13),
                                  text_color='#2E2E2E')
        self.label.place(x=14, y=7)

        self.table_values = self.controller.get_data()
        self.reordered_table = []
        for row_values in self.table_values:

            reordered_row_values = [row_values[0], row_values[1], row_values[3], row_values[2], row_values[5], row_values[4], row_values[6]]
            self.reordered_table.append(reordered_row_values)

        # Placing column titles
        column_titles = ["Product ID", "Product", "Type", "Brand", "Price", "Qty", "Status"]
        column_widths = [98, 96, 91, 86, 70, 60, 65]

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

        self.tableFrame = ctk.CTkScrollableFrame(self.productTableFrame, width=566, height=297, fg_color='#F7F7F7', corner_radius=0)
        self.tableFrame.place(x=12, y=55)

        # Placing table rows
        self.table = CTkTable(master=self.tableFrame, column=7, padx=0, pady=0, font=('Inter Medium', 12))
        if not self.reordered_table:
            required_rows = 0
        else:
            required_rows = len(self.reordered_table)

        current_rows = self.table.rows  # Subtract 1 for the header row
        for _ in range(required_rows - current_rows):
            self.table.add_row([''] * 7)  # Add empty rows to meet the required row count

        string_limit = 14
        for row, row_values in enumerate(self.reordered_table):
            for column, value in enumerate(row_values):
                if column == 4:  # Price column
                    value = f'₱{value:,.2f}'.rstrip('0').rstrip('.')
                if isinstance(value, str) and len(value) > string_limit:
                    value = value[:string_limit] + "..."  # Truncate and add ellipsis
                self.table.insert(row, column, value)

        cell_widths = [98, 96, 91, 86, 70, 60, 65]
        for row in range(0, self.table.rows):
            for column in range(self.table.columns):

                self.table.frame[row, column].configure(width=cell_widths[column], height=25,
                                                        fg_color='#F7F7F7', text_color='#868686',
                                                        corner_radius=0, anchor='w')

            if self.reordered_table:
                quantity = int(self.reordered_table[row][5])  # Column[5] = Quantity
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
                self.table.frame[row, 6].configure(text_color=status_color)  # Status
                self.table.frame[row, 5].configure(text_color=status_color, font=('Inter', 12))  # Quantity

        self.table.pack(fill='both', expand=True)

        self.selected_row = None
        self.bind_cell_click_events()

        for row in range(1, self.table.rows):
            rowLine = ctk.CTkFrame(self.tableFrame, width=598, height=2, fg_color='#dbdbdb')
            rowLine.place(x=0, y=(row * 25) - 4)

    def bind_cell_click_events(self):
        for row_index in range(self.table.rows):
            for col_index in range(self.table.columns):
                self.table.frame[row_index, col_index].bind("<Button-1>",
                                                            lambda event, row=row_index: self.handle_cell_click(event, row))

    def handle_cell_click(self, event, index):
        if self.selected_row == index:
            self.deselect_row(index)
            self.selected_row = None
        else:
            if self.selected_row is not None:
                self.deselect_row(self.selected_row)

            self.select_row(index)
            self.selected_row = index

    def select_row(self, row):
        self.table.edit_row(row, fg_color='#EAEAEA')
        capital_price = self.controller.get_capital_price(self.reordered_table[row][0])
        availability = self.controller.get_availability(self.reordered_table[row][0])
        self.id = self.table_values[row][0]
        self.name_entry.set(value=self.reordered_table[row][1])
        self.capital_price.set(value=capital_price)
        self.quantity.set(value=self.reordered_table[row][5])
        self.price.set(value=self.reordered_table[row][4])
        self.availabilityDropdown.set(value=availability[0])
        self.brandDropdown.set(value=self.reordered_table[row][3])
        self.typeDropdown.set(value=self.reordered_table[row][2])
        image = self.controller.get_product_image(self.reordered_table[row][0])
        imageblob = image[0]
        if imageblob:
            product_image = Image.open(io.BytesIO(imageblob))
            # product_image.thumbnail((66, 66))
            # product_image = ImageTk.PhotoImage(product_image)
            img_width, img_height = 45, 45
            aspect_ratio = product_image.width / product_image.height

            if aspect_ratio > 1:
                new_width = img_width
                new_height = int(img_width / aspect_ratio)
            else:
                new_height = img_height
                new_width = int(img_height * aspect_ratio)

            resized_image = product_image.resize((new_width, new_height))
            product_image = ctk.CTkImage(light_image=product_image, size=(new_width, new_height))

            self.imageButton = ctk.CTkButton(self.imageFrame, image=product_image, text='', width=58, height=58,
                                             border_width=2.5, border_color='#B8B8B8', corner_radius=7,
                                             fg_color='#FFFFFF', bg_color='#F7F7F7',
                                             hover_color='#FFFFFF', command=self.select_image,
                                             anchor='center')

        else:
            self.imageButton.configure(image=self.importIcon)


        self.imageButton.grid(row=0, column=0)
        self.imageButton.grid_propagate(0)

    def deselect_row(self, row):
        self.table.edit_row(row, fg_color='#F7F7F7')
        self.name_entry.set(value='')
        self.capital_price.set(value='')
        self.quantity.set(value='')
        self.price.set(value='')
        self.brandDropdown.set(value='Select')
        self.typeDropdown.set(value='Select')
        self.imageButton.configure(image=self.importIcon)
        self.availabilityDropdown.set(value='Select')


    def select_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])

        if file_path:
            selected_image = Image.open(file_path)
            img_width, img_height = 30, 30
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
        self.availabilityDropdown.set('Select')
        self.quantityEntry.delete(0, 'end')
        self.sellingPriceEntry.delete(0, 'end')
        self.capitalPriceEntry.delete(0, 'end')

    def save_button_clicked(self):
        if self.selected_row is not None:
            id = self.id
            name = self.name_entry.get()
            quantity = self.quantity.get()
            selling_price = self.price.get()
            capital_price = self.capital_price.get()
            # capital_price_list = list(capital_price)
            # print(id, name, quantity, selling_price, capital_price)
            availability = self.availability_var.get()

            self.clear_form()
            self.deselect_row(self.selected_row)

            self.controller.update_product(id, name, quantity, selling_price, capital_price, availability)
            self.show_productTable()
        else:
            product_name = self.name_entry.get()
            type = self.typeDropdown.get()
            brand = self.brandDropdown.get()
            quantity = self.quantity.get()
            price = self.price.get()
            image = self.image_data
            self.controller.save_button_clicked(product_name, type, brand, quantity, price, image)
            messagebox.showinfo('Success', 'Product Added Successfully')
            self.clear_form()

            self.show_productTable()

    def clear_base_frame(self):
        for widget in self.baseFrame.winfo_children():
            widget.destroy()

    def show_systemDialog(self):
        if self.system_dialog is None:
            self.system_dialog = SystemDialog(self)
            self.system_dialog.grab_set()  # Make the SystemDialog modal
            self.system_dialog.protocol("WM_DELETE_WINDOW", self.on_systemDialog_close)
            self.wait_window(self.system_dialog)
            
    def on_systemDialog_close(self):
        self.system_dialog.destroy()
        self.system_dialog = None

    def generate_pdf_report(self):
        # Ask user to select a directory
        directory = filedialog.askdirectory(title="Select Directory to Save PDF Report")
        if not directory:
            return

        # Define a fixed file name with timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        pdf_file = os.path.join(directory, f'stock_report_{timestamp}.pdf')

        # Generate PDF using ReportLab
        c = canvas.Canvas(pdf_file, pagesize=letter)
        width, height = letter

        # Store information
        store_name = "Salonga Music Shop"
        store_address = "#674 Gonzalo Puyat St., Quiapo, Manila"
        store_contact = "Telephone: 2955991, Cellphone: 0910-500-5096"

        # Header: Store name, address, and contact (centered)
        c.setFont("Helvetica-Bold", 16)
        store_name_width = c.stringWidth(store_name, "Helvetica-Bold", 16)
        store_name_x = (width - store_name_width) / 2
        c.drawString(store_name_x, height - 50, store_name)

        c.setFont("Helvetica", 10)
        store_address_width = c.stringWidth(store_address, "Helvetica", 10)
        store_address_x = (width - store_address_width) / 2
        c.drawString(store_address_x, height - 70, store_address)

        store_contact_width = c.stringWidth(store_contact, "Helvetica", 10)
        store_contact_x = (width - store_contact_width) / 2
        c.drawString(store_contact_x, height - 90, store_contact)

        # Title: Stock Report and timestamp (centered)
        c.setFont("Helvetica-Bold", 16)
        report_title = "Stock Report"
        report_title_width = c.stringWidth(report_title, "Helvetica-Bold", 16)
        report_title_x = (width - report_title_width) / 2
        c.drawString(report_title_x, height - 120, report_title)
        c.setFont("Helvetica", 10)

        # Set up table headers (left-aligned)
        headers = ['Product ID', 'Product Name', 'Type', 'Brand', 'Price', 'Quantity', 'Status']
        col_widths = [70, 115, 90, 85, 60, 60, 70]  # Adjust widths as needed
        row_height = 20
        y_start = height - 150

        # Draw table headers
        c.setFont("Helvetica-Bold", 12)
        for i, header in enumerate(headers):
            header_x = 36 + sum(col_widths[:i])  # Left-aligned position
            c.drawString(header_x, y_start, header)

        # Fetch and process data
        data = self.controller.get_processed_data()

        # Draw data rows (left-aligned)
        c.setFont("Helvetica", 12)
        y = y_start - row_height
        for row_values in data:
            for i, value in enumerate(row_values):
                if i == 1:  # Shorten product name if too long
                    value = value[:25] + '...' if len(value) > 28 else value
                elif i == 4:  # Format price column (was quantity)
                    value = f'{value:,.2f}'  # Assuming price is in Philippine Peso
                value_x = 36 + sum(col_widths[:i])  # Left-aligned position
                c.drawString(value_x, y, str(value))
            y -= row_height

        # Footer: Generated on (left-aligned)
        generated_on_text = f"Generated on: {datetime.datetime.now().strftime('%B %d, %Y %H:%M:%S')}"
        c.drawString(36, 36, generated_on_text)

        # Save the PDF file
        c.save()

        # Show message box confirming report generation
        messagebox.showinfo('Report Generated', f'Stock report has been generated as {pdf_file}')


class SystemDialog(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("370x220")
        self.title("Backup & Restore")
        self.configure(fg_color='#EBEBEB')
        self.resizable(False, False)        
        ctk.set_appearance_mode("light")
        self.center_window()
        self.transient()
        self.grab_set()
        
        backupFrame = ctk.CTkFrame(self, width=120, height=148, fg_color='transparent')
        backupFrame.place(x=36, y=33)
        
        backup_icon = ctk.CTkImage(light_image=Image.open('./assets/backup.png'), size=(102, 79))
        backupButton = ctk.CTkButton(backupFrame, image=backup_icon, text='', width=110, height=110,
                                     border_width=3, border_color='#B5B5B5', fg_color='#E2E2E2', corner_radius=7,
                                     hover_color='#E2E2E2', anchor='center', bg_color='#EBEBEB',
                                     command=self.backup_database)
        backupButton.place(x=0, y=0)
        
        backupLabel = ctk.CTkLabel(backupFrame, width=120, height=32, 
                                   text="Create a secure backup\nof your data.",
                                   font=('Inter Medium', 10), text_color='#696969')
        backupLabel.place(x=0, y=116)
        
        restoreFrame = ctk.CTkFrame(self, width=120, height=148, fg_color='transparent')
        restoreFrame.place(x=213, y=33)
        
        restore_icon = ctk.CTkImage(light_image=Image.open('./assets/restore.png'), size=(102, 79))
        restoreButton = ctk.CTkButton(restoreFrame, image=restore_icon, text='', width=110, height=110,
                                     border_width=3, border_color='#0792C5', fg_color='#1FB2E7', corner_radius=7,
                                     hover_color='#1FB2E7', anchor='center', bg_color='#EBEBEB',
                                     command=self.restore_database)
        restoreButton.place(x=0, y=0)
        
        restoreLabel = ctk.CTkLabel(restoreFrame, width=120, height=32, 
                                   text="Restore your data from\na previous backup.",
                                   font=('Inter Medium', 10), text_color='#0792C5')
        restoreLabel.place(x=0, y=116)
    
    def backup_database(self):
        database_path = './salonga_music_shop.db'
        backup_folder = filedialog.askdirectory(title='Select Backup Folder')

        if not backup_folder:
            return

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        backup_file = os.path.join(backup_folder, f'backup_{timestamp}.db')

        try:
            shutil.copy(database_path, backup_file)
            print(f"Database backed up successfully to {backup_file}")
        except Exception as e:
            print(f"Error during backup: {str(e)}")
    
    def restore_database(self):
        # Example: Database file path (adjust according to your actual path)
        database_path = './salonga_music_shop.db'

        # Prompt the user to choose a backup file
        backup_file = filedialog.askopenfilename(title='Select Backup File', filetypes=[('Database files', '*.db')])

        if not backup_file:
            # User canceled the dialog
            return

        try:
            # Perform the restore by copying the backup file to the database path
            shutil.copy(backup_file, database_path)
            print(f"Database restored successfully from {backup_file}")
        except Exception as e:
            print(f"Error during restore: {str(e)}")
            
    def center_window(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{370}x{220}+{x}+{y}')
       
class App:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Maintenance Three Page (Test)")

        self.maintenancethree_view = maintenanceThreeView(self.root, None)
        self.maintenancethree_view.pack(fill=ctk.BOTH, expand=True)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()