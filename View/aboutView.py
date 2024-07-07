import customtkinter as ctk
from CTkPDFViewer import CTkPDFViewer

class aboutView(ctk.CTkFrame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(width=842, height=620, fg_color='#DFDFDF', corner_radius=0)
        ctk.set_appearance_mode("light")

        self.active_tab = 1
        self.search_query = ctk.StringVar()
        self.pdf_frame = None
        
        self.custom_styles()
        self.base_frame()
 
    def custom_styles(self):
        pass

    def base_frame(self):    
        self.baseFrame = ctk.CTkFrame(self, width=842, height=620, fg_color='#DFDFDF', corner_radius=0)
        self.baseFrame.place(x=0, y=0)
        
        self.place(x=0, y=0) # Place productView Frame, do not change this

        self.show_aboutOne()
        self.show_userManual()
        
        
    def show_aboutOne(self):
        self.aboutOneFrame = ctk.CTkFrame(self.baseFrame, width=820, height=51, fg_color='#F7F7F7', corner_radius=7)
        self.aboutOneFrame.place(x=11, y=15)
            
        self.tabFrame = ctk.CTkFrame(self.aboutOneFrame, width=820, height=51, bg_color='#DFDFDF', fg_color='#F7F7F7', corner_radius=7)
        self.tabFrame.place(x=0, y=0)
        
        self.selection1 = ctk.CTkButton(self.tabFrame, width=115, height=18, text='User Manual',
                                        font=('Inter', 13, 'bold'), text_color='#2E2E2E',
                                        fg_color='#F7F7F7', hover_color='#F7F7F7')
        self.selection1.place(x=9, y=14)
        
        self.selection2 = ctk.CTkButton(self.tabFrame, width=115, height=18, text='FAQs',
                                        font=('Inter', 13, 'bold'), text_color='#9A9A9A',
                                        fg_color='#F7F7F7', hover_color='#F7F7F7', command=lambda: self.controller.set_active_tab(2))
        self.selection2.place(x=140, y=14)

        self.selection3 = ctk.CTkButton(self.tabFrame, width=115, height=18, text='System',
                                        font=('Inter', 13, 'bold'), text_color='#9A9A9A',
                                        fg_color='#F7F7F7', hover_color='#F7F7F7', command=lambda: self.controller.set_active_tab(3))
        self.selection3.place(x=253, y=14)
        
        self.tabLine = ctk.CTkFrame(self.tabFrame, width=78, height=4, fg_color='#5089B5', corner_radius=7)
        self.tabLine.place(x=28, y=39)

    def show_userManual(self):
        self.userManualFrame = ctk.CTkFrame(self.baseFrame, width=820, height=526, bg_color='#DFDFDF', fg_color='#F7F7F7')
        self.userManualFrame.place(x=11, y=79)
           
        self.open_pdf("SALONGA MUSIC SHOP SYSTEM MANUAL.pdf")  # Specify the PDF file to open
        
    def open_pdf(self, file_path):
        if self.pdf_frame:
            self.pdf_frame.destroy()
        
        self.pdf_frame = CTkPDFViewer(self.userManualFrame, 
                                      width=800, height=500, 
                                      page_width=400, page_height=500,
                                      file=file_path,
                                      page_separation_height=10,
                                      fg_color='#F7F7F7', bg_color='#DFDFDF',
                                      corner_radius=7,
                                      )
        self.pdf_frame.pack( expand=True)  # Occupy the entire userManualFrame
        self.pdf_frame.tkraise()  # Raise the PDF viewer widget to the top layer
    
    def clear_base_frame(self):
        for widget in self.baseFrame.winfo_children():
            widget.destroy()
