from Model.statisticModel import statisticModel
from View.statisticView import statisticView

class statisticController:
    def __init__(self, master):
        self.model = statisticModel()
        self.view = statisticView(master, self)
        self.update_revenue()

    def update_revenue(self):
        total_revenue = self.model.fetch_revenue()
        self.view.set_total_revenue(total_revenue)
