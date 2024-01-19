from static.models.destination import Destination
from static.models.voyage import Voyage

class Reservation:
    def __init__(self, dataset, column_names):
        dataset = dict(zip(column_names, dataset))
        
        self.id_res = dataset.get('id_res')
        self.id_client = dataset.get('id_client')
        self.id_dest = dataset.get('id_dest')
        self.cost = dataset.get('cost')
        self.voyage = Voyage(dataset, column_names)

        # Destination
        self.destination = Destination(dataset, column_names)