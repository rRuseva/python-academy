import datetime
class Pot:
    """Pot model class
    pots are small gardens with only one type of plant
    consists of composition of sensors"""
    def __init__(self,id, name, plant, sensors = [], notes = None ):
        self.id = id
        self.name = name
        self.notes = notes
        self.plant = plant
        date_crated = datetime.datetime.now()
        self.sensors = sensors

    def __repr__(self):
        return f"Pot {self.id} - {self.name} | " \
               f"plants: {self.plant} \n| " \
               f"Sensors: {self.sensors} \n| " \
               f"additional notes: {self.notes};\n"

    def __str__(self):
        return f"Pot  {self.id} - {self.name} | " \
               f"plants: {self.plant} \n| " \
               f"Sensors: {self.sensors} \n| " \
               f"additional notes: {self.notes};\n"


