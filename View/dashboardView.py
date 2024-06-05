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
        
        self.show_calendar()
        self.show_statistic()
        self.show_inventory()
        self.show_graph_of_sales()
        self.show_stock_alerts()

        self._app_icon()
        self._selection_1()
        self._selection_2()
        self._selection_3()
        self._selection_4()
        self._selection_5()

    def main(self):
        self.mainloop()

    def set_window(self):
        set_width = 760
        set_height = 500
        x = int((self.winfo_screenwidth() / 2) - (set_width / 2))
        y = int((self.winfo_screenheight() / 2) - (set_height / 2))
        self.geometry(f'{set_width}x{set_height}+{x}+{y}')
        self.configure(bg_color='#DFDFDF')
        self.minsize(set_width, set_height)
        self.maxsize(set_width, set_height)

    def _top_frame(self):
        self.topFrame = ctk.CTkFrame(self, width=628, height=39, fg_color='#FFFFFF', corner_radius=0)
        self.topFrame.place(x=446, y=16, anchor='center')

    def _left_frame(self):
        self.leftFrame = ctk.CTkFrame(self, width=132, height=504, fg_color='#E2E2E2', corner_radius=0, border_width=2)
        self.leftFrame.place(x=66, y=250, anchor='center')

    def _base_frame(self):
        self.baseFrame = ctk.CTkFrame(self, width=628, height=461, fg_color='#DFDFDF', corner_radius=0)
        self.baseFrame.place(x=446, y=266, anchor='center')

    def custom_styles(self):
        pass

    def _top_label(self):
        self.topLabel = ctk.CTkLabel(self.topFrame, text='Admin', font=('Consolas', 14, 'bold'), text_color='#2D2D2D')
        self.topLabel.place(x=16, y=6)

    def _app_icon(self):
        self.appIcon = ctk.CTkLabel(self.leftFrame, text="Icon: Name", text_color='#595959')
        self.appIcon.place(x=30, y=12)

    def _selection_1(self):
        self.selection1 = ctk.CTkButton(self.leftFrame, text="Dashboard", font=('Consolas', 12, 'bold'), text_color="#2D2D2D", fg_color='#FFFFFF', hover_color='#cdcdcd', width=116, height=36)
        self.selection1.place(x=8, y=50)

    def _selection_2(self):
        self.selection2 = ctk.CTkButton(self.leftFrame, text="Products", font=('Consolas', 12, 'bold'), text_color="#595959", fg_color='#E2E2E2', hover_color='#f5f5f5', width=116, height=36, command=self.controller.show_products)
        self.selection2.place(x=8, y=95)

    def _selection_3(self):
        self.selection3 = ctk.CTkButton(self.leftFrame, text="Reports", font=('Consolas', 12, 'bold'), text_color="#595959", fg_color='#E2E2E2', hover_color='#f5f5f5', width=116, height=36, command=self.controller.show_reports)
        self.selection3.place(x=8, y=140)

    def _selection_4(self):
        self.selection4 = ctk.CTkButton(self.leftFrame, text="Delivery", font=('Consolas', 12, 'bold'), text_color="#595959", fg_color='#E2E2E2', hover_color='#f5f5f5', width=116, height=36, command=self.controller.show_deliveries)
        self.selection4.place(x=8, y=185)

    def _selection_5(self):
        self.selection5 = ctk.CTkButton(self.leftFrame, text="Maintenance", font=('Consolas', 12, 'bold'), text_color="#595959", fg_color='#E2E2E2', hover_color='#f5f5f5', width=116, height=36, command=self.controller.show_maintenance)
        self.selection5.place(x=8, y=230)

    def show_statistic(self):
        statistic_controller = statisticController()
        statistic_view = statisticView(self.baseFrame, statistic_controller)
        statistic_view.place(x=10, y=146)
    
    def show_calendar(self):
        # self.clear_base_frame()
        calendar_controller = calendarController()
        calendar_view = calendarView(self.baseFrame, calendar_controller)
        calendar_view.place(x=10, y=10)
    
    def show_inventory(self):
        # self.clear_base_frame()
        inventory_controller = inventoryController()
        inventory_view = inventoryView(self.baseFrame, inventory_controller)
        inventory_view.place(x=227, y=10)

    def show_graph_of_sales(self):
        # self.clear_base_frame()
        graph_of_sales_controller = graphSalesController()
        graph_of_sales_view = graphSalesView(self.baseFrame, graph_of_sales_controller)
        graph_of_sales_view.place(x=227, y=255)

    def show_stock_alerts(self):
        stock_alerts_controller = stockAlertsController()
        stock_alerts_view = stockAlertsView(self.baseFrame, stock_alerts_controller)
        stock_alerts_view.place(x=10, y=240)

    def clear_base_frame(self):
        for widget in self.baseFrame.winfo_children():
            widget.destroy()
        # print("Base frame cleared")