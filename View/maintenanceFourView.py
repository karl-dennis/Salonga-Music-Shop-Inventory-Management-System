import customtkinter as ctk
from CTkTable import *
from PIL import Image

class maintenanceFourView(ctk.CTkFrame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(width=842, height=620, fg_color='#DFDFDF', corner_radius=0)
        ctk.set_appearance_mode("light")

        self.active_tab = 4
        self.search_query = ctk.StringVar()
        
        self.custom_styles()
        self.base_frame()
 
    def custom_styles(self):
        pass

    def base_frame(self):    
        self.baseFrame = ctk.CTkFrame(self, width=842, height=620, fg_color='#DFDFDF', corner_radius=0)
        self.baseFrame.place(x=0, y=0)
        
        self.place(x=0, y=0) # Place productView Frame, do not change this

        self.show_maintenanceFour()
        self.show_salesTable()
            
            
    def show_maintenanceFour(self):
        self.maintenanceFourFrame = ctk.CTkFrame(self.baseFrame, width=820, height=51, fg_color='#F7F7F7', corner_radius=7)
        self.maintenanceFourFrame.place(x=11, y=15)
            
        self.tabFrame = ctk.CTkFrame(self.maintenanceFourFrame, width=820, height=51, bg_color='#DFDFDF', fg_color='#F7F7F7', corner_radius=7)
        self.tabFrame.place(x=0, y=0)
        
        self.selection1 = ctk.CTkButton(self.tabFrame, width=115, height=18, text='Manage Users',
                                        font=('Inter', 13, 'bold'), text_color='#9A9A9A',
                                        fg_color='#F7F7F7', hover_color='#F7F7F7', command=lambda: self.controller.set_active_tab(1))
        self.selection1.place(x=9, y=14)
        
        self.selection2 = ctk.CTkButton(self.tabFrame, width=115, height=18, text='User Logs',
                                        font=('Inter', 13, 'bold'), text_color='#9A9A9A',
                                        fg_color='#F7F7F7', hover_color='#F7F7F7', command=lambda: self.controller.set_active_tab(2))
        self.selection2.place(x=140, y=14)

        self.selection3 = ctk.CTkButton(self.tabFrame, width=115, height=18, text='Manage Products',
                                        font=('Inter', 13, 'bold'), text_color='#9A9A9A',
                                        fg_color='#F7F7F7', hover_color='#F7F7F7', command=lambda: self.controller.set_active_tab(3))
        self.selection3.place(x=271, y=14)

        self.selection4 = ctk.CTkButton(self.tabFrame, width=115, height=18, text='Manage Sales',
                                        font=('Inter', 13, 'bold'), text_color='#2E2E2E',
                                        fg_color='#F7F7F7', hover_color='#F7F7F7')
        self.selection4.place(x=402, y=14)

        self.selection5 = ctk.CTkButton(self.tabFrame, width=115, height=18, text='Manage System',
                                        font=('Inter', 13, 'bold'), text_color='#9A9A9A',
                                        fg_color='#F7F7F7', hover_color='#F7F7F7', command=self.show_systemDialog)
        self.selection5.place(x=533, y=14)
        
        self.system_dialog = None

        self.tabLine = ctk.CTkFrame(self.tabFrame, width=78, height=4, fg_color='#5089B5', corner_radius=7)
        self.tabLine.place(x=421, y=39)
    
    def show_salesTable(self):
        self.salesTableFrame = ctk.CTkFrame(self.baseFrame, width=820, height=526, fg_color='#F7F7F7', corner_radius=7)
        self.salesTableFrame.place(x=11, y=79)
        
        # table_values = self.controller.get_data()
        table_values = [
            ['O0001', 'Fritz Gonzales', '09692123869', 25700, '10-12-2024', '10:00:25', 'Active'],
            ['O0002', 'Lucas Ballesteros', '09998299276', 8500, '11-15-2024', '13:01:25', 'Active']
        ]
        
        self.reordered_table = []
        for row_values in table_values:
            reordered_row_values = [row_values[0], row_values[1], row_values[2], row_values[3], row_values[4], row_values[5], row_values[6]]
            self.reordered_table.append(reordered_row_values)
            
        column_titles = ['Order ID', 'Buyer', 'Contact #', 'Revenue', 'Date', 'Time', 'Status']
        column_widths = [94, 142, 144, 127, 110, 90, 91] # Table Width = 798
        
        column_frame = ctk.CTkFrame(self.salesTableFrame, width=798, height=34, fg_color='#F7F7F7',
                                    bg_color='#DFDFDF', corner_radius=0)
        column_frame.place(x=17, y=0)
        
        x_position = 0
        for column, (title, width) in enumerate(zip(column_titles, column_widths)):
            self.columnLabel = ctk.CTkLabel(
                column_frame, 
                width=column_widths[column], 
                height=34, 
                text=title, 
                fg_color='#F7F7F7',
                font=('Inter Semibold', 12),
                text_color='#9E9E9E',
                corner_radius=0, 
                anchor='w'
            )
            self.columnLabel.place(x=x_position, y=0)
            x_position += width
            
        self.columnLine = ctk.CTkFrame(self.salesTableFrame, width=820, height=2, fg_color='#D2D2D2')
        self.columnLine.place(x=0, y=32)
        
        """ Table Rows """
        self.tableFrame = ctk.CTkScrollableFrame(self.salesTableFrame, width=790, height=490, fg_color='#F7F7F7',
                                                 corner_radius=0)
        self.tableFrame.place(x=13, y=34)

        self.table = CTkTable(master=self.tableFrame, column=6, padx=0, pady=0, font=('Inter Medium', 12),
                              text_color='#747474',
                              colors=['#F7F7F7', '#F7F7F7'])

        if not self.reordered_table:
            required_rows = 0
        else:
            required_rows = len(self.reordered_table)

        current_rows = self.table.rows
        for _ in range(required_rows - current_rows):
            self.table.add_row([''] * 6)

        for row_index, row_values in enumerate(self.reordered_table):
            self.table.insert(row_index, 0, row_values[0])
            self.table.insert(row_index, 1, row_values[1])
            self.table.insert(row_index, 2, row_values[2])
            revenue_value = f'₱{row_values[3]:,.2f}'.rstrip('0').rstrip('.')
            self.table.insert(row_index, 3, revenue_value)
            self.table.insert(row_index, 4, row_values[4])
            self.table.insert(row_index, 5, row_values[5])
        
        cell_widths = [94, 142, 144, 127, 110, 90, 91] # Table Width = 798
        for row in range(self.table.rows):                
            for column in range(self.table.columns):
                self.table.frame[row, column].configure(width=cell_widths[column], height=38,
                                                        fg_color='#F7F7F7', text_color='#868686',
                                                        corner_radius=0, anchor='w')

        self.table.pack(fill='y', expand=True, anchor='w')

        self.selected_row = None
        self.bind_cell_click_events()
        
        for row in range(1, self.table.rows + 1):
            rowLine = ctk.CTkFrame(self.tableFrame, width=798, height=2, fg_color='#dbdbdb')
            rowLine.place(x=0, y=(row) * 38)
            
        self.status_colors = {
            'Active': {
                'text_color': '#6CB510',
                'button_color': '#D1EFBE',
                'fg_color': '#D1EFBE',
                'button_hover_color': '#D1EFBE'
            },
            'Inactive': {
                'text_color': '#A65656',
                'button_color': '#EECECE',
                'fg_color': '#EECECE',
                'button_hover_color': '#EECECE'
            },
        }
        
        self.status_vars = [] 
        self.status_dropdowns = []
        for row in range(0, self.table.rows):
            status_var = ctk.StringVar(value=self.reordered_table[row][6])
            status_dropdown = ctk.CTkOptionMenu(self.tableFrame,
                                                values=["Active", "Inactive"],
                                                width=70, height=16,
                                                font=('Inter Medium', 9),
                                                corner_radius=10,
                                                variable=status_var)
            status_dropdown.place(x=710, y=11 + (row * 38))

            status_var.trace_add('write', lambda *args, sv=status_var, sd=status_dropdown: self.update_status_dropdown_colors(sv, sd))
            self.update_status_dropdown_colors(status_var, status_dropdown)

            self.status_vars.append(status_var)
            self.status_dropdowns.append(status_dropdown)    
            
    def update_status_dropdown_colors(self, status_var, status_dropdown):
        status = status_var.get()
        colors = self.status_colors.get(status, self.status_colors['Active'])

        status_dropdown.configure(text_color=colors['text_color'],
                                button_color=colors['button_color'],
                                fg_color=colors['fg_color'],
                                button_hover_color=colors['button_hover_color'])  
            
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
        print(f"Selected row {row}: {self.reordered_table[row]}")

    def deselect_row(self, row):
        self.table.edit_row(row, fg_color='#F7F7F7')
        print(f"Deselected row {row}: {self.reordered_table[row]}")
    
    def clear_base_frame(self):
        for widget in self.baseFrame.winfo_children():
            widget.destroy()

    def show_systemDialog(self):
        if self.system_dialog is None or not self.system_dialog.winfo_exists():
            self.system_dialog = SystemDialog(self)  
        else:
            self.system_dialog.focus() 
            
class SystemDialog(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("370x220")
        self.title("Backup & Restore")
        self.configure(fg_color='#EBEBEB')
        self.resizable(False, False)        
        
        self.center_window()
        
        backupFrame = ctk.CTkFrame(self, width=120, height=148, fg_color='transparent')
        backupFrame.place(x=36, y=33)
        
        backup_icon = ctk.CTkImage(light_image=Image.open('./assets/backup.png'), size=(102, 79))
        backupButton = ctk.CTkButton(backupFrame, image=backup_icon, text='', width=110, height=110,
                                     border_width=3, border_color='#B5B5B5', fg_color='#E2E2E2', corner_radius=7,
                                     hover_color='#E2E2E2', anchor='center', bg_color='#EBEBEB')
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
                                     hover_color='#1FB2E7', anchor='center', bg_color='#EBEBEB')
        restoreButton.place(x=0, y=0)
        
        restoreLabel = ctk.CTkLabel(restoreFrame, width=120, height=32, 
                                   text="Restore your data from\na previous backup.",
                                   font=('Inter Medium', 10), text_color='#0792C5')
        restoreLabel.place(x=0, y=116)
        
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
        self.root.title("Maintenance Four Page (Test)")
        
        self.maintenancefour_view = maintenanceFourView(self.root, None)
        self.maintenancefour_view.pack(fill=ctk.BOTH, expand=True)
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()