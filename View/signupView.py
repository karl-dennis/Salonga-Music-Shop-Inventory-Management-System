import customtkinter as ctk
import tkinter as tk
from tkcalendar import DateEntry
class signupView(ctk.CTk):

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.userName = tk.StringVar()
        self.password = tk.StringVar()
        self.firstName = tk.StringVar()
        self.lastName = tk.StringVar()
        self.birthday = tk.StringVar()
        self.email = tk.StringVar()
        self.title("Salonga Music Shop")
        
        ctk.set_appearance_mode("light")
        self.set_window() 
        self.custom_styles()

        self.mainframe() # Main/Root Frame
        self._top_label() # Top Bar + Heading
        self._form_frame() 
        self._formrow1_frame()
        self._formrow2_frame()
        self._formrow3_frame()       
        self._bottom_frame()
        
        self._username_frame()
        self._username_label()
        self._username_entry()
        self._password_frame()
        self._password_label()
        self._password_entry()
        
        self._firstname_frame()
        self._firstname_label()
        self._firstname_entry()
        self._lastname_frame()
        self._lastname_label()
        self._lastname_entry()
        
        self._birthday_frame()
        self._birthday_label()
        self._birthday_entry()
        self._email_frame()
        self._email_label()
        self._email_entry()
        
        self._button_frame()
        self._back_button()
        self._confirm_button()
        
    def main(self):
        self.mainloop()

    def set_window(self):
        set_width = 600
        set_height = 400
        x = int((self.winfo_screenwidth() / 2) - (set_width / 2))
        y = int((self.winfo_screenheight() / 2) - (set_height / 2))
        self.geometry(f'{set_width}x{set_height}+{x}+{y}')
        self.configure(fg_color='#FFFFFF')
        self.minsize(set_width, set_height)
        self.maxsize(set_width, set_height)

    def mainframe(self):
        self.frame = ctk.CTkFrame(self, border_width=1, width=420, height=280) 
        self.frame.place(x=300, y=200, anchor='center')
    
    def _top_label(self):
        self.signupLabel = ctk.CTkLabel(self.frame, text="Sign Up", font=("Consolas", 14, 'bold'), 
                                    anchor='center', bg_color='#E9E9E9',
                                    width=420, height=52)
        self.signupLabel.place(x=-1, y=-1)

    def _form_frame(self):
        self.formFrame = ctk.CTkFrame(self.frame, width=420, height=186)
        self.formFrame.place(x=209, y=143, anchor='center')
        
    def _formrow1_frame(self):
        self.formRow1 = ctk.CTkFrame(self.formFrame)
        self.formRow1.place(x=20, y=28)
    
    def _formrow2_frame(self):
        self.formRow2 = ctk.CTkFrame(self.formFrame)
        self.formRow2.place(x=20, y=78)
    
    def _formrow3_frame(self):
        self.formRow3 = ctk.CTkFrame(self.formFrame)
        self.formRow3.place(x=20, y=128)
    
    def _bottom_frame(self):
        self.bottomFrame = ctk.CTkFrame(self.frame, border_width=1, width=420, height=44)
        self.bottomFrame.place(relx=0.5, y=257, anchor='center')
        
    def custom_styles(self):
        pass
    
    def _username_frame(self):
        self.usernameFrame = ctk.CTkFrame(self.formRow1)
        self.usernameFrame.pack(side='left')

    def _username_entry(self):
        self.usernameEntry = ctk.CTkEntry(self.usernameFrame, textvariable=self.userName, width=15)
        self.usernameEntry.insert(0, "Username")
        self.usernameEntry.pack(side='left', padx=5, pady=5)

    def _username_label(self):
        self.usernameLabel = ctk.CTkLabel(self.usernameFrame, text="Username", width=10)
        self.usernameLabel.pack(side='left', padx=5, pady=5)

    def _password_frame(self):
        self.passwordFrame = ctk.CTkFrame(self.formRow1)
        self.passwordFrame.pack(side='left')

    def _password_label(self):
        self.passwordLabel = ctk.CTkLabel(self.passwordFrame, text="Password", width=10)
        self.passwordLabel.pack(side='left', padx=5, pady=5)

    def _password_entry(self):
        self.passwordEntry = ctk.CTkEntry(self.passwordFrame, textvariable=self.password, width=15, show='*')
        self.passwordEntry.pack(side='left', padx=5, pady=5)

    def _firstname_frame(self):
        self.firstNameFrame = ctk.CTkFrame(self.formRow2)
        self.firstNameFrame.pack(side='left')

    def _firstname_label(self):
        self.firstNameLabel = ctk.CTkLabel(self.firstNameFrame, text="First Name", width=10)
        self.firstNameLabel.pack(side='left', padx=5, pady=5)
        
    def _firstname_entry(self):
        self.firstNameEntry = ctk.CTkEntry(self.firstNameFrame, textvariable=self.firstName, width=15)
        self.firstNameEntry.pack(side='left', padx=5, pady=5)

    def _lastname_frame(self):
        self.lastNameFrame = ctk.CTkFrame(self.formRow2)
        self.lastNameFrame.pack(side='left')

    def _lastname_label(self):
        self.lastNameLabel = ctk.CTkLabel(self.lastNameFrame, text="Last Name", width=10)
        self.lastNameLabel.pack(side='left', padx=5, pady=5)
        
    def _lastname_entry(self):
        self.lastNameEntry = ctk.CTkEntry(self.lastNameFrame, textvariable=self.lastName, width=15)
        self.lastNameEntry.pack(side='left', padx=5, pady=5)
    
    def _birthday_frame(self): 
        self.birthdayFrame = ctk.CTkFrame(self.formRow3)
        self.birthdayFrame.pack(side='left')
    
    def _birthday_label(self):
        self.birthdayLabel = ctk.CTkLabel(self.birthdayFrame, text="Birthday", width=10)
        self.birthdayLabel.pack(side='left', padx=5, pady=5)
    
    def _birthday_entry(self): # TODO: implement tkcalendar instead of ctk.CTkEntry
        # self.birthdayEntry = ctk.CTkEntry(self.birthdayFrame, textvariable=self.birthday)
        # self.birthdayEntry.pack(side='left', padx=5, pady=5)
        self.calendarEntry = DateEntry(self.birthdayFrame, textvariable=self.birthday, 
                                       firstweekday='sunday', showweeknumbers=False,
                                       background='#F7F7F7', foreground='#393939', 
                                       headersbackground='#92A3AA', headersforeground='#FFFFFF',
                                       selectbackground='#5089B5', selectforeground='#FFFFFF',
                                       normalbackground='#FFFFFF', normalforeground='#6D6D6D',
                                       weekendbackground='#FFFFFF', weekendforeground='#6D6D6D',
                                       othermonthbackground='#E6E6E6', othermonthforeground='#BFBFBF',
                                       othermonthwebackground='#E6E6E6', othermonthweforeground='#BFBFBF',
                                       bordercolor='#92A3AA', 
                                       )
        self.calendarEntry.pack(side='left', padx=5, pady=5)

    def _email_frame(self): 
        self.emailFrame = ctk.CTkFrame(self.formRow3)
        self.emailFrame.pack(side='left')

    def _email_label(self):
        self.emailLabel = ctk.CTkLabel(self.emailFrame, text="Email", width=10)
        self.emailLabel.pack(side='left', padx=5, pady=5)
        
    def _email_entry(self):
        self.emailEntry = ctk.CTkEntry(self.emailFrame, textvariable=self.email, width=15)
        self.emailEntry.pack(side='left', padx=5, pady=5)

    def _button_frame(self):
        self.buttonFrame = ctk.CTkFrame(self.bottomFrame, fg_color="#F0F0F0")
        self.buttonFrame.pack(anchor='e')

    def _back_button(self):
        self.backButton = ctk.CTkButton(self.buttonFrame, text="Back", command=self._back_button_clicked)
        self.backButton.pack(side='left', padx=5, pady=7)

    def _confirm_button(self):
        self.confirmButton = ctk.CTkButton(self.buttonFrame, text="Confirm", command=self._on_confirm_button_click)
        self.confirmButton.pack(side='left', padx=(5,10), pady=7)

    def _on_confirm_button_click(self):
        username = self.userName.get()
        password = self.password.get()
        firstName = self.firstName.get()
        lastname = self.lastName.get()
        birthday = self.birthday.get()
        email = self.email.get()

        self.controller.on_button_click(username, password, firstName, lastname, birthday, email)

    def _back_button_clicked(self):
        self.controller.back_button_on_click()

    def _login_button_clicked(self):
        self.controller.switch_to_login()