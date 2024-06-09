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
        self._forgot_password()
        self._button_frame()
        self._confirm_button()
    
    def main(self):
        self.mainloop()

    def set_window(self):
        set_width = 1020
        set_height = 670
        x = int((self.winfo_screenwidth() / 2) - (set_width / 2))
        y = int((self.winfo_screenheight() / 2) - (set_height / 2))
        self.geometry(f'{set_width}x{set_height}+{x}+{y}')
        self.configure(fg_color='#FFFFFF')
        self.minsize(set_width, set_height)
        self.maxsize(set_width, set_height)

    def mainframe(self):
        self.frame = ctk.CTkFrame(self, width=568, height=466, fg_color='#F7F7F7', border_width=2) 
        self.frame.place(x=510, y=335, anchor='center')
            
    def _top_frame(self):
        self.topFrame = ctk.CTkFrame(self, width=568, height=82, fg_color='#E9E9E9', border_color="#B5B5B5", border_width=2, corner_radius=0)
        self.topFrame.place(x=510, y=143, anchor='center')
    
    def _form_frame(self):
        self.formFrame = ctk.CTkFrame(self, width=568, height=138, border_width=0, bg_color='#F7F7F7', fg_color='#F7F7F7')
        self.formFrame.place(x=510, y=320, anchor='center')
    
    def _bottom_frame(self):
        self.bottomFrame = ctk.CTkFrame(self, width=568, height=37, border_width=0, fg_color='transparent') 
        self.bottomFrame.place(x=510, y=528, anchor='center')
    
    
    def custom_styles(self):
        pass  
    
    def _top_label(self):
        self.signupLabel = ctk.CTkLabel(self.topFrame, text="Login", bg_color='transparent',
                                        font=("Consolas", 27, 'bold'), anchor='center')
        self.signupLabel.place(x=248, y=22) 
      
    def _username_frame(self):
        self.usernameFrame = ctk.CTkFrame(self.formFrame, border_width=0, bg_color='transparent', fg_color='transparent')
        self.usernameFrame.pack(pady=(10,0))

    def _userName_entry(self):
        self.usernameEntry = ctk.CTkEntry(self.usernameFrame, width=360, height=48, font=("Consolas", 20), border_color='#999999', textvariable=self.userName, border_width=2)
        self.usernameEntry.pack(side='top', padx=5, pady=5)

    def _username_label(self):
        self.usernameLabel = ctk.CTkLabel(self.usernameFrame, text="Username", font=("Consolas", 18))
        self.usernameLabel.pack(side='top', anchor='w', padx=5)

    def _password_frame(self):
        self.passwordFrame = ctk.CTkFrame(self.formFrame, border_width=0, bg_color='transparent', fg_color='transparent')
        self.passwordFrame.pack(pady=(20,0))

    def _password_entry(self):
        self.passwordEntry = ctk.CTkEntry(self.passwordFrame, width=360, height=48, font=("Consolas", 20), border_color='#999999', textvariable=self.password, show='*', border_width=2)
        self.passwordEntry.pack(side='top', padx=5, pady=5)
        
    def _password_label(self):
        self.passwordLabel = ctk.CTkLabel(self.passwordFrame, text="Password", font=("Consolas", 18))
        self.passwordLabel.pack(side='top', anchor='w', padx=5)
        
    def _forgot_password(self):
        self.forgotPassword = ctk.CTkButton(self.passwordFrame, text="Forgot Password", font=("Consolas", 14, 'underline'), 
                                            text_color="#535353", fg_color='transparent', hover_color='#F7F7F7', command=self.controller.forgot_pass)
        self.forgotPassword.pack(side='top', anchor='e')
    
    def _button_frame(self):
        self.buttonFrame = ctk.CTkFrame(self.bottomFrame, width=568, height=80, fg_color="#F0F0F0", border_width=2, corner_radius=0)
        self.buttonFrame.pack_propagate(0)
        self.buttonFrame.pack(side='left', anchor='s')

    def _confirm_button(self):
        self.confirmButton = ctk.CTkButton(self.buttonFrame, width=264, height=46, fg_color='#1FB2E7', hover_color='#2193BC', corner_radius=16,
                                           text="Confirm", font=("Consolas", 21), text_color='#F7F7F7', command=self._on_confirm_button_click)
        self.confirmButton.place(x=151, y=16)
                
    def _on_confirm_button_click(self):
        username = self.userName.get()
        password = self.password.get()
        self.controller.on_button_click(username, password)

    def _signup_button_clicked(self):
        self.controller.switch_to_signup()

