from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import customtkinter as ctk
from CTkTable import *
from PIL import Image
import shutil
import os
import datetime
from tkinter import filedialog

class maintenanceFourView(ctk.CTkFrame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(width=842, height=620, fg_color='#DFDFDF', corner_radius=0)
        ctk.set_appearance_mode("light")

        self.status_var = ctk.StringVar()

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
        
        generate_report_btn = ctk.CTkButton(self.baseFrame, text="Generate PDF Report",
                                            font=('Consolas', 12), text_color='#F7F7F7', bg_color='#F7F7F7',
                                            fg_color='#1FB2E7', hover_color='#2193BC', corner_radius=8,
                                            command=self.generate_pdf_report)
        generate_report_btn.place(x=23, y=570)

            
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

        self.selection5 = ctk.CTkButton(self.tabFrame, width=115, height=18, text='Backup & Restore',
                                        font=('Inter', 13, 'bold'), text_color='#9A9A9A',
                                        fg_color='#F7F7F7', hover_color='#F7F7F7', command=self.show_systemDialog)
        self.selection5.place(x=533, y=14)
        
        self.system_dialog = None

        self.tabLine = ctk.CTkFrame(self.tabFrame, width=78, height=4, fg_color='#5089B5', corner_radius=7)
        self.tabLine.place(x=421, y=39)
    
    def show_salesTable(self):
        self.salesTableFrame = ctk.CTkFrame(self.baseFrame, width=820, height=526, fg_color='#F7F7F7', corner_radius=7)
        self.salesTableFrame.place(x=11, y=79)
        
        table_values = self.controller.get_data()
        # table_values = [
        #     ['O0001', 'Fritz Gonzales', '09692123869', 25700, '10-12-2024', '10:00:25', 'Active'],
        #     ['O0002', 'Lucas Ballesteros', '09998299276', 8500, '11-15-2024', '13:01:25', 'Active']
        # ]
        
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

            self.status_dropdown = ctk.CTkOptionMenu(self.tableFrame,
                                                values=["Active", "Inactive"],
                                                width=70, height=16,
                                                font=('Inter Medium', 9),
                                                corner_radius=10,
                                                variable=self.status_var.set(self.reordered_table[row][6]),
                                                command=self.on_dropdown_clicked)
            self.status_dropdown.place(x=710, y=11 + (row * 38))

            self.status_dropdown.bind("<Button-1>", self.on_dropdown_clicked)

            self.status_var.trace_add('write', lambda *args, sv=self.status_var, sd=self.status_dropdown: self.update_status_dropdown_colors(sv, sd))
            self.update_status_dropdown_colors(self.status_var, self.status_dropdown)

            self.status_vars.append(self.status_var)
            self.status_dropdowns.append(self.status_dropdown)
            
    def update_status_dropdown_colors(self, status_var, status_dropdown):
        status = status_var.get()
        colors = self.status_colors.get(status, self.status_colors['Active'])

        status_dropdown.configure(text_color=colors['text_color'],
                                button_color=colors['button_color'],
                                fg_color=colors['fg_color'],
                                button_hover_color=colors['button_hover_color'])

    def update_status_cell(self, row_index, new_status):
        # Determine the status color based on the new status
        if new_status == 'Delivered':
            status_color = '#6CB510'
        elif new_status == 'Pending':
            status_color = '#BB9A25'
        else:
            status_color = '#868686'  # Default color

        # Update the cell text and color in the table
        self.table.insert(row_index, 3, new_status)
        self.table.frame[row_index, 3].configure(text_color=status_color, font=('Inter Semibold', 12))

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

    def on_dropdown_clicked(self, event):
        # This function will be called when the dropdown button is clicked
        if self.selected_row is not None:
            selected_transaction_id = self.reordered_table[self.selected_row][0]
            # Get the newly selected value from the dropdown
            selected_value = self.status_var.get()
            # print(selected_value)

            # Update the delivery status in the controller
            self.controller.update_transaction_status(selected_transaction_id, selected_value)

            # Update the status in the local table data
            self.reordered_table[self.selected_row][6] = selected_value

            # Update the specific cell in the table to reflect the new status
            self.update_status_cell(self.selected_row, selected_value)

            self.show_salesTable()
        else:
            print("No row selected.")

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
        if self.system_dialog is None:
            self.system_dialog = SystemDialog(self)
            self.system_dialog.grab_set()  # Make the SystemDialog modal
            self.system_dialog.protocol("WM_DELETE_WINDOW", self.on_systemDialog_close)
            self.wait_window(self.system_dialog)
            
    def on_systemDialog_close(self):
        self.system_dialog.destroy()
        self.system_dialog = None
    
    def generate_pdf_report(self):
        # Fetch data to be included in the report
        data = self.controller.get_data()

        # Ask user to select a directory
        directory = filedialog.askdirectory(title="Select Directory to Save PDF Report")
        
        if not directory:
            return

        # Define a fixed file name with timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        pdf_file = os.path.join(directory, f'sales_report_{timestamp}.pdf')
        
        # Generate PDF using ReportLab
        c = canvas.Canvas(pdf_file, pagesize=letter)
        width, height = letter

        # Set up the title and timestamp
        c.setFont("Helvetica-Bold", 16)
        c.drawString(36, height - 50, "Sales Report")
        c.setFont("Helvetica", 10)
        c.drawString(width - 140, height - 50, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        # Set up table headers
        headers = ['Order ID', 'Buyer', 'Contact #', 'Revenue', 'Date', 'Time', 'Status']
        col_widths = [60, 100, 100, 80, 80, 60, 60]  # Adjust widths as needed
        
        row_height = 20
        y_start = height - 100

        # Draw table headers
        c.setFont("Helvetica-Bold", 12)
        for i, header in enumerate(headers):
            c.drawString(36 + sum(col_widths[:i]), y_start, header)

        # Draw data rows
        c.setFont("Helvetica", 12)
        y = y_start - row_height
        for row_data in data:
            for i, col_value in enumerate(row_data):
                c.drawString(36 + sum(col_widths[:i]), y, str(col_value))
            y -= row_height

        # Save the PDF file
        c.save()
        print(f"PDF report generated successfully at: {pdf_file}")

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
        self.root.title("Maintenance Four Page (Test)")
        
        self.maintenancefour_view = maintenanceFourView(self.root, None)
        self.maintenancefour_view.pack(fill=ctk.BOTH, expand=True)
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()