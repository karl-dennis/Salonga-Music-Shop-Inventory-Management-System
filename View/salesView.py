import customtkinter as ctk
import tkinter as tk

class salesView(ctk.CTkFrame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(width=842, height=620, fg_color='#DFDFDF', corner_radius=0)
        ctk.set_appearance_mode("light")
        
        self.active_tab = 1
        self.search_query = tk.StringVar()
        
        self.custom_styles()
        self.base_frame()

    def custom_styles(self):
        pass
    
    def base_frame(self):
        self.baseFrame = ctk.CTkFrame(self, width=842, height=620, fg_color='#DFDFDF', corner_radius=0)
        self.baseFrame.place(x=0, y=0)
        
        self.place(x=0, y=0) # Place salesView Frame, do not change this
        
        self.show_firstPage()
        self.show_orderFrame()
    
    def show_firstPage(self):
        self.firstPageFrame = ctk.CTkFrame(self.baseFrame, width=522, height=583, fg_color='#F7F7F7', corner_radius=7)
        self.firstPageFrame.place(x=12, y=15)
                
        self.tabFrame = ctk.CTkFrame(self.firstPageFrame, width=246, height=40, fg_color='transparent')
        self.tabFrame.place(x=6, y=7)
        
        self.selection1 = ctk.CTkButton(self.tabFrame, width=110, height=36, text='New Sale',
                                        font=('Inter', 13, 'bold'), text_color='#2E2E2E',
                                        fg_color='#F7F7F7', hover_color='#F7F7F7', command=lambda: self.controller.set_active_tab(1))
        self.selection1.place(x=3, y=0)
        
        self.selection2 = ctk.CTkButton(self.tabFrame, width=110, height=36, text='Sales Report',
                                        font=('Inter', 13, 'bold'), text_color='#9A9A9A',
                                        fg_color='#F7F7F7', hover_color='#F7F7F7', command=lambda: self.controller.set_active_tab(2))
        self.selection2.place(x=133, y=0)

        self.tabLine = ctk.CTkFrame(self.tabFrame, width=78, height=4, fg_color='#5089B5', corner_radius=7)
        self.tabLine.place(x=19, y=33)
        
        self.dividerLine = ctk.CTkFrame(self.firstPageFrame, width=522, height=2, fg_color='#DDDDDD')
        self.dividerLine.place(x=0, y=51)

        self.searchFrame = ctk.CTkFrame(self.firstPageFrame, width=160, height=22, fg_color='transparent')
        self.searchFrame.place(x=349, y=14) 
        
        self.search_query.set('Search')
        
        self.searchEntry = ctk.CTkEntry(self.searchFrame, width=160, height=22,
                                        fg_color='#FAFAFA', border_color='#BCBCBC', 
                                        border_width=2, corner_radius=10, font=('Inter Medium', 11), 
                                        text_color='#959595', textvariable=self.search_query)
        self.searchEntry.place(x=0, y=0) 
        
        def on_entry_click(event):
            if self.searchEntry.get() == 'Search':
                self.searchEntry.delete(0, tk.END)  # Delete all the text in the entry

        def on_focus_out(event):
            if self.searchEntry.get() == '':
                self.search_query.set('Search')

        self.searchEntry.bind('<FocusIn>', on_entry_click)
        self.searchEntry.bind('<FocusOut>', on_focus_out)    
        
        def perform_search():
            query = self.search_query.get()
            if query.strip() != '':
                query = self.search_query.get()
                
                """Insert model/controller here"""
                
                print(f"Performing search for: {query}")
            
        self.searchEntry.bind('<Return>', lambda event: perform_search())
        self.baseFrame.bind('<Button-1>', lambda event: self.baseFrame.focus_set())
        self.firstPageFrame.bind('<Button-1>', lambda event: self.firstPageFrame.focus_set())
        
    def show_orderFrame(self):
        self.orderFrame = ctk.CTkFrame(self.baseFrame, width=285, height=583, fg_color='#F7F7F7', corner_radius=7)
        self.orderFrame.place(x=546, y=15)
        
        self.label = ctk.CTkLabel(self.orderFrame, text="Order #0001", font=('Inter', 15, 'bold'), text_color='#2E2E2E')
        self.label.place(x=95, y=12)
        self.orderFrame.bind('<Button-1>', lambda event: self.orderFrame.focus_set())

    
    def clear_base_frame(self):
        for widget in self.baseFrame.winfo_children():
            widget.destroy()
