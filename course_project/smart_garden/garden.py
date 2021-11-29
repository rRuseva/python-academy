import datetime

class Garden:
    """A garden model class:
    a single garden may have more than one pot """
    def __init__(self, name, status, pots = [],  dimensions = [], location = []):
        self.id = None
        self.name = name
        self.status = status
        self.date_crated = datetime.datetime.now()
        self.pots = pots
        self.dimensions = dimensions
        self.location = location

    def __repr__(self):
        return f"Garden         : {self.id:<5d} - {self.name} \n" \
               f"status         : {self.status}\n" \
               f"date created   : {self.date_crated} \n" \
               f"pots           : {self.pots}\n" \
               f"size           : {self.dimensions[0]}x{self.dimensions[1]} meters \n" \
               f"location       : {self.location}"


    def __str__(self):
        return f"Garden         : {self.id} - {self.name} \n" \
               f"status         : {self.status}\n" \
               f"date created   : {self.date_crated} \n" \
               f"pots           : \n{self.pots}\n" \
               f"size           : {self.dimensions[0]}x{self.dimensions[1]} meters \n" \
               f"location       : {self.location}"
