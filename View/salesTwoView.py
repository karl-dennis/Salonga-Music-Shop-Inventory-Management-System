import customtkinter as ctk

class salesTwoView(ctk.CTkFrame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(width=842, height=620, fg_color='#DFDFDF', corner_radius=0)
        ctk.set_appearance_mode("light")
        
        self.active_tab = 2
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
    
    def show_secondPage(self):
        self.secondPageFrame = ctk.CTkFrame(self.baseFrame, width=522, height=340, fg_color='#F7F7F7', corner_radius=7)
        self.secondPageFrame.place(x=12, y=15)
        
        self.tabFrame = ctk.CTkFrame(self.secondPageFrame, width=246, height=40, fg_color='transparent')
        self.tabFrame.place(x=6, y=7)
        
        self.selection1 = ctk.CTkButton(self.tabFrame, width=110, height=36, text='New Sale',
                                        font=('Inter', 13, 'bold'), text_color='#9A9A9A',
                                        fg_color='#F7F7F7', hover_color='#F7F7F7', command=lambda: self.set_active_tab(1))
        self.selection1.place(x=3, y=0)
        
        self.selection2 = ctk.CTkButton(self.tabFrame, width=110, height=36, text='Sales Report',
                                        font=('Inter', 13, 'bold'), text_color='#2E2E2E',
                                        fg_color='#F7F7F7', hover_color='#F7F7F7', command=lambda: self.set_active_tab(2))
        self.selection2.place(x=133, y=0)

        self.tabLine = ctk.CTkFrame(self.tabFrame, width=78, height=4, fg_color='#5089B5', corner_radius=7)
        self.tabLine.place(x=150, y=33)
        
        self.dividerLine = ctk.CTkFrame(self.secondPageFrame, width=522, height=2, fg_color='#DDDDDD')
        self.dividerLine.place(x=0, y=51)
        
    def show_orderFrame(self):
        self.orderFrame = ctk.CTkFrame(self.baseFrame, width=285, height=583, fg_color='#F7F7F7', corner_radius=7)
        self.orderFrame.place(x=546, y=15)
        
        self.label = ctk.CTkLabel(self.orderFrame, text="Order #0001", font=('Inter', 15, 'bold'), text_color='#2E2E2E')
        self.label.place(x=95, y=12)
        
    def show_salesGraph(self):
        self.salesGraphFrame = ctk.CTkFrame(self.baseFrame, width=315, height=232, fg_color='#F7F7F7', corner_radius=7)
        self.salesGraphFrame.place(x=231, y=10)
        
        self.label = ctk.CTkLabel(self.salesGraphFrame, text="Sales Graph", font=('Inter Medium', 13), text_color='#2E2E2E')
        self.label.place(x=14, y=7)

    def clear_base_frame(self):
        for widget in self.baseFrame.winfo_children():
            widget.destroy()

    def set_active_tab(self, tab):
        self.active_tab = tab
        self.update_tab()
        
        match tab:
            case 1:
                self.controller.show_firstPage()
                self.tabLine.place_forget()
                self.tabLine.place(x=19, y=33)
            case 2:
                self.controller.show_secondPage()
                self.tabLine.place_forget()
                self.tabLine.place(x=150, y=33)
                
    def update_tab(self):
        active_text = '#2E2E2E'
        inactive_text ='#9A9A9A'
        
        for i in range(1, 3):
            tab = getattr(self, f'selection{i}')
            if i == self.active_tab:
                tab.configure(text_color=active_text)
            else:
                tab.configure(text_color=inactive_text)

# class App:
#     def __init__(self):
#         self.root = ctk.CTk()
#         self.root.title("Sales Page (Test)")
        
#         self.product_view = salesView(self.root, None)
#         self.product_view.pack(fill=ctk.BOTH, expand=True)
        
#     def run(self):
#         self.root.mainloop()

# if __name__ == "__main__":
#     app = App()
#     app.run()