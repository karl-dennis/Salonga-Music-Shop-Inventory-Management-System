import customtkinter as ctk
import tkinter as tk

class loginView(ctk.CTk):

    def __init__(self, controller):
        
        super().__init__()
        self.controller = controller
        self.userName = tk.StringVar()
        self.password = tk.StringVar()
        self.title("Salonga Music Shop")
        
        ctk.set_appearance_mode("light")
        self.set_window() 
        self.custom_styles()
        
        self.mainframe() # Main/Root Frame
        self._top_frame()
        self._form_frame() 
        self._bottom_frame()
        self._top_label() # Top Bar + Heading
        self._username_frame()
        self._username_label()
        self._userName_entry()
        self._password_frame()
        self._password_label()
        self._password_entry()
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
        self.configure(fg_color='#FFFFFF')
        self.minsize(set_width, set_height)
        self.maxsize(set_width, set_height)

    def mainframe(self):
        self.frame = ctk.CTkFrame(self, width=280, height=210, fg_color='#F7F7F7', border_width=2,) 
        self.frame.place(x=200, y=150, anchor='center')
            
    def _top_frame(self):
        self.topFrame = ctk.CTkFrame(self, width=277, height=37, bg_color='#E9E9E9', border_width=2, corner_radius=0)
        self.topFrame.place(x=200, y=66, anchor='center')
    
    def _form_frame(self):
        self.formFrame = ctk.CTkFrame(self.frame, width=280, height=138, border_width=0)
        self.formFrame.place(x=139, y=103, anchor='center')
    
    def _bottom_frame(self):
        self.bottomFrame = ctk.CTkFrame(self, width=280, height=37, border_width=0) 
        self.bottomFrame.place(x=200, y=230, anchor='center')
    
    
    def custom_styles(self):
        pass  
    
    def _top_label(self):
        self.signupLabel = ctk.CTkLabel(self.topFrame, text="Log In", width=280, height=37, bg_color='#E9E9E9',
                                        font=("Consolas", 14, 'bold'), anchor='center')
        self.signupLabel.place(x=-1, y=-1) 
    
    def _username_frame(self):
        self.usernameFrame = ctk.CTkFrame(self.formFrame, border_width=0, bg_color='#F7F7F7', fg_color='#F7F7F7')
        self.usernameFrame.pack()

    def _userName_entry(self):
        self.usernameEntry = ctk.CTkEntry(self.usernameFrame, textvariable=self.userName, border_width=2)
        self.usernameEntry.pack(side='left', padx=5, pady=5)

    def _username_label(self):
        self.usernameLabel = ctk.CTkLabel(self.usernameFrame, text="Username", font=("Consolas", 12))
        self.usernameLabel.pack(side='left', padx=5, pady=5)

    def _password_frame(self):
        self.passwordFrame = ctk.CTkFrame(self.formFrame, border_width=0, bg_color='#F7F7F7', fg_color='#F7F7F7')
        self.passwordFrame.pack()

    def _password_label(self):
        self.passwordLabel = ctk.CTkLabel(self.passwordFrame, text="Password", font=("Consolas", 12))
        self.passwordLabel.pack(side='left', padx=5, pady=5)

    def _password_entry(self):
        self.passwordEntry = ctk.CTkEntry(self.passwordFrame, textvariable=self.password, show='*', border_width=2)
        self.passwordEntry.pack(side='left', padx=5, pady=5)

    def _signup_button(self):
        self.signupButton = ctk.CTkButton(self.bottomFrame, width=74, height=21, fg_color='#E9E9E9', hover_color='#cdcdcd',
                                          text="Sign Up", font=("Consolas", 12), text_color='#595959', command=self._signup_button_clicked)
        self.signupButton.pack(side='left', padx=7, pady=5)

    def _confirm_button(self):
        self.confirmButton = ctk.CTkButton(self.bottomFrame, width=74, height=21, fg_color='#1FB2E7', hover_color='#2193BC',
                                           text="Confirm", font=("Consolas", 12), text_color='#F7F7F7', command=self._on_confirm_button_click)
        self.confirmButton.pack(side='left', padx=7, pady=5)
                
    def _on_confirm_button_click(self):
        username = self.userName.get()
        password = self.password.get()
        self.controller.on_button_click(username, password)

    def _signup_button_clicked(self):
        self.controller.switch_to_signup()

