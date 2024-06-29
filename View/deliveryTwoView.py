import customtkinter as ctk
import tkinter as tk
from CTkTable import *
import json

class deliveryTwoView(ctk.CTkFrame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(width=842, height=620, fg_color='#DFDFDF', corner_radius=0)
        ctk.set_appearance_mode("light")

        self.active_tab = 2
        self.search_query = tk.StringVar()

        self.rowFrames = []

        self.custom_styles()
        self.base_frame()

    def custom_styles(self):
        pass

    def base_frame(self):
        self.baseFrame = ctk.CTkFrame(self, width=842, height=620, fg_color='#DFDFDF', corner_radius=0)
        self.baseFrame.place(x=0, y=0)

        self.place(x=0, y=0)  # Place salesView Frame, do not change this

        self.show_secondPage()
        self.show_orderFrame()
        self.show_historyTable()

        self.baseFrame.bind('<Button-1>', lambda event: self.baseFrame.focus_set())
        self.secondPageFrame.bind('<Button-1>', lambda event: self.secondPageFrame.focus_set())
        self.orderFrame.bind('<Button-1>', lambda event: self.orderFrame.focus_set())

    def show_secondPage(self):
        self.secondPageFrame = ctk.CTkFrame(self.baseFrame, width=522, height=583, fg_color='#F7F7F7',
                                            bg_color='#DFDFDF', corner_radius=7)
        self.secondPageFrame.place(x=12, y=15)

        self.tabFrame = ctk.CTkFrame(self.secondPageFrame, width=246, height=40, fg_color='transparent')
        self.tabFrame.place(x=6, y=7)

        self.selection1 = ctk.CTkButton(self.tabFrame, width=110, height=36, text='New Sale',
                                        font=('Inter', 13, 'bold'), text_color='#9A9A9A',
                                        fg_color='#F7F7F7', hover_color='#F7F7F7',
                                        command=lambda: self.controller.set_active_tab(1))
        self.selection1.place(x=3, y=0)

        self.selection2 = ctk.CTkButton(self.tabFrame, width=110, height=36, text='Sales Report',
                                        font=('Inter', 13, 'bold'), text_color='#2E2E2E',
                                        fg_color='#F7F7F7', hover_color='#F7F7F7',
                                        command=lambda: self.controller.set_active_tab(2))
        self.selection2.place(x=133, y=0)

        self.tabLine = ctk.CTkFrame(self.tabFrame, width=78, height=4, fg_color='#5089B5', corner_radius=7)
        self.tabLine.place(x=150, y=33)

        self.dividerLine = ctk.CTkFrame(self.secondPageFrame, width=522, height=2, fg_color='#DDDDDD')
        self.dividerLine.place(x=0, y=51)

        self.searchFrame = ctk.CTkFrame(self.secondPageFrame, width=160, height=22, fg_color='transparent')
        self.searchFrame.place(x=349, y=14)

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

    def show_historyTable(self):
        # pass
        self.historyTableFrame = ctk.CTkFrame(self.secondPageFrame, width=522, height=288, corner_radius=7,
                                              fg_color='#F7F7F7', bg_color='#DFDFDF')
        self.historyTableFrame.place(x=0, y=52)

        table_values = self.controller.fetch_delivery()
        # print(table_values)
        if table_values is None:
            table_values = []

        self.reordered_table = []
        for row_values in table_values:
            delivery_id, delivery_list, total, date, status = row_values
            self.orderList_JSON = json.loads(delivery_list)
            # reordered_row_values = {
            #     'orderID': row_values['orderID'],
            #     'totalRevenue': row_values['totalRevenue'],
            #     'date': row_values['date'],
            #     'status': row_values['status'],
            #     'productsOrdered': row_values['orderList']
            # }

            reordered_row_values = [row_values[0], row_values[2], row_values[3], row_values[4], row_values[1]]
            self.reordered_table.append(reordered_row_values)
        print(table_values)
        print(self.reordered_table)
        # print("Reordered Table:")
        # for row in self.reordered_table:
        #     print(row)

        column_titles = ['Delivery ID', 'Date', 'Subtotal', 'Status']
        column_widths = [132, 138, 131, 99]  # Table Width = 500

        column_frame = ctk.CTkFrame(self.historyTableFrame, width=522, height=36, fg_color='#F3F3F3',
                                    bg_color='#DFDFDF', corner_radius=0)
        column_frame.place(x=0, y=0)

        """ Table Columns """
        x_position = 0
        for column, (title, width) in enumerate(zip(column_titles, column_widths)):
            self.columnLabel = ctk.CTkLabel(
                column_frame,
                width=column_widths[column],
                height=30,
                text=title,
                fg_color='#F3F3F3',
                font=('Inter Semibold', 12),
                text_color='#9E9E9E',
                corner_radius=0,
                anchor='w'
            )
            self.columnLabel.place(x=12 + x_position, y=3)
            x_position += width

        """ Convert to CTkScrollable Frame """
        self.tableFrame = ctk.CTkScrollableFrame(self.historyTableFrame, width=495, height=252, fg_color='#F7F7F7',
                                                 corner_radius=0)
        self.tableFrame.place(x=12, y=37)

        self.table = CTkTable(master=self.tableFrame, column=4, padx=0, pady=0, font=('Inter Semibold', 11),
                              text_color='#747474',
                              colors=['#F7F7F7', '#F7F7F7'],
                              )

        if not self.reordered_table:
            required_rows = 0
        else:
            required_rows = len(self.reordered_table)

        current_rows = self.table.rows  # Subtract 1 for the header row
        for _ in range(required_rows - current_rows):
            self.table.add_row([''] * 4)  # Add empty rows to meet the required row count

        string_limit = 14
        # Loop through reordered_table and populate table cells
        for row_index, row_values in enumerate(self.reordered_table):
            # Populate table cells with formatted values
            self.table.insert(row_index, 0, row_values[0]) # Delivery ID
            self.table.insert(row_index, 1, row_values[2]) # Date
            self.table.insert(row_index, 2,
                              f"${row_values[1]:.2f}".rstrip('0').rstrip('.'))  # Subtotal
            self.table.insert(row_index, 3, row_values[3])  # Status

        # Configure cell widths and colors after inserting all data
        cell_widths = [132, 138, 131, 99]  # Adjusted based on your table width
        for row in range(self.table.rows):
        #     # Determine status_color based on current row's status_text
        #     # print(self.reordered_table[row][3])
        #     # print(row)
        #     status_text = self.reordered_table[row][3]
        #     if status_text == 'Delivered':
        #         status_color = '#6CB510'
        #     elif status_text == 'Pending':
        #         status_color = '#BB9A25'
        #     else:
        #         status_color = '#868686'  # Default color

            # Configure each cell in the row
            for column in range(self.table.columns):
                self.table.frame[row, column].configure(width=cell_widths[column], height=36,
                                                        fg_color='#F7F7F7', text_color='#868686',
                                                        corner_radius=0, anchor='w')

                # Apply specific configuration for the Status column (assuming index 3)
                # if column == 3:
                    # self.table.frame[row, column].configure(text_color=status_color, font=('Inter Semibold', 12))

        self.table.pack(fill='y', expand=True)

        self.selected_row = None
        self.bind_cell_click_events()

        for row in range(1, self.table.rows + 1):
            rowLine = ctk.CTkFrame(self.tableFrame, width=522, height=2, fg_color='#dbdbdb')
            rowLine.place(x=0, y=(row) * 38 - 1)

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
            self.clear_display_list()
        else:
            if self.selected_row is not None:
                self.deselect_row(self.selected_row)
                self.clear_display_list()

            self.select_row(index)
            self.selected_row = index
            self.display_list(index)
        # selected_row_data = self.table.get_row(index)
        # print(f"Selected row {index}: {self.reordered_table[index]}")

    def clear_display_list(self):
        self.orderIDLabel.configure(text="Delivery #")
        self.status_var.set(value="")
        self.revenueValue.configure(text="")

        for frame in self.rowFrames:
            frame.destroy()
        self.rowFrames.clear()

        if hasattr(self, 'statusDropdown'):  # Check if statusDropdown exists
            self.statusDropdown.destroy()
            del self.statusDropdown

    def select_row(self, row):
        self.table.edit_row(row, fg_color='#EAEAEA')

    def deselect_row(self, row):
        self.table.edit_row(row, fg_color='#F7F7F7')

    def update_status_dropdown_colors(self, *args):
        status = self.status_var.get()
        colors = self.status_colors.get(status, self.status_colors['Available'])

        self.statusDropdown.configure(text_color=colors['text_color'],
                                      button_color=colors['button_color'],
                                      fg_color=colors['fg_color'],
                                      button_hover_color=colors['button_hover_color'])

    def display_list(self, index):
        self.refresh_list()

        row_values = self.reordered_table[index]
        # print(row_values)
        orderID = row_values[0]
        revenue = row_values[1]
        date = row_values[2]
        status = row_values[3]
        orderList = json.loads(row_values[4])

        self.orderIDLabel = ctk.CTkLabel(self.orderFrame, text=f"Delivery #{orderID}", width=121, height=23,
                                         anchor='w',
                                         font=('Inter', 15, 'bold'), text_color='#2E2E2E')
        self.orderIDLabel.place(x=16, y=12)

        self.status_colors = {
            'Delivered': {
                'text_color': '#6CB510',
                'button_color': '#D1EFBE',
                'fg_color': '#D1EFBE',
                'button_hover_color': '#D1EFBE'
            },
            'Pending': {
                'text_color': '#BB9A25',
                'button_color': '#EFE4BE',
                'fg_color': '#EFE4BE',
                'button_hover_color': '#EFE4BE'
            },
            'Available': {
                'text_color': '#868686',
                'button_color': '#F7F7F7',
                'fg_color': '#F7F7F7',
                'button_hover_color': '#F7F7F7'
            }
        }

        # self.orderStatusLabel = ctk.CTkLabel(self.orderFrame, text=status, width=111, height=12, anchor='e', font=('Inter', 10, 'bold'), text_color=text_color)
        # self.orderStatusLabel.place(x=164, y=12)

        self.status_var = ctk.StringVar(value=status)
        self.statusDropdown = ctk.CTkOptionMenu(self.orderFrame,
                                                values=["Delivered", "Pending"],
                                                width=98, height=22,
                                                font=('Inter Semibold', 12),
                                                corner_radius=15,
                                                variable=self.status_var)
        self.statusDropdown.place(x=178, y=14)

        # Bind an event to update colors when dropdown value changes
        self.status_var.trace_add('write', self.update_status_dropdown_colors)

        # Initial update of dropdown colors based on default status
        self.update_status_dropdown_colors()

        self.summaryFrame = ctk.CTkFrame(self.orderFrame, width=285, height=36, fg_color='#F1F1F1', bg_color='#DFDFDF',
                                         corner_radius=7)
        self.summaryFrame.place(x=0, y=547)

        self.revenueLabel = ctk.CTkLabel(self.orderFrame, width=66, height=25, text='Subtotal',
                                         font=('Inter', 14, 'bold'), text_color='#747474', anchor='center',
                                         fg_color='#F1F1F1')
        self.revenueLabel.place(x=14, y=551)

        formatted_revenue = f'₱{revenue:,.2f}'
        self.revenueValue = ctk.CTkLabel(self.orderFrame, width=96, height=25, text=formatted_revenue,
                                         font=('Inter', 14, 'bold'), text_color='#57AF20',
                                         fg_color='#F1F1F1')
        self.revenueValue.place(x=186, y=551)

        # print(f"\nOrder ID: {orderID}\nName: {name}\nContact: {contact}\nRevenue: {revenue}\nDate: {date}\nTimestamp: {timestamp}\nOrder List: {orderList}")
        self.row_counter = 0
        y_position = 0
        print(orderList)
        for product in orderList:
            productName = product['name']
            productBrand = product['brand']
            productQuantity = product['quantity']
            computedPrice = product['price']
            

            # print(f"Product Name: {productName}, Brand: {productBrand}, Quantity: {productQuantity}, Price: {computedPrice}")

            rowFrame = ctk.CTkFrame(self.orderListFrame, width=285, height=40, fg_color='transparent')

            self.rowLine = ctk.CTkFrame(rowFrame, width=285, height=2, fg_color='#E9E9E9')
            self.rowLine.place(x=0, y=39)

            self.productName = ctk.CTkLabel(rowFrame, text=productName, width=90, height=14,
                                            font=('Inter Semibold', 11), text_color='#747474', anchor='w')
            self.productName.place(x=10, y=7)

            self.productBrand = ctk.CTkLabel(rowFrame, text=productBrand, width=90, height=12,
                                             font=('Inter Semibold', 9), text_color='#747474', anchor='w')
            self.productBrand.place(x=10, y=21)

            formatted_price = f'₱{computedPrice:,.2f}'
            self.productPrice = ctk.CTkLabel(rowFrame, text=formatted_price, width=69, height=14,
                                             font=('Inter Semibold', 10), text_color='#747474', anchor='w')
            self.productPrice.place(x=207, y=11)

            self.productQuantity = ctk.CTkLabel(rowFrame, text=productQuantity, width=28, height=14,
                                                font=('Inter Semibold', 10), text_color='#747474', anchor='center')
            self.productQuantity.place(x=148, y=12)
            rowFrame.place(x=0, y=y_position)

            self.rowLine = ctk.CTkFrame(rowFrame, width=285, height=2, fg_color='#E9E9E9')
            self.rowLine.place(x=0, y=39)

            y_position += 40
            self.rowFrames.append(rowFrame)
            self.row_counter += 1

    def refresh_list(self):
        for widget in self.rowFrames:
            widget.destroy()

        self.rowFrames = []

    def show_orderFrame(self):
        self.orderFrame = ctk.CTkFrame(self.baseFrame, width=285, height=583, fg_color='#F7F7F7', corner_radius=7)
        self.orderFrame.place(x=546, y=15)

        self.orderIDLabel = ctk.CTkLabel(self.orderFrame, text="Delivery #", width=121, height=23,
                                         anchor='w',
                                         font=('Inter', 15, 'bold'), text_color='#2E2E2E')
        self.orderIDLabel.place(x=16, y=12)

        self.orderColumnFrame = ctk.CTkFrame(self.orderFrame, width=285, height=24, corner_radius=0, fg_color='#E9E9E9')
        self.orderColumnFrame.place(x=0, y=48)

        self.orderProduct = ctk.CTkLabel(self.orderColumnFrame, text='Product', width=106, height=22,
                                         font=('Inter Semibold', 12), text_color='#B8B8B8', anchor='w')
        self.orderProduct.place(x=10, y=1)

        self.orderQuantity = ctk.CTkLabel(self.orderColumnFrame, text='Qty', width=28, height=22,
                                          font=('Inter Semibold', 12), text_color='#B8B8B8', anchor='center')
        self.orderQuantity.place(x=148, y=1)

        self.orderPrice = ctk.CTkLabel(self.orderColumnFrame, text='Price', width=63, height=22,
                                       font=('Inter Semibold', 12), text_color='#B8B8B8', anchor='w')
        self.orderPrice.place(x=207, y=1)

        self.orderListFrame = ctk.CTkFrame(self.orderFrame, width=285, height=354, fg_color='transparent')
        self.orderListFrame.place(x=0, y=72)

        self.orderIDLabel = ctk.CTkLabel(self.orderFrame, text=f"Delivery #", width=121, height=23,
                                         anchor='w',
                                         font=('Inter', 15, 'bold'), text_color='#2E2E2E')
        self.orderIDLabel.place(x=16, y=12)

        self.summaryFrame = ctk.CTkFrame(self.orderFrame, width=285, height=36, fg_color='#F1F1F1', bg_color='#DFDFDF',
                                         corner_radius=7)
        self.summaryFrame.place(x=0, y=547)

        self.revenueLabel = ctk.CTkLabel(self.orderFrame, width=66, height=25, text='Subtotal',
                                         font=('Inter', 14, 'bold'), text_color='#747474', anchor='center',
                                         fg_color='#F1F1F1')
        self.revenueLabel.place(x=14, y=551)

    def clear_base_frame(self):
        for widget in self.baseFrame.winfo_children():
            widget.destroy()


class App:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Delivery Two Page (Test)")

        self.salesTwo_view = deliveryTwoView(self.root, None)
        self.salesTwo_view.pack(fill=ctk.BOTH, expand=True)

        self.root.update()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()