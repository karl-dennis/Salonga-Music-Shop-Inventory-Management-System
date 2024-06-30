import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
from tkinter import ttk
from tkcalendar import DateEntry
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
        
        
        self.price = ctk.StringVar()
        
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
            
    def show_maintenanceOne(self):
        self.maintenanceOneFrame = ctk.CTkFrame(self.baseFrame, width=820, height=51, fg_color='#F7F7F7', corner_radius=7)
        self.maintenanceOneFrame.place(x=11, y=15)
            
        self.tabFrame = ctk.CTkFrame(self.maintenanceOneFrame, width=820, height=51, fg_color='transparent')
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

        self.selection4 = ctk.CTkButton(self.tabFrame, width=115, height=18, text='System',
                                        font=('Inter', 13, 'bold'), text_color='#9A9A9A',
                                        fg_color='#F7F7F7', hover_color='#F7F7F7', command=lambda: self.controller.set_active_tab(4))
        self.selection4.place(x=402, y=14)

        self.tabLine = ctk.CTkFrame(self.tabFrame, width=78, height=4, fg_color='#5089B5', corner_radius=7)
        self.tabLine.place(x=28, y=39)

    def show_manageAcc(self):
        self.manageAccFrame = ctk.CTkFrame(self.baseFrame, width=210, height=526, fg_color='#F7F7F7', corner_radius=7)
        self.manageAccFrame.place(x=11, y=79)
       
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
        
        self.label = ctk.CTkLabel(self.manageAccFrame, text="Manage Users", font=('Inter Medium', 13), text_color='#2E2E2E')
        self.label.place(x=14, y=7)
    
    def show_accountsTable(self):
        pass
    
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
        self.typeDropdown.set('Select')
        self.quantityEntry.delete(0, 'end')
        self.priceEntry.delete(0, 'end')
    
    def save_button_clicked(self):
        product_name = self.username_entry.get()
        type = self.typeDropdown.get()
        brand = self.loaDropdown.get()
        quantity = self.quantity.get()
        price = self.price.get()
        image = self.image_data
        self.controller.save_button_clicked(product_name,type,brand,quantity,price,image)
        messagebox.showinfo('Success', 'Product Added Successfully')
        self.clear_form()

    
    
class App:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Maintenance Page (Test)")
        
        self.maintenance_view = maintenanceView(self.root, None)
        self.maintenance_view.pack(fill=ctk.BOTH, expand=True)
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()