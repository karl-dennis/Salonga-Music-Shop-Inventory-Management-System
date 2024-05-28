import tkinter as tk
from tkinter import ttk

class signupView(tk.Tk):

    PAD = 10

    def __init__(self, controller):
        
        super().__init__()
        self.controller = controller
        
        self.userName = tk.StringVar()
        self.password = tk.StringVar()
        
        self.title("Salonga Music Shop")
        
        self.mainframe()
        self.center_window()
        self.custom_styles()
        self._signup_label()
        self._username_frame()
        self._username_label()
        self._userName_entry()
        self._password_frame()
        self._password_label()
        self._password_entry()
        self._button_frame()
        self._back_button()
        self._confirm_button()


    def main(self):
        self.mainloop()

    def center_window(self): # Centers window relative to screen dimensions
        set_width = 400 # Change to desired values
        set_height = 300

        x = int((self.winfo_screenwidth() / 2) - (set_width / 2))
        y = int((self.winfo_screenheight() / 2) - (set_height / 2))

        self.geometry(f'{set_width}x{set_height}+{x}+{y}')
        self.minsize(set_width, set_height) # Locks the window dimensions
        self.maxsize(set_width, set_height) 
            
    def mainframe(self): # Renamed frame for frame switching
        self.signupFrame = ttk.Frame(self, borderwidth=1, relief='ridge')
        self.signupFrame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, relwidth=0.7, relheight=0.7)
    
    # Added custom fontstyles
    def custom_styles(self):
        self.style = ttk.Style()
        self.style.configure("Text.TLabel", font=('Consolas', 10))
        self.style.configure("Text.TButton", font=('Consolas', 10))
        
    # the methods / functions below are private, meaning it cant be accessed outside of this class
    def _signup_label(self):
        self.signupLabel = ttk.Label(self.signupFrame, text="Sign Up", font=("Consolas", 12, 'bold'))
        self.signupLabel.pack(pady=(20,10))
        
    def _username_frame(self): # Added separate frames to merge entry and label widgets
        self.usernameFrame = ttk.Frame(self.signupFrame)
        self.usernameFrame.pack(pady=(10,0))
        
    def _userName_entry(self):
        self.usernameEntry = ttk.Entry(self.usernameFrame, textvariable=self.userName)
        self.usernameEntry.pack(side='left', padx=5, pady=5)

    def _username_label(self):
        self.usernameLabel = ttk.Label(self.usernameFrame, text="Username", style="Text.TLabel")
        self.usernameLabel.pack(side='left', padx=5, pady=5)

    def _password_frame(self):
        self.passwordFrame = ttk.Frame(self.signupFrame)
        self.passwordFrame.pack()
        
    def _password_label(self):
        self.passwordLabel = ttk.Label(self.passwordFrame, text="Password", style="Text.TLabel")
        self.passwordLabel.pack(side='left', padx=5, pady=5)

    def _password_entry(self):
        self.passwordEntry = ttk.Entry(self.passwordFrame, textvariable=self.password)
        self.passwordEntry.pack(side='left', padx=5, pady=5)

    def _button_frame(self): # Frame for merging button widgets
        self.buttonFrame = ttk.Frame(self.signupFrame)
        self.buttonFrame.pack(pady=(20,0))
    
    def _back_button(self): # TODO: change window on click
        self.backButton = ttk.Button(self.buttonFrame, text="Back", style="Text.TButton")
        self.backButton.pack(side='left', padx=5, pady=5)
        
    def _confirm_button(self):
        self.confirmButton = ttk.Button(self.buttonFrame, text="Confirm", style="Text.TButton", command=self._on_confirm_button_click)
        self.confirmButton.pack(side='left', padx=5, pady=5)

    def _on_confirm_button_click(self):
        username = self.userName.get()
        password = self.password.get()
        self.controller.on_button_click(username, password)

