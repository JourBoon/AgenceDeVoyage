from voyage import Voyage

class VoyageDAO:

    def __init__(self) -> None:
        pass

    def toVoyage(self, dataset):
        return Voyage(dataset)