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
        self.custom_styles()
        self.geometry("400x300+500+200") # TODO: dynamic resizing
        # self.minsize(400, 300)
        # self.maxsize(400, 300) 
        self._signup_Label()
        self.usernameFrame()
        self._username_Label()
        self._userName_entry()
        self.passwordFrame()
        self._password_Label()
        self._password_entry()
        self._signup_button()



    def main(self):
        self.mainloop()

    def mainframe(self):
        self.frame = ttk.Frame(self, borderwidth=1, relief='ridge')
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, relwidth=0.7, relheight=0.7)
    
    # Added custom fontstyles
    def custom_styles(self):
        self.style = ttk.Style()
        self.style.configure("Text.TLabel", font=('Consolas', 10))
        self.style.configure("Text.TButton", font=('Consolas', 10))
        
    # the methods / functions below are private, meaning it cant be accessed outside of this class
    def _signup_Label(self):
        self.signupLabel = ttk.Label(self.frame, text="Sign In", font=("Consolas", 12, 'bold'))
        self.signupLabel.pack(pady=(20,0))
        
    def usernameFrame(self): # Added separate frames to merge entry and label widgets
        self.usernameFrame = ttk.Frame(self.frame)
        self.usernameFrame.pack(pady=(20,0))
        
    def _userName_entry(self):
        self.usernameEntry = ttk.Entry(self.usernameFrame, textvariable=self.userName)
        self.usernameEntry.pack(side='left', padx=5, pady=5)

    def _username_Label(self):
        self.usernameLabel = ttk.Label(self.usernameFrame, text="Username", style="Text.TLabel")
        self.usernameLabel.pack(side='left', padx=5, pady=5)

    def passwordFrame(self):
        self.passwordFrame = ttk.Frame(self.frame)
        self.passwordFrame.pack(pady=(0,20))
        
    def _password_Label(self):
        self.passwordLabel = ttk.Label(self.passwordFrame, text="Password", style="Text.TLabel")
        self.passwordLabel.pack(side='left', padx=5, pady=5)

    def _password_entry(self):
        self.passwordEntry = ttk.Entry(self.passwordFrame, textvariable=self.password)
        self.passwordEntry.pack(side='left', padx=5, pady=5)

    def _signup_button(self):
        self.signupButton = ttk.Button(self.frame, text="Confirm", style="Text.TButton", command=self._on_signup_button_click)
        self.signupButton.pack(pady=(25,0))

    def _on_signup_button_click(self):
        username = self.userName.get()
        self.controller.on_button_click(username)

        password = self.password.get()
        self.controller.on_button_click(password)
