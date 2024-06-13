import customtkinter as ctk

class reportView(ctk.CTk):

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Salonga Music Shop")
        
        ctk.set_appearance_mode("light")
        self.set_window() 
        self.custom_styles()

        self._top_frame() 
        self._left_frame()
        self._base_frame() 
        self._top_label()
        
        self._app_icon()
        self._selection_1()
        self._selection_2()
        self._selection_3()
        self._selection_4()
        self._selection_5()

    def main(self):
        self.mainloop()

    def set_window(self):
        set_width = 1020
        set_height = 670
        x = int((self.winfo_screenwidth() / 2) - (set_width / 2))
        y = int((self.winfo_screenheight() / 2) - (set_height / 2))
        self.geometry(f'{set_width}x{set_height}+{x}+{y}')
        self.configure(bg_color='#DFDFDF')
        self.minsize(set_width, set_height)
        self.maxsize(set_width, set_height)
    
    def _top_frame(self):
        self.topFrame = ctk.CTkFrame(self, width=844, height=50, fg_color='#FFFFFF', corner_radius=0)
        self.topFrame.place(x=598, y=25, anchor='center')

    def _left_frame(self):
        self.leftFrame = ctk.CTkFrame(self, width=178, height=674, fg_color='#EDEDED', corner_radius=0, border_width=2)
        self.leftFrame.place(x=88, y=335, anchor='center')

    def _base_frame(self):
        self.baseFrame = ctk.CTkFrame(self, width=842, height=620, fg_color='#DFDFDF', corner_radius=0)
        self.baseFrame.place(x=598, y=359, anchor='center')

    def custom_styles(self):
        pass

    def _top_label(self):
        self.topLabel = ctk.CTkLabel(self.topFrame, text='Admin', font=('Consolas', 18, 'bold'), text_color='#2D2D2D')
        self.topLabel.place(x=20, y=12)

    def _app_icon(self):
        self.appIcon = ctk.CTkLabel(self.leftFrame, text="Icon: Name", text_color='#595959', font=('Consolas', 20, 'bold'))
        self.appIcon.place(x=33, y=12)
    
    def _selection_1(self):
        self.selection1 = ctk.CTkButton(self.leftFrame, text="Dashboard", font=('Consolas', 18, 'bold'), text_color="#595959", fg_color='#E2E2E2', hover_color='#f5f5f5',
                                        width=156, height=48, command=self.controller.show_dashboard)
        self.selection1.place(x=10, y=70)

    def _selection_2(self):
        self.selection2 = ctk.CTkButton(self.leftFrame, text="Products", font=('Consolas', 18, 'bold'), text_color="#595959", fg_color='#E2E2E2', hover_color='#f5f5f5',
                                        width=156, height=48, command=self.controller.show_products)
        self.selection2.place(x=10, y=135)
        
    def _selection_3(self):
        self.selection3 = ctk.CTkButton(self.leftFrame, text="Sales", font=('Consolas', 18, 'bold'), text_color="#2D2D2D", fg_color='#FFFFFF', hover_color='#cdcdcd',
                                        width=156, height=48)
        self.selection3.place(x=10, y=200)
        
    def _selection_4(self):
        self.selection4 = ctk.CTkButton(self.leftFrame, text="Delivery", font=('Consolas', 18, 'bold'), text_color="#595959", fg_color='#E2E2E2', hover_color='#f5f5f5',
                                        width=156, height=48, command=self.controller.show_deliveries)
        self.selection4.place(x=10, y=265)
        
    def _selection_5(self):
        self.selection5 = ctk.CTkButton(self.leftFrame, text="Maintenance", font=('Consolas', 18, 'bold'), text_color="#595959", fg_color='#E2E2E2', hover_color='#f5f5f5',
                                        width=156, height=48, command=self.controller.show_maintenance)
        self.selection5.place(x=10, y=330)
