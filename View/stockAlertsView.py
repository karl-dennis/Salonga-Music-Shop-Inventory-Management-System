import customtkinter as ctk
from CTkTable import *


class stockAlertsView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, 
                         width=360, height=280, 
                         fg_color='transparent', corner_radius=7)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        # Add your widgets here
        self.baseFrame = ctk.CTkFrame(self, width=360, height=280, fg_color='#F7F7F7')
        # self.baseFrame.pack_propagate(0)
        # self.baseFrame.pack()
        self.baseFrame.place(x=0, y=0)
        
        label = ctk.CTkLabel(self.baseFrame, text="Sales History", font=('Inter Medium', 12), text_color='#2E2E2E',
                             width=80, height=14)
        label.place(x=13, y=12)
        
        view_all = ctk.CTkButton(self.baseFrame, text="View All", font=("Inter Medium", 12, 'underline'), 
                                            text_color="#2E8EC4", fg_color='transparent', hover_color='#F7F7F7',
                                            width=60, height=14)
        view_all.place(x=290, y=9)
        
        self.show_salesHistoryTable()
        
    
    def show_salesHistoryTable(self):
        self.salesHistoryTableFrame = ctk.CTkFrame(self.baseFrame, width=360, height=251, corner_radius=7,
                                                   fg_color='#F7F7F7', bg_color='#DFDFDF')
        self.salesHistoryTableFrame.place(x=0, y=30)
        
        table_values = self.controller.fetch_transaction()
        # table_values = [
        #     ['O0001', 'Fritz', 'Gonzales', '09212267656', 12500, '10:59 PM'],
        #     ['O0002', 'Bob', 'Gomez', '09212267656', 8700, '02:51 AM'],
        # ]
        
        self.reordered_table = []
        for row_values in table_values:
            reordered_row_values = [row_values[0], row_values[1], row_values[2], row_values[3], row_values[4]]
            self.reordered_table.append(reordered_row_values)
        
        column_titles = ['Order ID', 'Buyer', 'Contact #', 'Revenue', 'Time']
        column_widths = [54, 81, 93, 69, 50] # Table Width = 347
        
        column_frame = ctk.CTkFrame(self.salesHistoryTableFrame, width=347, height=24, fg_color='#F7F7F7',
                                    bg_color='#F7F7F7', corner_radius=0)
        column_frame.place(x=9, y=0)
        
        """ Table Columns """
        x_position = 0
        for column, (title, width) in enumerate(zip(column_titles, column_widths)):
            self.columnLabel = ctk.CTkLabel(
                column_frame,
                width=column_widths[column],
                height=24,
                text=title,
                fg_color='#F7F7F7', bg_color='#F7F7F7',
                font=('Inter Semibold', 10),
                text_color='#9E9E9E',
                corner_radius=0,
                anchor='w'
            )
            self.columnLabel.place(x=3 + x_position, y=0)
            x_position += width
        
        columnLine = ctk.CTkFrame(self.salesHistoryTableFrame, width=596, height=2, fg_color='#dbdbdb')
        columnLine.place(x=0, y=24)
        
        """ Table Rows """
        self.tableFrame = ctk.CTkScrollableFrame(self.salesHistoryTableFrame, width=347, height=249, fg_color='#F7F7F7', corner_radius=0)
        self.tableFrame.place(x=9, y=26)
        
        self.table = CTkTable(master=self.tableFrame, column=5, padx=0, pady=0, font=('Inter Medium', 10), text_color='#747474',
                              colors=['#F7F7F7', '#F7F7F7'])
        
        if not self.reordered_table:
            required_rows = 0
        else:
            required_rows= len(self.reordered_table)
        
        current_rows = self.table.rows
        for _ in range(required_rows - current_rows):
            self.table.add_row([''] * 5)
            
        for row_index, row_values in enumerate(self.reordered_table):
            self.table.insert(row_index, 0, row_values[0])
            self.table.insert(row_index, 1, row_values[1])
            self.table.insert(row_index, 2, row_values[2])
            revenue_value = f'₱{row_values[3]:,.2f}'.rstrip('0').rstrip('.')
            self.table.insert(row_index, 3, revenue_value)
            self.table.insert(row_index, 4, row_values[4])

        cell_widths = [54, 81, 93, 69, 50] # Table Width = 347
        for row in range(self.table.rows):                
            for column in range(self.table.columns):
                self.table.frame[row, column].configure(width=cell_widths[column], height=26,
                                                        fg_color='#F7F7F7', text_color='#868686',
                                                        corner_radius=0, anchor='w')

        self.table.pack(fill='y', expand=True, anchor='w')
        
        