import customtkinter as ctk
import tkinter as tk

class resetPassView(ctk.CTk):

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
        self._newPass_frame()
        self._newPass_label()
        self._newPass_entry()
        self._password_frame()
        self._password_label()
        self._password_entry()
        self._button_frame()
        self._return_button()
        self._save_button()
    
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
        self.signupLabel = ctk.CTkLabel(self.formFrame, text="Enter your new password!",
                                        bg_color='transparent', font=("Consolas", 16), text_color='#535353', width=310, height=40)
        self.signupLabel.pack(pady=(10,0))
      
    def _newPass_frame(self):
        self.newPassFrame = ctk.CTkFrame(self.formFrame, border_width=0, bg_color='transparent', fg_color='transparent')
        self.newPassFrame.pack(pady=(10,0))

    def _newPass_entry(self):
        self.newPassEntry = ctk.CTkEntry(self.newPassFrame, width=360, height=48, font=("Consolas", 20), border_color='#999999', text_color='#595959', textvariable=self.userName, border_width=2)
        self.newPassEntry.pack(side='top', padx=5, pady=5)

    def _newPass_label(self):
        self.newPassLabel = ctk.CTkLabel(self.newPassFrame, text="New Password", font=("Consolas", 18), text_color='#595959')
        self.newPassLabel.pack(side='top', anchor='w', padx=5)

    def _password_frame(self):
        self.passwordFrame = ctk.CTkFrame(self.formFrame, border_width=0, bg_color='transparent', fg_color='transparent')
        self.passwordFrame.pack(pady=(10,10))

    def _password_entry(self):
        self.passwordEntry = ctk.CTkEntry(self.passwordFrame, width=360, height=48, font=("Consolas", 20), border_color='#999999', text_color='#595959', textvariable=self.password, border_width=2)
        self.passwordEntry.pack(side='top', padx=5, pady=5)
        
    def _password_label(self):
        self.passwordLabel = ctk.CTkLabel(self.passwordFrame, text="Confirm Password", font=("Consolas", 18), text_color='#595959')
        self.passwordLabel.pack(side='top', anchor='w', padx=5)
    
    def _button_frame(self):
        self.buttonFrame = ctk.CTkFrame(self.bottomFrame, width=568, height=80, fg_color="#F0F0F0", border_width=2, corner_radius=0)
        self.buttonFrame.pack_propagate(0)
        self.buttonFrame.pack(side='left', anchor='s')

    def _return_button(self):
        self.confirmButton = ctk.CTkButton(self.buttonFrame, width=174, height=46, fg_color='#E2E2E2', hover_color='#d5d5d5', corner_radius=16,
                                           text="Return", font=("Consolas", 21), text_color='#595959', command=self.controller.show_verifyEmail)
        self.confirmButton.place(x=95, y=16)
    
    def _save_button(self):
        self.confirmButton = ctk.CTkButton(self.buttonFrame, width=174, height=46, fg_color='#1FB2E7', hover_color='#2193BC', corner_radius=16,
                                           text="Save", font=("Consolas", 21), text_color='#F7F7F7', command=self.controller.show_login)
        self.confirmButton.place(x=300, y=16)
                