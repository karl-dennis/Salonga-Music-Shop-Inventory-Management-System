import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
from tkinter import ttk
from tkcalendar import DateEntry
from CTkTable import *
import shutil
import os
import datetime
from tkinter import filedialog

class maintenanceView(ctk.CTkFrame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(width=842, height=620, fg_color='#DFDFDF', corner_radius=0)
        ctk.set_appearance_mode("light")

        self.active_tab = 1
        self.search_query = ctk.StringVar()

        self.username_entry = ctk.StringVar()
        self.password_entry = ctk.StringVar()
        self.firstname_entry = ctk.StringVar()
        self.lastname_entry = ctk.StringVar()
        self.birthday_entry = ctk.StringVar()
        self.email_entry = ctk.StringVar()
        
        self.custom_styles()
        self.base_frame()

    def custom_styles(self):
        pass

    def base_frame(self):    
        self.baseFrame = ctk.CTkFrame(self, width=842, height=620, fg_color='#DFDFDF', corner_radius=0)
        self.baseFrame.place(x=0, y=0)
        
        self.place(x=0, y=0) # Place productView Frame, do not change this

        self.show_maintenanceOne()
        self.show_manageAcc()
        self._toggle_password_button()
        self.show_accountsTable()
        
    def show_maintenanceOne(self):
        self.maintenanceOneFrame = ctk.CTkFrame(self.baseFrame, width=820, height=51, fg_color='#F7F7F7', corner_radius=7)
        self.maintenanceOneFrame.place(x=11, y=15)
            
        self.tabFrame = ctk.CTkFrame(self.maintenanceOneFrame, width=820, height=51, bg_color='#DFDFDF', fg_color='#F7F7F7', corner_radius=7)
        self.tabFrame.place(x=0, y=0)
        
        self.selection1 = ctk.CTkButton(self.tabFrame, width=115, height=18, text='Manage Users',
                                        font=('Inter', 13, 'bold'), text_color='#2E2E2E',
                                        fg_color='#F7F7F7', hover_color='#F7F7F7')
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
                                        font=('Inter', 13, 'bold'), text_color='#9A9A9A',
                                        fg_color='#F7F7F7', hover_color='#F7F7F7', command=lambda: self.controller.set_active_tab(4))
        self.selection4.place(x=402, y=14)

        self.selection5 = ctk.CTkButton(self.tabFrame, width=115, height=18, text='Backup & Restore',
                                        font=('Inter', 13, 'bold'), text_color='#9A9A9A',
                                        fg_color='#F7F7F7', hover_color='#F7F7F7', command=self.show_systemDialog)
        self.selection5.place(x=533, y=14)
        
        self.system_dialog = None
        
        self.tabLine = ctk.CTkFrame(self.tabFrame, width=78, height=4, fg_color='#5089B5', corner_radius=7)
        self.tabLine.place(x=28, y=39)

    def show_manageAcc(self):
        self.manageAccFrame = ctk.CTkFrame(self.baseFrame, width=210, height=526, fg_color='#F7F7F7', corner_radius=7)
        self.manageAccFrame.place(x=11, y=79)

        self.label = ctk.CTkLabel(self.manageAccFrame, text="Manage Users", font=('Inter Medium', 13), text_color='#2E2E2E')
        self.label.place(x=14, y=7)
        
        self.usernameFrame = ctk.CTkFrame(self.manageAccFrame, width=160, height=56, fg_color='transparent')
        self.usernameFrame.place(x=25, y=39)
        
        self.usernameLabel = ctk.CTkLabel(self.usernameFrame, text='Username', font=('Inter Medium', 12), text_color='#595959',
                                       width=106, height=26, bg_color='transparent', anchor='w')
        self.usernameLabel.place(x=5, y=0)
        
        self.usernameEntry = ctk.CTkEntry(self.usernameFrame, width=160, height=30, corner_radius=7, 
                                       bg_color='transparent', fg_color='#FAFAFA',
                                       border_color='#CACACA', border_width=2,
                                       font=('Inter Medium', 12), text_color='#595959', textvariable=self.username_entry)
        self.usernameEntry.place(x=0, y=26)

        self.passwordFrame = ctk.CTkFrame(self.manageAccFrame, width=160, height=56, fg_color='transparent')
        self.passwordFrame.place(x=25, y=98)
        
        self.passwordLabel = ctk.CTkLabel(self.passwordFrame, text='Password', font=('Inter Medium', 12), text_color='#595959',
                                       width=106, height=26, bg_color='transparent', anchor='w')
        self.passwordLabel.place(x=5, y=0)
        
        self.passwordEntry = ctk.CTkEntry(self.passwordFrame, width=160, height=30, corner_radius=7, 
                                       bg_color='transparent', fg_color='#FAFAFA',
                                       border_color='#CACACA', border_width=2,
                                       font=('Inter Medium', 12), text_color='#595959', textvariable=self.password_entry,
                                       show='*')
        self.passwordEntry.place(x=0, y=26)

        self.firstnameFrame = ctk.CTkFrame(self.manageAccFrame, width=160, height=56, fg_color='transparent')
        self.firstnameFrame.place(x=25, y=157)
        
        self.firstnameLabel = ctk.CTkLabel(self.firstnameFrame, text='First Name', font=('Inter Medium', 12), text_color='#595959',
                                       width=106, height=26, bg_color='transparent', anchor='w')
        self.firstnameLabel.place(x=5, y=0)
        
        self.firstnameEntry = ctk.CTkEntry(self.firstnameFrame, width=160, height=30, corner_radius=7, 
                                       bg_color='transparent', fg_color='#FAFAFA',
                                       border_color='#CACACA', border_width=2,
                                       font=('Inter Medium', 12), text_color='#595959', textvariable=self.firstname_entry)
        self.firstnameEntry.place(x=0, y=26)
        
        self.lastnameFrame = ctk.CTkFrame(self.manageAccFrame, width=160, height=56, fg_color='transparent')
        self.lastnameFrame.place(x=25, y=216)
        
        self.lastnameLabel = ctk.CTkLabel(self.lastnameFrame, text='Last Name', font=('Inter Medium', 12), text_color='#595959',
                                       width=106, height=26, bg_color='transparent', anchor='w')
        self.lastnameLabel.place(x=5, y=0)
        
        self.lastnameEntry = ctk.CTkEntry(self.lastnameFrame, width=160, height=30, corner_radius=7, 
                                       bg_color='transparent', fg_color='#FAFAFA',
                                       border_color='#CACACA', border_width=2,
                                       font=('Inter Medium', 12), text_color='#595959', textvariable=self.lastname_entry)
        self.lastnameEntry.place(x=0, y=26)
        
        self.birthdateFrame = ctk.CTkFrame(self.manageAccFrame, width=160, height=56, fg_color='transparent')
        self.birthdateFrame.place(x=25, y=275)
        
        self.birthdateLabel = ctk.CTkLabel(self.birthdateFrame, text='Birthdate', font=('Inter Medium', 12), text_color='#595959',
                                       width=106, height=26, bg_color='transparent', anchor='w')
        self.birthdateLabel.place(x=5, y=0)
        
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("CalendarButton.TButton")
        
        self.birthdateEntry = DateEntry(self.birthdateFrame, font=("Inter", 13),
                                     firstweekday='sunday', showweeknumbers=True,
                                     background='#F7F7F7', foreground='#393939',
                                     headersbackground='#92A3AA', headersforeground='#FFFFFF',
                                     selectbackground='#5089B5', selectforeground='#FFFFFF',
                                     normalbackground='#FFFFFF', normalforeground='#6D6D6D',
                                     weekendbackground='#FFFFFF', weekendforeground='#6D6D6D',
                                     othermonthbackground='#E6E6E6', othermonthforeground='#BFBFBF',
                                     othermonthwebackground='#E6E6E6', othermonthweforeground='#BFBFBF',
                                     bordercolor='#92A3AA', width=130, height=97,
                                     style="CalendarButton.TButton", textvariable=self.birthday_entry)
        self.birthdateEntry.place(x=0, y=26)
        
        self.emailFrame = ctk.CTkFrame(self.manageAccFrame, width=160, height=56, fg_color='transparent')
        self.emailFrame.place(x=25, y=334)
        
        self.emailLabel = ctk.CTkLabel(self.emailFrame, text='Email', font=('Inter Medium', 12), text_color='#595959',
                                       width=106, height=26, bg_color='transparent', anchor='w')
        self.emailLabel.place(x=5, y=0)
        
        self.emailEntry = ctk.CTkEntry(self.emailFrame, width=160, height=30, corner_radius=7, 
                                       bg_color='transparent', fg_color='#FAFAFA',
                                       border_color='#CACACA', border_width=2,
                                       font=('Inter Medium', 12), text_color='#595959', textvariable=self.email_entry)
        self.emailEntry.place(x=0, y=26)
        
        
        self.loaFrame = ctk.CTkFrame(self.manageAccFrame, width=160, height=56, fg_color='transparent')
        self.loaFrame.place(x=25, y=393)
        
        self.loaLabel = ctk.CTkLabel(self.loaFrame, text='Level of Access', font=('Inter Medium', 12), text_color='#595959',
                                          width=106, height=26, bg_color='transparent', anchor='w')
        self.loaLabel.place(x=5, y=0)
        
        self.loaDropdown = ctk.CTkComboBox(self.loaFrame, 
                                            values=['Admin', 'Employee'], # Insert values here
                                            width=160, height=30, corner_radius=7,
                                            bg_color='transparent', fg_color='#FAFAFA',
                                            border_color='#CACACA', border_width=2, state='readonly', 
                                            font=('Inter Medium', 12), text_color='#595959',
                                            dropdown_font=('Inter Medium', 12), dropdown_text_color='#595959', 
                                            dropdown_fg_color='#FAFAFA', dropdown_hover_color='#e4e4e4',
                                            button_color='#CACACA',)
        self.loaDropdown.set('Select')
        self.loaDropdown.place(x=0, y=26)
        
        self.buttonFrame = ctk.CTkFrame(self.manageAccFrame, width=160, height=28, bg_color='transparent', fg_color='transparent')
        self.buttonFrame.place(x=25, y=476)    
        
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
    
    def show_accountsTable(self):
        self.accountsTableFrame = ctk.CTkFrame(self.baseFrame, width=596, height=526, corner_radius=7,
                                               fg_color='#F7F7F7', bg_color='#DFDFDF')
        self.accountsTableFrame.place(x=235, y=79)

        self.label = ctk.CTkLabel(self.accountsTableFrame, text="Accounts", font=('Inter Medium', 13), text_color='#2E2E2E')
        self.label.place(x=14, y=7)
        
        self.table_values = self.controller.get_employees_with_accounts()
        """ [employeeID, username, firstName, lastName, birthdate, email, LOA, status] """
        # table_values = [
        #     ['A0001', 'seris', 'Karl', 'Rodriguez', '10/20/02', 'abcdefghij@tip.edu.ph', 'Admin', 'Active'],
        #     ['E0001', 'kurt', 'Fritz', 'Gonzales', '11/21/02', 'klmnopqrstu@tip.edu.ph', 'Employee', 'Inactive'],
        # ]
        
        self.reordered_table = []
        
        for row_values in self.table_values:
            fullname = row_values[2] + ' ' + row_values[3]
            reordered_row_values = [row_values[0], row_values[1], fullname, row_values[4], row_values[5], row_values[6], row_values[7]]
            self.reordered_table.append(reordered_row_values)
        
        # firstName + lastName = Full Name
        column_titles = ['Employee ID', 'Username', 'Full Name', 'Birthdate', 'Email', 'LOA', 'Status']
        column_widths = [90, 82, 96, 70, 93, 76, 60] # Table Width = 567
        
        column_frame = ctk.CTkFrame(self.accountsTableFrame, width=567, height=25, fg_color='#F7F7F7',
                                    bg_color='#DFDFDF', corner_radius=0)
        column_frame.place(x=17, y=26)
        
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
            self.columnLabel.place(x=0 + x_position, y=3)
            x_position += width
        
        columnLine = ctk.CTkFrame(self.accountsTableFrame, width=596, height=2, fg_color='#dbdbdb')
        columnLine.place(x=0, y=53)
        
        """ Table Rows """
        self.tableFrame = ctk.CTkScrollableFrame(self.accountsTableFrame, width=567, height=469, fg_color='#F7F7F7', corner_radius=0)
        self.tableFrame.place(x=14, y=55)
        
        self.table = CTkTable(master=self.tableFrame, column=6, padx=0, pady=0, font=('Inter Medium', 10), text_color='#747474',
                              colors=['#F7F7F7', '#F7F7F7'])
        
        if not self.reordered_table:
            required_rows = 0
        else:
            required_rows= len(self.reordered_table)
        
        current_rows = self.table.rows
        for _ in range(required_rows - current_rows):
            self.table.add_row([''] * 6)
        
        for row_index, row_values in enumerate(self.reordered_table):
            self.table.insert(row_index, 0, row_values[0])
            self.table.insert(row_index, 1, row_values[1])
            self.table.insert(row_index, 2, row_values[2])
            self.table.insert(row_index, 3, row_values[3])
            self.table.insert(row_index, 4, row_values[4])
            self.table.insert(row_index, 5, row_values[5])

        
        
        cell_widths = [90, 82, 96, 70, 93, 76] # Table Width = 507
        for row in range(self.table.rows):                
            for column in range(self.table.columns):
                self.table.frame[row, column].configure(width=cell_widths[column], height=25,
                                                        fg_color='#F7F7F7', text_color='#868686',
                                                        corner_radius=0, anchor='w')

                # self.table.frame[row, 6].configure(text_color=status_color, font=('Inter Medium', 8)) # Status
                self.table.frame[row, 4].configure(font=('Inter Medium', 6)) # Email

        self.table.pack(fill='y', expand=True, anchor='w')

        self.selected_row = None
        self.bind_cell_click_events()
        
        for row in range(1, self.table.rows + 1):
            rowLine = ctk.CTkFrame(self.tableFrame, width=567, height=2, fg_color='#dbdbdb')
            rowLine.place(x=0, y=(row) * 25 - 1)
            
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
                                                width=60, height=13,
                                                font=('Inter Semibold', 8),
                                                corner_radius=8,
                                                variable=status_var)
            status_dropdown.place(x=510, y=5 + (row * 25))

            status_var.trace_add('write', lambda *args, sv=status_var, sd=status_dropdown: self.update_status_dropdown_colors(sv, sd))
            self.update_status_dropdown_colors(status_var, status_dropdown)

            self.status_vars.append(status_var)
            self.status_dropdowns.append(status_dropdown)

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
        self.id = self.table_values[row][0]
        # self.username_entry.set(value=self.reordered_table[row][1])
        self.username_entry.set(value=self.table_values[row][1])
        self.passwordEntry.configure(state='disabled')
        self.firstname_entry.set(value=self.table_values[row][2])
        self.lastname_entry.set(value=self.table_values[row][3])
        self.birthday_entry.set(value=self.table_values[row][4])
        self.email_entry.set(value=self.table_values[row][5])
        self.loaDropdown.set(value=self.table_values[row][6])

    def deselect_row(self, row):
        self.table.edit_row(row, fg_color='#F7F7F7')
        print(f"Deselected row {row}: {self.reordered_table[row]}")

        self.username_entry.set(value='')
        self.passwordEntry.configure(state='normal')
        self.password_entry.set(value='')
        self.firstname_entry.set(value='')
        self.lastname_entry.set(value='')
        self.birthday_entry.set(value='')
        self.email_entry.set(value='')
        self.loaDropdown.set(value='')
        
    def update_status_dropdown_colors(self, status_var, status_dropdown):
        status = status_var.get()
        colors = self.status_colors.get(status, self.status_colors['Active'])

        status_dropdown.configure(text_color=colors['text_color'],
                                button_color=colors['button_color'],
                                fg_color=colors['fg_color'],
                                button_hover_color=colors['button_hover_color'])

    
    def _toggle_password_button(self):
        self.eye_open = ctk.CTkImage(light_image=Image.open('./assets/eye-open.png'), size=(15, 15))
        self.eye_closed = ctk.CTkImage(light_image=Image.open('./assets/eye-closed.png'), size=(15, 15))

        self.toggle_button = ctk.CTkButton(self.passwordEntry, image=self.eye_closed, text='',
                                           width=15, height=15, fg_color='#FAFAFA', hover_color='#FAFAFA', corner_radius=0, border_width=0,
                                           command=self._toggle_password_visibility)
        self.toggle_button.place(x=132, y=3)

        self.show_password = False 
    
    def _toggle_password_visibility(self):
        if self.show_password:
            self.passwordEntry.configure(show='*')
            self.toggle_button.configure(image=self.eye_closed)
        else:
            self.passwordEntry.configure(show='')
            self.toggle_button.configure(image=self.eye_open)

        self.show_password = not self.show_password
        
    def clear_base_frame(self):
        for widget in self.baseFrame.winfo_children():
            widget.destroy()

    def clear_form(self):
        self.usernameEntry.delete(0, 'end')
        self.loaDropdown.set('Select')

    def save_button_clicked(self):
        if self.selected_row is not None:
            id = self.id
            username = self.username_entry.get()
            # password = self.password_entry.get()
            first_name = self.firstname_entry.get()
            last_name = self.lastname_entry.get()
            birthdate = self.birthday_entry.get()
            email = self.email_entry.get()
            loa = self.loaDropdown.get()

            # Assuming you want to update the selected row with the new data
            # self.reordered_table[self.selected_row] = [id, username, f"{first_name} {last_name}", birthdate, email,
            #                                            loa, 'Active']

            self.clear_form()
            self.deselect_row(self.selected_row)  # Deselect the row after saving

            # Assuming you have a method in the controller to handle saving
            self.controller.update(id,username, first_name, last_name, birthdate, email, loa)
            self.show_accountsTable()
        else:
            username = self.username_entry.get()
            password = self.password_entry.get()
            first_name = self.firstname_entry.get()
            last_name = self.lastname_entry.get()
            birthdate = self.birthday_entry.get()
            email = self.email_entry.get()
            loa = self.loaDropdown.get()
            self.controller.save_button_clicked(username, password, first_name, last_name, birthdate, email, loa)
            self.clear_form()
            self.show_accountsTable()
    # def save_button_clicked(self):
    #     username = self.username_entry.get()
    #     password = self.password_entry.get()
    #     first_name = self.firstname_entry.get()
    #     last_name = self.lastname_entry.get()
    #     birthdate = self.birthday_entry.get()
    #     email = self.email_entry.get()
    #     loa = self.loaDropdown.get()
    #     self.controller.save_button_clicked(username, password, first_name, last_name, birthdate, email, loa)
    #     self.clear_form()
    #
    #     self.show_accountsTable()
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