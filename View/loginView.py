import tkinter as tk
from tkinter import ttk

class loginView(tk.Tk):

    PAD = 10

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.userName = tk.StringVar()
        self.password = tk.StringVar()
        self.title("Salonga Music Shop")
        

        self.mainframe() # Main/Root Frame
        self.set_window() 
        self.custom_styles()
        self._top_label() # Top Bar + Heading
        self._form_frame() 
        self._bottom_frame()
        
        self._username_frame()
        self._username_label()
        self._userName_entry()
        # self._password_frame()
        # self._password_label()
        # self._password_entry()
        self._button_frame()
        self._signup_button()
        self._confirm_button()
    

    def main(self):
        self.mainloop()

    def set_window(self):
        set_width = 400
        set_height = 300
        x = int((self.winfo_screenwidth() / 2) - (set_width / 2))
        y = int((self.winfo_screenheight() / 2) - (set_height / 2))
        self.geometry(f'{set_width}x{set_height}+{x}+{y}')
        self.configure(bg='#FFFFFF')
        self.minsize(set_width, set_height)
        self.maxsize(set_width, set_height)

    def mainframe(self):
        self.frame = ttk.Frame(self, borderwidth=1, relief='solid')
        # self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, relwidth=0.7, relheight=0.7)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=280, height=210)
    
    def _top_label(self):
        self.signupLabel = ttk.Label(self.frame, text="Log In", font=("Consolas", 14, 'bold'), 
                                    relief='solid', borderwidth=1, anchor=tk.CENTER, background='#E9E9E9')
        self.signupLabel.place(width=280, height=37, x=-1, y=-1)
        # self.signupLabel.place(width=280, height=37)
    
    def _form_frame(self):
        self.formFrame = tk.Frame(self.frame, background="#F7F7F7")
        self.formFrame.place(relx=0.5, y=104, anchor=tk.CENTER, height=136, width=278)
    
    def _bottom_frame(self):
        self.bottomFrame = ttk.Frame(self, borderwidth=1, relief='solid')
        self.bottomFrame.place(relx=0.5, y=236, anchor=tk.CENTER, width=280, height=37)
    
    
    def custom_styles(self):
        self.style = ttk.Style()
        self.style.configure("Text.TLabel", font=('Consolas', 10))
        self.style.configure("Text.TButton", font=('Consolas', 10))

    

    
    
    
    def _username_frame(self):
        self.usernameFrame = ttk.Frame(self.formFrame)
        self.usernameFrame.pack(pady=(10, 0))

    def _userName_entry(self):
        self.usernameEntry = ttk.Entry(self.usernameFrame, textvariable=self.userName)
        self.usernameEntry.pack(side='left', padx=5, pady=5)

    def _username_label(self):
        self.usernameLabel = ttk.Label(self.usernameFrame, text="Username", style="Text.TLabel")
        self.usernameLabel.pack(side='left', padx=5, pady=5)

    def _password_frame(self):
        self.passwordFrame = ttk.Frame(self.frame)
        self.passwordFrame.pack()

    def _password_label(self):
        self.passwordLabel = ttk.Label(self.passwordFrame, text="Password", style="Text.TLabel")
        self.passwordLabel.pack(side='left', padx=5, pady=5)

    def _password_entry(self):
        self.passwordEntry = ttk.Entry(self.passwordFrame, textvariable=self.password, show='*')
        self.passwordEntry.pack(side='left', padx=5, pady=5)

    def _button_frame(self):
        self.buttonFrame = tk.Frame(self.bottomFrame, background="#F0F0F0")
        self.buttonFrame.pack()

    def _signup_button(self):
        self.signupButton = ttk.Button(self.buttonFrame, text="Sign Up", style="Text.TButton", command=self._signup_button_clicked)
        self.signupButton.pack(side='left', padx=5, pady=5)

    def _confirm_button(self):
        self.confirmButton = ttk.Button(self.buttonFrame, text="Confirm", style="Text.TButton", command=self._on_confirm_button_click)
        self.confirmButton.pack(side='left', padx=5, pady=5)

    def _on_confirm_button_click(self):
        username = self.userName.get()
        password = self.password.get()
        self.controller.on_button_click(username, password)

    def _signup_button_clicked(self):
        self.controller.switch_to_signup()
