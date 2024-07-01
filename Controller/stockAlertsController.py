from Model.stockAlertsModel import stockAlertsModel
from View.stockAlertsView import stockAlertsView


class stockAlertsController:
    def __init__(self, parent):
        self.model = stockAlertsModel()
        self.view = stockAlertsView(parent, self)
        
    def main(self):
        pass
    
    def fetch_transaction(self):
        return self.model.fetch_transaction()