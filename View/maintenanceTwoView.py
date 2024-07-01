import customtkinter as ctk
from CTkTable import *
import shutil
import os
import datetime
from tkinter import filedialog
from PIL import Image

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

        self.place(x=0, y=0)  # Place productView Frame, do not change this

        self.show_maintenanceTwo()
        self.show_userLogsTable()

    def show_maintenanceTwo(self):
        self.maintenanceTwoFrame = ctk.CTkFrame(self.baseFrame, width=820, height=51, fg_color='#F7F7F7',
                                                corner_radius=7)
        self.maintenanceTwoFrame.place(x=11, y=15)

        self.tabFrame = ctk.CTkFrame(self.maintenanceTwoFrame, width=820, height=51, bg_color='#DFDFDF',
                                     fg_color='#F7F7F7', corner_radius=7)
        self.tabFrame.place(x=0, y=0)

        self.selection1 = ctk.CTkButton(self.tabFrame, width=115, height=18, text='Manage Users',
                                        font=('Inter', 13, 'bold'), text_color='#9A9A9A',
                                        fg_color='#F7F7F7', hover_color='#F7F7F7',
                                        command=lambda: self.controller.set_active_tab(1))
        self.selection1.place(x=9, y=14)

        self.selection2 = ctk.CTkButton(self.tabFrame, width=115, height=18, text='User Logs',
                                        font=('Inter', 13, 'bold'), text_color='#2E2E2E',
                                        fg_color='#F7F7F7', hover_color='#F7F7F7')
        self.selection2.place(x=140, y=14)

        self.selection3 = ctk.CTkButton(self.tabFrame, width=115, height=18, text='Manage Products',
                                        font=('Inter', 13, 'bold'), text_color='#9A9A9A',
                                        fg_color='#F7F7F7', hover_color='#F7F7F7',
                                        command=lambda: self.controller.set_active_tab(3))
        self.selection3.place(x=271, y=14)

        self.selection4 = ctk.CTkButton(self.tabFrame, width=115, height=18, text='Manage Sales',
                                        font=('Inter', 13, 'bold'), text_color='#9A9A9A',
                                        fg_color='#F7F7F7', hover_color='#F7F7F7',
                                        command=lambda: self.controller.set_active_tab(4))
        self.selection4.place(x=402, y=14)

        self.selection5 = ctk.CTkButton(self.tabFrame, width=115, height=18, text='Manage System',
                                        font=('Inter', 13, 'bold'), text_color='#9A9A9A',
                                        fg_color='#F7F7F7', hover_color='#F7F7F7', command=self.show_systemDialog)
        self.selection5.place(x=533, y=14)

        self.system_dialog = None
        
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
            action = f"{row_values[2]} logged in at {row_values[1]}"  # username logged in at timestamp
            reordered_row_values = [row_values[0], row_values[1], action, row_values[3], row_values[4]]
            self.reordered_table.append(reordered_row_values)

        column_titles = ['Date', 'Timestamp', 'Action', 'Employee ID', 'Status']
        column_widths = [165, 165, 165, 165, 120]  # Table Width = 780

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
        self.tableFrame = ctk.CTkScrollableFrame(self.userLogsTableFrame, width=780, height=496, fg_color='#F7F7F7',
                                                 corner_radius=0)
        self.tableFrame.place(x=23, y=30)

        self.table = CTkTable(master=self.tableFrame, column=5, padx=0, pady=0, font=('Inter Medium', 10),
                              text_color='#747474',
                              colors=['#F7F7F7', '#F7F7F7'])

        if not self.reordered_table:
            required_rows = 0
        else:
            required_rows = len(self.reordered_table)

        current_rows = self.table.rows
        for _ in range(required_rows - current_rows):
            self.table.add_row([''] * 5)

        for row_index, row_values in enumerate(self.reordered_table):
            self.table.insert(row_index, 0, row_values[0])
            self.table.insert(row_index, 1, row_values[1])
            self.table.insert(row_index, 2, row_values[2])
            self.table.insert(row_index, 3, row_values[3])
            self.table.insert(row_index, 4, row_values[4])

        cell_widths = [165, 165, 165, 165, 120]  # Table Width = 780
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

    def show_systemDialog(self):
        if self.system_dialog is None:
            self.system_dialog = SystemDialog(self)
            self.system_dialog.grab_set()  # Make the SystemDialog modal
            self.system_dialog.protocol("WM_DELETE_WINDOW", self.on_systemDialog_close)
            self.wait_window(self.system_dialog)
            
    def on_systemDialog_close(self):
        self.system_dialog.destroy()
        self.system_dialog = None
            
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
        self.root.title("Maintenance Two Page (Test)")

        self.maintenancetwo_view = maintenanceTwoView(self.root, None)
        self.maintenancetwo_view.pack(fill=ctk.BOTH, expand=True)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()