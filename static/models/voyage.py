class Voyage:
    def __init__(self, dataset):
        self.dataset = dataset

    def getName(self):
        return self.dataset[0]
    
    def getCost(self):
        return self.dataset[1]