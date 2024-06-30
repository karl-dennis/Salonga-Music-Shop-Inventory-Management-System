import customtkinter as ctk
from PIL import Image
import io
from tkinter import filedialog
from tkinter import messagebox
from CTkTable import *


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
        self.image_data = None
        self.search_query = ctk.StringVar()

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

        self.selection4 = ctk.CTkButton(self.tabFrame, width=115, height=18, text='System',
                                        font=('Inter', 13, 'bold'), text_color='#9A9A9A',
                                        fg_color='#F7F7F7', hover_color='#F7F7F7',
                                        command=lambda: self.controller.set_active_tab(4))
        self.selection4.place(x=402, y=14)

        self.tabLine = ctk.CTkFrame(self.tabFrame, width=78, height=4, fg_color='#5089B5', corner_radius=7)
        self.tabLine.place(x=290, y=39)

    def show_productReg(self):
        self.productRegFrame = ctk.CTkFrame(self.baseFrame, width=210, height=526, fg_color='#F7F7F7', corner_radius=7)
        self.productRegFrame.place(x=12, y=79)

        self.label = ctk.CTkLabel(self.productRegFrame, width=174, height=16, text="Manage Products",
                                  font=('Inter Medium', 13), text_color='#2E2E2E', anchor='w')
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

        self.nameLabel = ctk.CTkLabel(self.nameFrame, text='Product Name', font=('Inter Medium', 12),
                                      text_color='#595959',
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
                                             values=self.controller.get_brand(),  # Insert values here
                                             width=160, height=30, corner_radius=7,
                                             bg_color='transparent', fg_color='#FAFAFA',
                                             border_color='#CACACA', border_width=2, state='readonly',
                                             font=('Inter Medium', 12), text_color='#595959',
                                             dropdown_font=('Inter Medium', 12), dropdown_text_color='#595959',
                                             dropdown_fg_color='#FAFAFA', dropdown_hover_color='#e4e4e4',
                                             button_color='#CACACA', )
        self.brandDropdown.set('Select')
        self.brandDropdown.place(x=0, y=26)

        self.typeFrame = ctk.CTkFrame(self.productRegFrame, width=160, height=56, fg_color='transparent')
        self.typeFrame.place(x=25, y=197)

        self.typeLabel = ctk.CTkLabel(self.typeFrame, text='Product Type', font=('Inter Medium', 12),
                                      text_color='#595959',
                                      width=80, height=26, bg_color='transparent', anchor='w')
        self.typeLabel.place(x=5, y=0)

        self.typeDropdown = ctk.CTkComboBox(self.typeFrame,
                                            values=self.controller.get_type(),  # Insert values here
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

        self.quantityLabel = ctk.CTkLabel(self.quantityFrame, text='Initial Quantity', font=('Inter Medium', 12),
                                          text_color='#595959',
                                          width=106, height=26, bg_color='transparent', anchor='w')
        self.quantityLabel.place(x=5, y=0)

        self.quantityEntry = ctk.CTkEntry(self.quantityFrame, width=160, height=30, corner_radius=7,
                                          bg_color='transparent', fg_color='#FAFAFA',
                                          border_color='#CACACA', border_width=2,
                                          font=('Inter Medium', 12), text_color='#595959', textvariable=self.quantity)
        self.quantityEntry.place(x=0, y=26)

        self.sellingPriceFrame = ctk.CTkFrame(self.productRegFrame, width=160, height=56, fg_color='transparent')
        self.sellingPriceFrame.place(x=25, y=309)

        self.sellingPriceLabel = ctk.CTkLabel(self.sellingPriceFrame, text='Price', font=('Inter Medium', 12),
                                              text_color='#595959',
                                              width=106, height=26, bg_color='transparent', anchor='w')
        self.sellingPriceLabel.place(x=5, y=0)

        self.sellingPriceEntry = ctk.CTkEntry(self.sellingPriceFrame, width=160, height=30, corner_radius=7,
                                              bg_color='transparent', fg_color='#FAFAFA',
                                              border_color='#CACACA', border_width=2,
                                              font=('Inter Medium', 12), text_color='#595959', textvariable=self.price)
        self.sellingPriceEntry.place(x=0, y=26)

        self.capitalPriceFrame = ctk.CTkFrame(self.productRegFrame, width=160, height=56, fg_color='transparent')
        self.capitalPriceFrame.place(x=25, y=365)

        self.capitalPriceLabel = ctk.CTkLabel(self.capitalPriceFrame, text='Capital Price', font=('Inter Medium', 12),
                                              text_color='#595959',
                                              width=106, height=26, bg_color='transparent', anchor='w')
        self.capitalPriceLabel.place(x=5, y=0)

        self.capitalPriceEntry = ctk.CTkEntry(self.capitalPriceFrame, width=160, height=30, corner_radius=7,
                                              bg_color='transparent', fg_color='#FAFAFA',
                                              border_color='#CACACA', border_width=2,
                                              font=('Inter Medium', 12), text_color='#595959', textvariable=self.price)
        self.capitalPriceEntry.place(x=0, y=26)

        self.availabilityFrame = ctk.CTkFrame(self.productRegFrame, width=160, height=56, fg_color='transparent')
        self.availabilityFrame.place(x=25, y=421)

        self.availabilityLabel = ctk.CTkLabel(self.availabilityFrame, text='Availability', font=('Inter Medium', 12),
                                              text_color='#595959',
                                              width=80, height=26, bg_color='transparent', anchor='w')
        self.availabilityLabel.place(x=5, y=0)

        self.availabilityDropdown = ctk.CTkComboBox(self.availabilityFrame,
                                                    values=['For Sale', 'VOID'],  # Insert values here
                                                    width=160, height=30, corner_radius=7,
                                                    bg_color='transparent', fg_color='#FAFAFA',
                                                    border_color='#CACACA', border_width=2, state='readonly',
                                                    font=('Inter Medium', 12), text_color='#595959',
                                                    dropdown_font=('Inter Medium', 12), dropdown_text_color='#595959',
                                                    dropdown_fg_color='#FAFAFA', dropdown_hover_color='#e4e4e4',
                                                    button_color='#CACACA')
        self.availabilityDropdown.set('Select')
        self.availabilityDropdown.place(x=0, y=26)

        self.buttonFrame = ctk.CTkFrame(self.productRegFrame, width=160, height=28, bg_color='transparent',
                                        fg_color='transparent')
        self.buttonFrame.place(x=25, y=487)

        self.clearButton = ctk.CTkButton(self.buttonFrame, width=72, height=28, bg_color='transparent',
                                         fg_color='#E2E2E2', hover_color='#D5D5D5', corner_radius=7,
                                         text='Clear', font=('Consolas', 12), text_color='#595959',
                                         command=self.clear_form)
        self.clearButton.place(x=0, y=0)

        self.saveButton = ctk.CTkButton(self.buttonFrame, width=72, height=28, bg_color='transparent',
                                        fg_color='#1FB2E7', hover_color='#2193BC', corner_radius=7,
                                        text='Save', font=('Consolas', 12), text_color='#F7F7F7',
                                        command=self.save_button_clicked
                                        )
        self.saveButton.place(x=88, y=0)

    def show_productTable(self):
        self.productTableFrame = ctk.CTkFrame(self.baseFrame, width=596, height=526, fg_color='#F7F7F7',
                                              corner_radius=7)
        self.productTableFrame.place(x=235, y=79)

        self.label = ctk.CTkLabel(self.productTableFrame, text="Stock Levels", font=('Inter Medium', 13),
                                  text_color='#2E2E2E')
        self.label.place(x=14, y=7)

        table_values = self.controller.get_data()
        self.reordered_table = []
        for row_values in table_values:
            reordered_row_values = [row_values[0], row_values[1], row_values[3], row_values[2], row_values[5],
                                    row_values[4], row_values[6]]
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
            self.columnLabel.place(x=15 + x_position, y=30)
            x_position += width

        self.columnLine = ctk.CTkFrame(self.productTableFrame, width=598, height=2, fg_color='#D2D2D2')
        self.columnLine.place(x=0, y=53)

        self.tableFrame = ctk.CTkScrollableFrame(self.productTableFrame, width=566, height=297, fg_color='#F7F7F7',
                                                 corner_radius=0)
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
                                                            lambda event, row=row_index: self.handle_cell_click(event,
                                                                                                                row))

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
        print(f"Selected row {row}: {self.reordered_table[row]}")

    def deselect_row(self, row):
        self.table.edit_row(row, fg_color='#F7F7F7')
        print(f"Deselected row {row}: {self.reordered_table[row]}")

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

    def save_button_clicked(self):
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