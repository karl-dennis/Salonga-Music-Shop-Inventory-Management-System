import customtkinter as ctk
import tkinter as tk
from CTkTable import *

class salesTwoView(ctk.CTkFrame):

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
        
        self.place(x=0, y=0) # Place salesView Frame, do not change this
        
        self.show_secondPage()
        self.show_orderFrame()
        self.show_salesGraph()
        self.show_revenue()
        self.show_reports()
        self.show_historyTable()
        
        self.baseFrame.bind('<Button-1>', lambda event: self.baseFrame.focus_set())
        self.secondPageFrame.bind('<Button-1>', lambda event: self.secondPageFrame.focus_set())
        self.orderFrame.bind('<Button-1>', lambda event: self.orderFrame.focus_set())
        self.salesGraphFrame.bind('<Button-1>', lambda event: self.salesGraphFrame.focus_set())
        self.revenueFrame.bind('<Button-1>', lambda event: self.revenueFrame.focus_set())
        self.reportsFrame.bind('<Button-1>', lambda event: self.reportsFrame.focus_set())

                
    def show_secondPage(self):
        self.secondPageFrame = ctk.CTkFrame(self.baseFrame, width=522, height=340, fg_color='#F7F7F7', bg_color='#DFDFDF', corner_radius=7)
        self.secondPageFrame.place(x=12, y=15)
        
        self.tabFrame = ctk.CTkFrame(self.secondPageFrame, width=246, height=40, fg_color='transparent')
        self.tabFrame.place(x=6, y=7)
        
        self.selection1 = ctk.CTkButton(self.tabFrame, width=110, height=36, text='New Sale',
                                        font=('Inter', 13, 'bold'), text_color='#9A9A9A',
                                        fg_color='#F7F7F7', hover_color='#F7F7F7', command=lambda: self.controller.set_active_tab(1))
        self.selection1.place(x=3, y=0)
        
        self.selection2 = ctk.CTkButton(self.tabFrame, width=110, height=36, text='Sales Report',
                                        font=('Inter', 13, 'bold'), text_color='#2E2E2E',
                                        fg_color='#F7F7F7', hover_color='#F7F7F7', command=lambda: self.controller.set_active_tab(2))
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

        # table_values = self.controller.get_data()
        # reordered_table = []

        order1 = [
            {
                'productName': 'productName1',
                'productBrand': 'productBrand1',
                'productQuantity': 1,
                'computedPrice': 100.0,
                'BLOB': 'BLOB1'
            },
            {
                'productName': 'productName2',
                'productBrand': 'productBrand2',
                'productQuantity': 2,
                'computedPrice': 200.0,
                'BLOB': 'BLOB2'
            }
        ]
        
        order2 = [
            {
                'productName': 'productName3',
                'productBrand': 'productBrand3',
                'productQuantity': 3,
                'computedPrice': 300.0,
                'BLOB': 'BLOB3'
            },
            {
                'productName': 'productName4',
                'productBrand': 'productBrand4',
                'productQuantity': 4,
                'computedPrice': 400.0,
                'BLOB': 'BLOB4'
            }
        ]
        product_orders = [order1, order2]
        
        table_values = [
            {
                'orderID': '0001',
                'products_ordered': order1,
                'buyerName': 'Fritz Gonzales',
                'buyerContact': '0999-999-9999',
                'totalRevenue': 300.0,
                'date': '2023-06-26',
                'timestamp': '12:00:00'
            },
            {
                'orderID': '0002',
                'products_ordered': order2,
                'buyerName': 'Lucas Ballesteros',
                'buyerContact': '0999-999-9999',
                'totalRevenue': 700.0,
                'date': '2023-06-27',
                'timestamp': '14:00:00'
            }
        ]

        reordered_table = []
        for row_values in table_values:
            reordered_row_values = {
                'orderID': row_values['orderID'],
                'buyerName': row_values['buyerName'],
                'buyerContact': row_values['buyerContact'],
                'totalRevenue': row_values['totalRevenue'],
                'date': row_values['date'],
                'timestamp': row_values['timestamp']
            }
            reordered_table.append(reordered_row_values)
            
        # print("Reordered Table:")
        # for row in reordered_table:
        #     print(row)
            
        column_titles = ['Order ID', 'Buyer', 'Contact #', 'Revenue', 'Date', 'Time']
        column_widths = [67, 101, 102, 91, 78, 65] # Table Width = 504
        
        column_frame = ctk.CTkFrame(self.historyTableFrame, width=522, height=36, fg_color='#F3F3F3', bg_color='#DFDFDF', corner_radius=0)
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
            self.columnLabel.place(x=12+x_position, y=3)
            x_position += width
        
        """ Convert to CTkScrollable Frame """
        self.tableFrame = ctk.CTkScrollableFrame(self.historyTableFrame, width=495, height=252, fg_color='#F7F7F7', corner_radius=0)
        self.tableFrame.place(x=12, y=37)
        
        self.table = CTkTable(master=self.tableFrame, column=6, padx=0, pady=0, font=('Inter Semibold', 11), text_color='#747474',
                              colors=['#F7F7F7', '#F7F7F7'],
                              )
        
        if not reordered_table:
            required_rows = 0
        else:
            required_rows = len(reordered_table)
        
        current_rows = self.table.rows  # Subtract 1 for the header row
        for _ in range(required_rows - current_rows):
            self.table.add_row([''] * 6)  # Add empty rows to meet the required row count
            
        string_limit = 14
        for row_index, row_values in enumerate(reordered_table):
            # Populate table cells with formatted values
            self.table.insert(row_index, 0, row_values['orderID'])
            self.table.insert(row_index, 1, row_values['buyerName'])
            self.table.insert(row_index, 2, row_values['buyerContact'])
            self.table.insert(row_index, 3, f"${row_values['totalRevenue']:.2f}".rstrip('0').rstrip('.'))  # Format revenue
            self.table.insert(row_index, 4, row_values['date'])
            self.table.insert(row_index, 5, row_values['timestamp'])
    
        cell_widths = [67, 101, 102, 91, 78, 65] # Table Width = 504
        for row in range(self.table.rows):
            for column in range(self.table.columns):
                self.table.frame[row, column].configure(width=cell_widths[column], height=36, 
                                                        fg_color='#F7F7F7', text_color='#868686', 
                                                        corner_radius=0, anchor='w')

        self.table.pack(fill='y', expand=True)
        
        self.selected_row = None
        self.bind_cell_click_events()

        for row in range(1, self.table.rows + 1):
            rowLine = ctk.CTkFrame(self.tableFrame, width=522, height=2, fg_color='#dbdbdb')
            rowLine.place(x=0, y=(row) * 38 - 1)


    def bind_cell_click_events(self):
        for row_index in range(self.table.rows):
            for col_index in range(self.table.columns):
                # Bind click event to each cell in the table
                self.table.frame[row_index, col_index].bind("<Button-1>", lambda event, row=row_index: self.handle_cell_click(event, row))

    def handle_cell_click(self, event, row_index):
        if self.selected_row is not None:
            self.deselect_row(self.selected_row)

        self.select_row(row_index)
        self.selected_row = row_index
        
        selected_row_data = self.table.get_row(row_index)
        print(f"Selected row {row_index}: {selected_row_data}")
        """Connect controller here"""

    def select_row(self, row):
        self.table.edit_row(row, fg_color='#EAEAEA') 

    def deselect_row(self, row):
        self.table.edit_row(row, fg_color='#F7F7F7') 

        
    def show_orderFrame(self):
        self.orderFrame = ctk.CTkFrame(self.baseFrame, width=285, height=583, fg_color='#F7F7F7', corner_radius=7)
        self.orderFrame.place(x=546, y=15)
        
        orderID = 1 # ID Counter, increments on click (save button)
        
        self.orderIDLabel = ctk.CTkLabel(self.orderFrame, text=f"Order #{orderID:04}", width=121, height=23, # Pads zeroes (length of 4), e.g. 0001
                                         font=('Inter', 15, 'bold'), text_color='#2E2E2E') 
        self.orderIDLabel.place(x=82, y=12)
        
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
        
    def show_salesGraph(self):
        self.salesGraphFrame = ctk.CTkFrame(self.baseFrame, width=315, height=232, fg_color='#F7F7F7', corner_radius=7)
        self.salesGraphFrame.place(x=12, y=367)
        
        self.label = ctk.CTkLabel(self.salesGraphFrame, text="Sales Graph", font=('Inter Medium', 13), text_color='#2E2E2E',
                                  width=130, height=16, anchor='w')
        self.label.place(x=12, y=8)

    def show_revenue(self):
        from PIL import Image
        self.revenueFrame = ctk.CTkFrame(self.baseFrame, width=201, height=58, fg_color='#F7F7F7', 
                                         bg_color='transparent', border_width=3, border_color='#5089B5',
                                         corner_radius=7)
        self.revenueFrame.place(x=334, y=367)
        
        self.icon = ctk.CTkImage(light_image=Image.open("./assets/revenue.png"), size=(30,30))
        self.my_icon = ctk.CTkLabel(self.revenueFrame, text="", image=self.icon)
        self.my_icon.place(x=13, y=10)
        
        self.label = ctk.CTkLabel(self.revenueFrame, text="Revenue (May 2024)", font=('Inter', 13, 'bold'), 
                                  text_color='#5089B5', fg_color='transparent',
                                  width=145, height=15, anchor='w')
        self.label.place(x=50, y=13)
        
        self.label = ctk.CTkLabel(self.revenueFrame, text="₱18,049.25", font=('Inter Medium', 12), 
                                  text_color='#5089B5', fg_color='transparent', 
                                  width=130, height=12, anchor='w')
        self.label.place(x=50, y=26)
    
    def show_reports(self):
        self.reportsFrame = ctk.CTkFrame(self.baseFrame, width=201, height=165, fg_color='#F7F7F7', corner_radius=7)
        self.reportsFrame.place(x=334, y=434)
        
        self.label = ctk.CTkLabel(self.reportsFrame, text="Reports", font=('Inter Medium', 13), text_color='#2E2E2E')
        self.label.place(x=14, y=7)
    
    def clear_base_frame(self):
        for widget in self.baseFrame.winfo_children():
            widget.destroy()

class App:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Sales Two Page (Test)")

        self.salesTwo_view = salesTwoView(self.root, None)
        self.salesTwo_view.pack(fill=ctk.BOTH, expand=True)

        self.root.update()
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()