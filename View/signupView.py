import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
class signupView(tk.Tk):

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
        
        self.mainframe() # Main/Root Frame
        self.set_window() 
        self.custom_styles()
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
        self.configure(bg='#FFFFFF')
        self.minsize(set_width, set_height)
        self.maxsize(set_width, set_height)

    def mainframe(self):
        self.frame = ttk.Frame(self, borderwidth=1, relief='solid')
        self.frame.place(x=300, y=200, anchor=tk.CENTER, width=420, height=280)
        Shadow(self.frame, color='#888888', size=1.015, offset_y=4)
    
    def _top_label(self):
        self.signupLabel = ttk.Label(self.frame, text="Sign Up", font=("Consolas", 14, 'bold'), 
                                    relief='solid', borderwidth=1, anchor=tk.CENTER, background='#E9E9E9')
        self.signupLabel.place(width=420, height=52, x=-1, y=-1)

    def _form_frame(self):
        self.formFrame = ttk.Frame(self.frame, style='CustomForm.TFrame')
        self.formFrame.place(x=209, y=143, anchor=tk.CENTER, width=420, height=186)
        
    def _formrow1_frame(self):
        self.formRow1 = ttk.Frame(self.formFrame)
        self.formRow1.place(x=20, y=28)
    
    def _formrow2_frame(self):
        self.formRow2 = ttk.Frame(self.formFrame)
        self.formRow2.place(x=20, y=78)
    
    def _formrow3_frame(self):
        self.formRow3 = ttk.Frame(self.formFrame)
        self.formRow3.place(x=20, y=128)
    
    def _bottom_frame(self):
        self.bottomFrame = ttk.Frame(self.frame, borderwidth=1, relief='solid')
        self.bottomFrame.place(relx=0.5, y=257, anchor=tk.CENTER, width=420, height=44)
        
    def custom_styles(self):
        self.style = ttk.Style()
        self.style.configure("Text.TLabel", font=('Consolas', 10), background='#F7F7F7')
        self.style.configure("Custom.TButton", font=('Consolas', 10))
        self.style.configure("CustomForm.TFrame", background='#F7F7F7', 
                             borderwidth=1, relief='solid',
                             )
    
    def _username_frame(self):
        self.usernameFrame = ttk.Frame(self.formRow1, style='CustomForm.TFrame')
        self.usernameFrame.pack(side='left')

    def _username_entry(self):
        self.usernameEntry = ttk.Entry(self.usernameFrame, textvariable=self.userName, width=15)
        self.usernameEntry.insert(0, "Username")
        self.usernameEntry.pack(side='left', padx=5, pady=5)

    def _username_label(self):
        self.usernameLabel = ttk.Label(self.usernameFrame, text="Username", style="Text.TLabel", width=10)
        self.usernameLabel.pack(side='left', padx=5, pady=5)

    def _password_frame(self):
        self.passwordFrame = ttk.Frame(self.formRow1, style='CustomForm.TFrame')
        self.passwordFrame.pack(side='left')

    def _password_label(self):
        self.passwordLabel = ttk.Label(self.passwordFrame, text="Password", style="Text.TLabel", width=10)
        self.passwordLabel.pack(side='left', padx=5, pady=5)

    def _password_entry(self):
        self.passwordEntry = ttk.Entry(self.passwordFrame, textvariable=self.password, width=15, show='*')
        self.passwordEntry.pack(side='left', padx=5, pady=5)

    def _firstname_frame(self):
        self.firstNameFrame = ttk.Frame(self.formRow2, style='CustomForm.TFrame')
        self.firstNameFrame.pack(side='left')

    def _firstname_label(self):
        self.firstNameLabel = ttk.Label(self.firstNameFrame, text="First Name", style="Text.TLabel", width=10)
        self.firstNameLabel.pack(side='left', padx=5, pady=5)
        
    def _firstname_entry(self):
        self.firstNameEntry = ttk.Entry(self.firstNameFrame, textvariable=self.firstName, width=15)
        self.firstNameEntry.pack(side='left', padx=5, pady=5)

    def _lastname_frame(self):
        self.lastNameFrame = ttk.Frame(self.formRow2, style='CustomForm.TFrame')
        self.lastNameFrame.pack(side='left')

    def _lastname_label(self):
        self.lastNameLabel = ttk.Label(self.lastNameFrame, text="Last Name", style="Text.TLabel", width=10)
        self.lastNameLabel.pack(side='left', padx=5, pady=5)
        
    def _lastname_entry(self):
        self.lastNameEntry = ttk.Entry(self.lastNameFrame, textvariable=self.lastName, width=15)
        self.lastNameEntry.pack(side='left', padx=5, pady=5)
    
    def _birthday_frame(self): 
        self.birthdayFrame = ttk.Frame(self.formRow3, style='CustomForm.TFrame')
        self.birthdayFrame.pack(side='left')
    
    def _birthday_label(self):
        self.birthdayLabel = ttk.Label(self.birthdayFrame, text="Birthday", style="Text.TLabel", width=10)
        self.birthdayLabel.pack(side='left', padx=5, pady=5)
    
    def _birthday_entry(self): # TODO: implement tkcalendar instead of ttk.Entry
        # self.birthdayEntry = ttk.Entry(self.birthdayFrame, textvariable=self.birthday)
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
        self.emailFrame = ttk.Frame(self.formRow3, style='CustomForm.TFrame')
        self.emailFrame.pack(side='left')

    def _email_label(self):
        self.emailLabel = ttk.Label(self.emailFrame, text="Email", style="Text.TLabel", width=10)
        self.emailLabel.pack(side='left', padx=5, pady=5)
        
    def _email_entry(self):
        self.emailEntry = ttk.Entry(self.emailFrame, textvariable=self.email, width=15)
        self.emailEntry.pack(side='left', padx=5, pady=5)

    def _button_frame(self):
        self.buttonFrame = tk.Frame(self.bottomFrame, background="#F0F0F0")
        self.buttonFrame.pack(anchor='e')

    def _back_button(self):
        self.backButton = ttk.Button(self.buttonFrame, text="Back", style="Custom.TButton", command=self._back_button_clicked)
        self.backButton.pack(side='left', padx=5, pady=7)

    def _confirm_button(self):
        self.confirmButton = ttk.Button(self.buttonFrame, text="Confirm", style="Custom.TButton", command=self._on_confirm_button_click)
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