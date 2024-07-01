import customtkinter as ctk

class FAQSection(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(fg_color='#DFDFDF')
        ctk.set_appearance_mode('light')
        
        # Scrollable Frame
        self.scrollable_frame = ctk.CTkScrollableFrame(self, fg_color='#DFDFDF', corner_radius=0)
        self.scrollable_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # FAQ Title
        self.faq_title = ctk.CTkLabel(self.scrollable_frame, text="Frequently Asked Questions", font=("Inter", 16, "bold"), fg_color="#DFDFDF")
        self.faq_title.pack(pady=10)
        
        # FAQ Entries
        self.faq_entries = [
            {"question": "How do I create an account?", "answer": "To create an account, click on the 'Sign Up' button on the top right and fill in the required information."},
            {"question": "How do I reset my password?", "answer": "Click on 'Forgot Password' on the login page and follow the instructions to reset your password."},
            {"question": "How can I contact support?", "answer": "You can contact support via email at support@example.com or call us at (123) 456-7890."}
        ]
        
        self.create_faq_entries()

    def create_faq_entries(self):
        for entry in self.faq_entries:
            question_frame = self.create_collapsible_frame(entry["question"], entry["answer"])
            question_frame.pack(fill="x", pady=5, padx=10, ipadx=5, ipady=5)

    def create_collapsible_frame(self, question, answer):
        frame = ctk.CTkFrame(self.scrollable_frame, fg_color="#F7F7F7", corner_radius=5)
        frame.question = question
        frame.answer = answer
        frame.expanded = False
        
        # Question Button
        frame.question_button = ctk.CTkButton(frame, text=question, command=lambda: self.toggle_answer(frame), fg_color="#5089B5", hover_color="#407AB5", text_color="#FFFFFF", anchor="w", width=600)
        frame.question_button.pack(fill="x", padx=5, pady=5)
        
        # Answer Label
        frame.answer_label = ctk.CTkLabel(frame, text=answer, fg_color="#FFFFFF", text_color="#333333", anchor="w", justify="left", wraplength=580)
        frame.answer_label.pack(fill="x", padx=5, pady=5)
        frame.answer_label.pack_forget()  # Initially hide the answer

        return frame

    def toggle_answer(self, frame):
        if frame.expanded:
            frame.answer_label.pack_forget()
        else:
            frame.answer_label.pack(fill="x", padx=5, pady=5)
        frame.expanded = not frame.expanded

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("FAQ Section Example")
        self.geometry("650x400")
        
        self.faq_section = FAQSection(self)
        self.faq_section.pack(fill="both", expand=True, padx=10, pady=10)

if __name__ == "__main__":
    app = App()
    app.mainloop()
