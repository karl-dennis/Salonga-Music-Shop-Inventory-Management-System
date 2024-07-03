import customtkinter as ctk

class aboutTwoView(ctk.CTkFrame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(width=842, height=620, fg_color='#DFDFDF', corner_radius=0)
        ctk.set_appearance_mode("light")

        self.active_tab = 2
        self.search_query = ctk.StringVar()
        
        self.custom_styles()
        self.base_frame()
 
    def custom_styles(self):
        pass

    def base_frame(self):    
        self.baseFrame = ctk.CTkFrame(self, width=842, height=620, fg_color='#DFDFDF', corner_radius=0)
        self.baseFrame.place(x=0, y=0)
        
        self.place(x=0, y=0) # Place productView Frame, do not change this

        self.show_aboutTwo()
        self.show_faq()
            
    def show_aboutTwo(self):
        self.aboutTwoFrame = ctk.CTkFrame(self.baseFrame, width=820, height=51, fg_color='#F7F7F7', corner_radius=7)
        self.aboutTwoFrame.place(x=11, y=15)
            
        self.tabFrame = ctk.CTkFrame(self.aboutTwoFrame, width=820, height=51, bg_color='#DFDFDF', fg_color='#F7F7F7', corner_radius=7)
        self.tabFrame.place(x=0, y=0)
        
        self.selection1 = ctk.CTkButton(self.tabFrame, width=115, height=18, text='User Manual',
                                        font=('Inter', 13, 'bold'), text_color='#9A9A9A',
                                        fg_color='#F7F7F7', hover_color='#F7F7F7', command=lambda: self.controller.set_active_tab(1))
        self.selection1.place(x=9, y=14)
        
        self.selection2 = ctk.CTkButton(self.tabFrame, width=115, height=18, text='FAQs',
                                        font=('Inter', 13, 'bold'), text_color='#2E2E2E',
                                        fg_color='#F7F7F7', hover_color='#F7F7F7')
        self.selection2.place(x=140, y=14)

        self.selection3 = ctk.CTkButton(self.tabFrame, width=115, height=18, text='System',
                                        font=('Inter', 13, 'bold'), text_color='#9A9A9A',
                                        fg_color='#F7F7F7', hover_color='#F7F7F7', command=lambda: self.controller.set_active_tab(3))
        self.selection3.place(x=253, y=14)
        
        self.tabLine = ctk.CTkFrame(self.tabFrame, width=78, height=4, fg_color='#5089B5', corner_radius=7)
        self.tabLine.place(x=159, y=39)
        
    def show_faq(self):
        self.faqFrame = ctk.CTkFrame(self.baseFrame, width=820, height=526, bg_color='#DFDFDF', fg_color='#F7F7F7')
        self.faqFrame.place(x=11, y=79)
        
        self.scrollingFrame = ctk.CTkScrollableFrame(self.faqFrame, width=800, height=500, fg_color='#F7F7F7', corner_radius=0)
        self.scrollingFrame.place(x=10, y=10)
        
        self.faqLabel = ctk.CTkLabel(self.scrollingFrame, text="Frequently Asked Questions (FAQs)", 
                                     font=("Inter Medium", 17), 
                                     text_color='#000000',
                                     anchor='w',
                                     fg_color="#F7F7F7")
        self.faqLabel.pack(pady=10)
        
        faq_entries = [
            {"question": "How do I add a new product to the inventory?", 
            "answer": "To add a new product, go to the “Products” page, fill in the form with the required details, and click “Save” to add the new product."},
            
            {"question": "How do I record new sale transactions?", 
            "answer": 'To add a new sale, go to the Sales page, select products in the New Sale tab, adjust quantities and view prices in the order list, input buyer information, and click "Save" to complete the transaction.'},
            
            {"question": "How do I add a delivery order?",
            "answer": "To add a delivery order, navigate to the Delivery page, fill out the required information including delivery details and product quantities, then click “Save” to create the order."},
            
            {"question": "How do I reset my password?", 
            "answer": "To reset your password, click on 'Forgot Password' on the login page. Enter your registered email address and follow the instructions sent to your email, including entering the OTP (One-Time Password)."},
            
            {"question": "How do I backup and restore data?", 
            "answer": "To backup data, click the Backup & Restore tab in Maintenance, choose 'Backup', and select where you want to save your data. To restore, select 'Restore' and choose the backup file you want to restore from."},
        ]

        
        for entry in faq_entries:
            question_frame = CollapsibleFrame(self.scrollingFrame, entry["question"], entry["answer"])
            question_frame.pack(padx=10, pady=5)

    def clear_base_frame(self):
        for widget in self.baseFrame.winfo_children():
            widget.destroy()

class CollapsibleFrame(ctk.CTkFrame):
    def __init__(self, parent, question, answer):
        super().__init__(parent, fg_color="#F7F7F7", corner_radius=5)
        self.question = question
        self.answer = answer
        self.expanded = False
        
        self.line_frame = ctk.CTkFrame(self, width=600, height=2, bg_color="#CCCCCC")
        self.line_frame.pack(fill="x", padx=5, pady=(0, 5))
        
        self.question_button = ctk.CTkButton(self, text=self.question, command=self.toggle, 
                                             font=('Inter', 15),
                                             fg_color="#F7F7F7", 
                                             hover_color="#F7F7F7", 
                                             text_color="#000000", 
                                             anchor="w", 
                                             width=600, 
                                             height=50)
        self.question_button.pack(padx=5, pady=0)
        
        self.answer_label = ctk.CTkTextbox(self, 
                                           fg_color="#F7F7F7", 
                                           bg_color='#F7F7F7', 
                                           text_color="#000000", 
                                           width=600, 
                                           height=50,
                                           spacing2=7, 
                                           activate_scrollbars=False, 
                                           wrap='word')
        self.answer_label.insert("1.0", self.answer)  

        self.answer_label.configure(state='disabled')
        self.answer_label.pack(pady=5, fill='both')
        self.answer_label.pack_forget() 
    
    def toggle(self):
        if self.expanded:
            self.answer_label.pack_forget()
        else:
            self.answer_label.pack(pady=5)
        self.expanded = not self.expanded

class App:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("About Two Page (Test)")
        
        self.abouttwo_view = aboutTwoView(self.root, None)
        self.abouttwo_view.pack(fill=ctk.BOTH, expand=True)
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()
