import customtkinter as ctk
import tkinter as tk

class verifyEmailView(ctk.CTk):

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
        self._text_box()
        self._email_frame()
        self._email_label()
        self._email_entry()
        self._otp_frame()
        self._otp_label()
        self._otp_entry()
        self._otp_button()
        self._button_frame()
        self._return_button()
        self._verify_button()
    
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
        self.signupLabel = ctk.CTkLabel(self.topFrame, text="Reset Password", bg_color='transparent',
                                        font=("Consolas", 27, 'bold'), anchor='center')
        self.signupLabel.place(x=178, y=22) 
        
    def _text_box(self):
        self.signupLabel = ctk.CTkLabel(self.formFrame, text="Enter your email to receive a\nverification code.",
                                        bg_color='transparent', font=("Consolas", 16), text_color='#535353', width=310, height=40)
        self.signupLabel.pack(pady=(10,0))
      
    def _email_frame(self):
        self.emailFrame = ctk.CTkFrame(self.formFrame, border_width=0, bg_color='transparent', fg_color='transparent')
        self.emailFrame.pack(pady=(10,0))

    def _email_entry(self):
        self.emailEntry = ctk.CTkEntry(self.emailFrame, width=360, height=48, font=("Consolas", 20), border_color='#999999', text_color='#595959', textvariable=self.userName, border_width=2)
        self.emailEntry.pack(side='top', padx=5, pady=5)

    def _email_label(self):
        self.emailLabel = ctk.CTkLabel(self.emailFrame, text="Email Address", font=("Consolas", 18), text_color='#595959')
        self.emailLabel.pack(side='top', anchor='w', padx=5)

    def _otp_frame(self):
        self.otpFrame = ctk.CTkFrame(self.formFrame, border_width=0, bg_color='transparent', fg_color='transparent')
        self.otpFrame.pack(pady=(10,10))

    def _otp_entry(self):
        self.otpEntry = ctk.CTkEntry(self.otpFrame, width=360, height=48, font=("Consolas", 20), border_color='#999999', text_color='#595959', textvariable=self.password, border_width=2)
        self.otpEntry.pack(side='top', padx=5, pady=5)
        
    def _otp_label(self):
        self.otpLabel = ctk.CTkLabel(self.otpFrame, text="One-Time Pin", font=("Consolas", 18), text_color='#595959')
        self.otpLabel.pack(side='top', anchor='w', padx=5)
    
    def _otp_button(self):
        self.confirmButton = ctk.CTkButton(self.formFrame, width=94, height=28, bg_color='transparent', fg_color='#EBEBEB', hover_color='#e0e0e0', 
                                           corner_radius=16, border_width=2, border_color='#B5B5B5',
                                           text="Send OTP", font=("Consolas", 12), text_color='#595959', command=self._on_confirm_button_click)
        self.confirmButton.place(x=260, y=200)
    
    def _button_frame(self):
        self.buttonFrame = ctk.CTkFrame(self.bottomFrame, width=568, height=80, fg_color="#F0F0F0", border_width=2, corner_radius=0)
        self.buttonFrame.pack_propagate(0)
        self.buttonFrame.pack(side='left', anchor='s')

    def _return_button(self):
        self.confirmButton = ctk.CTkButton(self.buttonFrame, width=174, height=46, fg_color='#E2E2E2', hover_color='#d5d5d5', corner_radius=16,
                                           text="Return", font=("Consolas", 21), text_color='#595959', command=self._on_confirm_button_click)
        self.confirmButton.place(x=95, y=16)
    
    def _verify_button(self):
        self.confirmButton = ctk.CTkButton(self.buttonFrame, width=174, height=46, fg_color='#1FB2E7', hover_color='#2193BC', corner_radius=16,
                                           text="Verify", font=("Consolas", 21), text_color='#F7F7F7', command=self._on_confirm_button_click)
        self.confirmButton.place(x=300, y=16)
                
    def _on_confirm_button_click(self):
        username = self.userName.get()
        password = self.password.get()
        self.controller.on_button_click(username, password)

    def _signup_button_clicked(self):
        self.controller.switch_to_signup()

