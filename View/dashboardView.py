import customtkinter as ctk
from Controller.inventoryController import inventoryController
from Controller.graphSalesController import graphSalesController
from Controller.stockAlertsController import stockAlertsController
from Controller.statisticController import statisticController
from Controller.calendarController import calendarController
from View.inventoryView import inventoryView
from View.graphSalesVIew import graphSalesView
from View.stockAlertsView import stockAlertsView
from View.statisticView import statisticView
from View.calendarView import calendarView
import time

class dashboardView(ctk.CTk):

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Salonga Music Shop")

        ctk.set_appearance_mode("light")

        self.set_window()
        self.custom_styles()

        self.protocol("WM_DELETE_WINDOW",
                      controller.close_window)  # Bind the close event to controller's on_closing method

        self._top_frame()
        self._left_frame()
        self._base_frame()
        self._top_label()

        self._time_label()
        self._update_time()
        
        self.show_dashboard() # Initially show the dashboard view
        self.active_selection = 1 # Default to selection 1 as active
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

    def _time_label(self):
        self.timeLabel = ctk.CTkLabel(self.topFrame, text='', font=("Consolas", 16, 'bold'), text_color='#000000', fg_color='#FFFFFF')
        self.timeLabel.place(x=745, y=12)  # Adjust the x and y values as needed

    def _update_time(self):
        self.current_time = time.strftime("%H:%M:%S")  # Get the current time
        self.timeLabel.configure(text=self.current_time)  # Update the label text
        self.after(1000, self._update_time)

    def _app_icon(self):
            self.appIcon = ctk.CTkLabel(self.leftFrame, text="Icon: Name", text_color='#595959', font=('Consolas', 20, 'bold'))
            self.appIcon.place(x=33, y=12)

    def _selection_1(self):
        self.selection1 = ctk.CTkButton(self.leftFrame, text="Dashboard", font=('Consolas', 18, 'bold'), 
                                        text_color="#2D2D2D", fg_color='#FFFFFF', hover_color='#FFFFFF', 
                                        width=156, height=48, command=lambda: self.set_active_selection(1))
        self.selection1.place(x=10, y=70)

    def _selection_2(self):
        self.selection2 = ctk.CTkButton(self.leftFrame, text="Products", font=('Consolas', 18, 'bold'), 
                                        text_color="#595959", fg_color='#E2E2E2', hover_color='#f5f5f5', 
                                        width=156, height=48, command=lambda: self.set_active_selection(2))
        self.selection2.place(x=10, y=135)

    def _selection_3(self):
        self.selection3 = ctk.CTkButton(self.leftFrame, text="Sales", font=('Consolas', 18, 'bold'), 
                                        text_color="#595959", fg_color='#E2E2E2', hover_color='#f5f5f5', 
                                        width=156, height=48, command=lambda: self.set_active_selection(3))
        self.selection3.place(x=10, y=200)

    def _selection_4(self):
        self.selection4 = ctk.CTkButton(self.leftFrame, text="Delivery", font=('Consolas', 18, 'bold'), 
                                        text_color="#595959", fg_color='#E2E2E2', hover_color='#f5f5f5', 
                                        width=156, height=48, command=lambda: self.set_active_selection(4))
        self.selection4.place(x=10, y=265)

    def _selection_5(self):
        self.selection5 = ctk.CTkButton(self.leftFrame, text="Maintenance", font=('Consolas', 18, 'bold'), 
                                        text_color="#595959", fg_color='#E2E2E2', hover_color='#f5f5f5', 
                                        width=156, height=48, command=lambda: self.set_active_selection(5))
        self.selection5.place(x=10, y=330)
            
    def show_dashboard(self): # Execute on click
            self.clear_base_frame()
            self.show_calendar()
            self.show_statistic()
            self.show_inventory()
            self.show_graph_of_sales()
            self.show_stock_alerts()
            
    def show_calendar(self):
        calendar_controller = calendarController()
        calendar_view = calendarView(self.baseFrame, calendar_controller)
        calendar_view.place(x=15, y=15)
        
    def show_statistic(self):
        statistic_controller = statisticController()
        statistic_view = statisticView(self.baseFrame, statistic_controller)
        statistic_view.place(x=15, y=233)
    
    def show_inventory(self):
        inventory_controller = inventoryController()
        inventory_view = inventoryView(self.baseFrame, inventory_controller)
        inventory_view.place(x=305, y=15)

    def show_stock_alerts(self):
        stock_alerts_controller = stockAlertsController()
        stock_alerts_view = stockAlertsView(self.baseFrame, stock_alerts_controller)
        stock_alerts_view.place(x=15, y=325)
    
    def show_graph_of_sales(self):
        graph_of_sales_controller = graphSalesController()
        graph_of_sales_view = graphSalesView(self.baseFrame, graph_of_sales_controller)
        graph_of_sales_view.place(x=395, y=325)

    def clear_base_frame(self):
        for widget in self.baseFrame.winfo_children():
            widget.destroy()
            
    def set_active_selection(self, selection):
        if self.active_selection == selection: # Skips when the selection is chosen again
            return
        
        self.active_selection = selection
        self.update_button()
        
        match selection:
            case 1:
                self.controller.show_dashboard()
            case 2:
                self.controller.show_products()
            case 3:
                self.controller.show_sales()
            case 4:
                self.controller.show_deliveries()
            case 5:
                self.controller.show_maintenance()
    
    def update_button(self):
        active_fg = '#FFFFFF'
        active_hover = '#FFFFFF'
        inactive_fg = '#E2E2E2'
        inactive_hover ='#F5F5F5'
        active_text ='#2D2D2D'
        inactive_text ='#595959'
        
        for i in range(1, 6):
            button = getattr(self, f'selection{i}')
            if i == self.active_selection:
                button.configure(fg_color=active_fg, hover_color=active_hover, text_color=active_text)
            else:
                button.configure(fg_color=inactive_fg, hover_color=inactive_hover, text_color=inactive_text)
        