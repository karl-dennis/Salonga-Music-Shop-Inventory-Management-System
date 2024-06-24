import customtkinter as ctk
import tkinter as tk

class salesTwoView(ctk.CTkFrame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(width=842, height=620, fg_color='#DFDFDF', corner_radius=0)
        ctk.set_appearance_mode("light")
        
        self.active_tab = 2
        self.search_query = tk.StringVar()

        self.custom_styles()
        self.base_frame()

    def custom_styles(self):
        pass
    
    def base_frame(self):
        self.baseFrame = ctk.CTkFrame(self, width=842, height=620, fg_color='#DFDFDF', corner_radius=0)
        self.baseFrame.place(x=0, y=0)
        
        self.place(x=0, y=0) # Place salesView Frame, do not change this
        
        self.show_secondPage()
        self.show_orderFrame()
        self.show_salesGraph()
        self.show_revenue()
        self.show_reports()
        
        self.baseFrame.bind('<Button-1>', lambda event: self.baseFrame.focus_set())
        self.secondPageFrame.bind('<Button-1>', lambda event: self.secondPageFrame.focus_set())
        self.orderFrame.bind('<Button-1>', lambda event: self.orderFrame.focus_set())
        self.salesGraphFrame.bind('<Button-1>', lambda event: self.salesGraphFrame.focus_set())
        self.revenueFrame.bind('<Button-1>', lambda event: self.revenueFrame.focus_set())
        self.reportsFrame.bind('<Button-1>', lambda event: self.reportsFrame.focus_set())

                
    def show_secondPage(self):
        self.secondPageFrame = ctk.CTkFrame(self.baseFrame, width=522, height=340, fg_color='#F7F7F7', corner_radius=7)
        self.secondPageFrame.place(x=12, y=15)
        
        self.tabFrame = ctk.CTkFrame(self.secondPageFrame, width=246, height=40, fg_color='transparent')
        self.tabFrame.place(x=6, y=7)
        
        self.selection1 = ctk.CTkButton(self.tabFrame, width=110, height=36, text='New Sale',
                                        font=('Inter', 13, 'bold'), text_color='#9A9A9A',
                                        fg_color='#F7F7F7', hover_color='#F7F7F7', command=lambda: self.controller.set_active_tab(1))
        self.selection1.place(x=3, y=0)
        
        self.selection2 = ctk.CTkButton(self.tabFrame, width=110, height=36, text='Sales Report',
                                        font=('Inter', 13, 'bold'), text_color='#2E2E2E',
                                        fg_color='#F7F7F7', hover_color='#F7F7F7', command=lambda: self.controller.set_active_tab(2))
        self.selection2.place(x=133, y=0)

        self.tabLine = ctk.CTkFrame(self.tabFrame, width=78, height=4, fg_color='#5089B5', corner_radius=7)
        self.tabLine.place(x=150, y=33)
        
        self.dividerLine = ctk.CTkFrame(self.secondPageFrame, width=522, height=2, fg_color='#DDDDDD')
        self.dividerLine.place(x=0, y=51)
        
        
        self.searchFrame = ctk.CTkFrame(self.secondPageFrame, width=160, height=22, fg_color='transparent')
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
        
    def show_orderFrame(self):
        self.orderFrame = ctk.CTkFrame(self.baseFrame, width=285, height=585, fg_color='#F7F7F7', corner_radius=7)
        self.orderFrame.place(x=546, y=15)
        
        self.label = ctk.CTkLabel(self.orderFrame, text="Order #0001", font=('Inter', 15, 'bold'), text_color='#2E2E2E')
        self.label.place(x=95, y=12)
        
    def show_salesGraph(self):
        self.salesGraphFrame = ctk.CTkFrame(self.baseFrame, width=315, height=232, fg_color='#F7F7F7', corner_radius=7)
        self.salesGraphFrame.place(x=12, y=367)
        
        self.label = ctk.CTkLabel(self.salesGraphFrame, text="Sales Graph", font=('Inter Medium', 13), text_color='#2E2E2E',
                                  width=130, height=16, anchor='w')
        self.label.place(x=12, y=8)

    def show_revenue(self):
        from PIL import Image
        self.revenueFrame = ctk.CTkFrame(self.baseFrame, width=201, height=58, fg_color='#F7F7F7', 
                                         bg_color='transparent', border_width=3, border_color='#5089B5',
                                         corner_radius=7)
        self.revenueFrame.place(x=334, y=367)
        
        self.icon = ctk.CTkImage(light_image=Image.open("./assets/revenue.png"), size=(30,30))
        self.my_icon = ctk.CTkLabel(self.revenueFrame, text="", image=self.icon)
        self.my_icon.place(x=13, y=10)
        
        self.label = ctk.CTkLabel(self.revenueFrame, text="Revenue (May 2024)", font=('Inter', 13, 'bold'), 
                                  text_color='#5089B5', fg_color='transparent',
                                  width=145, height=15, anchor='w')
        self.label.place(x=50, y=13)
        
        self.label = ctk.CTkLabel(self.revenueFrame, text="₱18,049.25", font=('Inter Medium', 12), 
                                  text_color='#5089B5', fg_color='transparent', 
                                  width=130, height=12, anchor='w')
        self.label.place(x=50, y=26)
    
    def show_reports(self):
        self.reportsFrame = ctk.CTkFrame(self.baseFrame, width=201, height=165, fg_color='#F7F7F7', corner_radius=7)
        self.reportsFrame.place(x=334, y=434)
        
        self.label = ctk.CTkLabel(self.reportsFrame, text="Reports", font=('Inter Medium', 13), text_color='#2E2E2E')
        self.label.place(x=14, y=7)
    
    def clear_base_frame(self):
        for widget in self.baseFrame.winfo_children():
            widget.destroy()
