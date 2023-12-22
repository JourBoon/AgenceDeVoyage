from voyage import Voyage
from destination import Destination

class VoyageDAO:

    def __init__(self) -> None:
        pass

    def toVoyage(self, dataset):
        return Voyage(dataset)
    
    def toDestination(self, dataset):
        return Destination(dataset)