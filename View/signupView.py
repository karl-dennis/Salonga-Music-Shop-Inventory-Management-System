import tkinter as tk

class signupView(tk.Tk):

    PAD = 10

    def __init__(self, controller):
        
        super().__init__()
        self.controller = controller
        
        self.userName = tk.StringVar()
        
        self.title("Salonga Music Shop")

        self.mainframe()
        self.geometry('340x440')
        self._signup_Label()
        self._username_Label()
        self._userName_entry()
        self._password_Label()
        self._password_entry()
        self._signup_button()


    def main(self):
        self.mainloop()

    def mainframe(self):
        self.frame = tk.Frame(self)
        self.frame.grid()

    # this method / function is private, meaning it cant be accessed outside of this class

    def _signup_Label(self):
        self.signupLabel = tk.Label(self.frame, text="Sign Up")
        self.signupLabel.grid(row=0, column=0, columnspan=2)

    def _userName_entry(self):
        self.userNameEntry = tk.Entry(self.frame, textvariable=self.userName)
        self.userNameEntry.grid(row=1, column=1)

    def _username_Label(self):
        self.userNameLabel = tk.Label(self.frame, text="Username")
        self.userNameLabel.grid(row=1, column=0)

    def _password_Label(self):
        self.passwordLabel = tk.Label(self.frame, text="Password")
        self.passwordLabel.grid(row=2, column=0)

    def _password_entry(self):
        self.passwordEntry = tk.Entry(self.frame)
        self.passwordEntry.grid(row=2, column=1)

    def _signup_button(self):
        self.signupButton = tk.Button(self.frame, text="Sign Up")
        self.signupButton.grid(row=3, column=0, columnspan=2)
    