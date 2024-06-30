import customtkinter as ctk
from CTkTable import *

class maintenanceTwoView(ctk.CTkFrame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(width=842, height=620, fg_color='#DFDFDF', corner_radius=0)
        ctk.set_appearance_mode("light")

        self.active_tab = 2
        self.search_query = ctk.StringVar()
        
        self.custom_styles()
        self.base_frame()
 
    def custom_styles(self):
        pass

    def base_frame(self):    
        self.baseFrame = ctk.CTkFrame(self, width=842, height=620, fg_color='#DFDFDF', corner_radius=0)
        self.baseFrame.place(x=0, y=0)
        
        self.place(x=0, y=0) # Place productView Frame, do not change this

        self.show_maintenanceTwo()
        self.show_userLogsTable()
        
    def show_maintenanceTwo(self):
        self.maintenanceTwoFrame = ctk.CTkFrame(self.baseFrame, width=820, height=51, fg_color='#F7F7F7', corner_radius=7)
        self.maintenanceTwoFrame.place(x=11, y=15)
            
        self.tabFrame = ctk.CTkFrame(self.maintenanceTwoFrame, width=820, height=51, bg_color='#DFDFDF', fg_color='#F7F7F7', corner_radius=7)
        self.tabFrame.place(x=0, y=0)
        
        self.selection1 = ctk.CTkButton(self.tabFrame, width=115, height=18, text='Manage Users',
                                        font=('Inter', 13, 'bold'), text_color='#9A9A9A',
                                        fg_color='#F7F7F7', hover_color='#F7F7F7', command=lambda: self.controller.set_active_tab(1))
        self.selection1.place(x=9, y=14)
        
        self.selection2 = ctk.CTkButton(self.tabFrame, width=115, height=18, text='User Logs',
                                        font=('Inter', 13, 'bold'), text_color='#2E2E2E',
                                        fg_color='#F7F7F7', hover_color='#F7F7F7')
        self.selection2.place(x=140, y=14)

        self.selection3 = ctk.CTkButton(self.tabFrame, width=115, height=18, text='Manage Products',
                                        font=('Inter', 13, 'bold'), text_color='#9A9A9A',
                                        fg_color='#F7F7F7', hover_color='#F7F7F7', command=lambda: self.controller.set_active_tab(3))
        self.selection3.place(x=271, y=14)

        self.selection4 = ctk.CTkButton(self.tabFrame, width=115, height=18, text='System',
                                        font=('Inter', 13, 'bold'), text_color='#9A9A9A',
                                        fg_color='#F7F7F7', hover_color='#F7F7F7', command=lambda: self.controller.set_active_tab(4))
        self.selection4.place(x=402, y=14)

        self.tabLine = ctk.CTkFrame(self.tabFrame, width=78, height=4, fg_color='#5089B5', corner_radius=7)
        self.tabLine.place(x=159, y=39)

    def show_userLogsTable(self):
        self.userLogsTableFrame = ctk.CTkFrame(self.baseFrame, width=820, height=526, corner_radius=7,
                                               fg_color='#F7F7F7', bg_color='#DFDFDF')
        self.userLogsTableFrame.place(x=11, y=79)

        """ [date, timestamp, username, employeeID, role] """
        table_values = [
            ['June 30, 2024', '10:21:54', 'seris', 'A0001', 'Admin'],
            ['July 01, 2024', '00:01:21', 'fritz', 'E0001', 'Employee'],
        ]
        
        self.reordered_table = []
        
        for row_values in table_values:
            action = f"{row_values[2]} logged in at {row_values[1]}" # username logged in at timestamp
            reordered_row_values = [row_values[0], row_values[1], action, row_values[3], row_values[4]]
            self.reordered_table.append(reordered_row_values)
            
        column_titles = ['Date', 'Timestamp', 'Action', 'Employee ID', 'Status']
        column_widths = [165, 165, 165, 165, 120] # Table Width = 780
        
        column_frame = ctk.CTkFrame(self.userLogsTableFrame, width=780, height=28, fg_color='#F7F7F7',
                                    bg_color='#DFDFDF', corner_radius=0)
        column_frame.place(x=23, y=2)
        
        """ Table Columns """
        x_position = 0
        for column, (title, width) in enumerate(zip(column_titles, column_widths)):
            self.columnLabel = ctk.CTkLabel(
                column_frame,
                width=column_widths[column],
                height=25,
                text=title,
                fg_color='#F7F7F7',
                font=('Inter Semibold', 12),
                text_color='#9E9E9E',
                corner_radius=0,
                anchor='w'
            )
            self.columnLabel.place(x=0 + x_position, y=0)
            x_position += width
        
        columnLine = ctk.CTkFrame(self.userLogsTableFrame, width=820, height=2, fg_color='#dbdbdb')
        columnLine.place(x=0, y=28)
        
        """ Table Rows """
        self.tableFrame = ctk.CTkScrollableFrame(self.userLogsTableFrame, width=780, height=496, fg_color='#F7F7F7', corner_radius=0)
        self.tableFrame.place(x=23, y=30)
        
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
            self.table.insert(row_index, 3, row_values[3])
            self.table.insert(row_index, 4, row_values[4])
        
        cell_widths = [165, 165, 165, 165, 120] # Table Width = 780
        for row in range(self.table.rows):                
            for column in range(self.table.columns):
                self.table.frame[row, column].configure(width=cell_widths[column], height=28,
                                                        fg_color='#F7F7F7', text_color='#868686',
                                                        corner_radius=0, anchor='w')
        self.table.pack(fill='y', expand=True, anchor='w')
        
        for row in range(1, self.table.rows + 1):
            rowLine = ctk.CTkFrame(self.tableFrame, width=800, height=2, fg_color='#dbdbdb')
            rowLine.place(x=0, y=(row) * 28 - 1)
        
        
        
    def clear_base_frame(self):
        for widget in self.baseFrame.winfo_children():
            widget.destroy()
    
class App:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Maintenance Two Page (Test)")
        
        self.maintenancetwo_view = maintenanceTwoView(self.root, None)
        self.maintenancetwo_view.pack(fill=ctk.BOTH, expand=True)
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()