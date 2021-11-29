class Sensor:
    """ Sensor model class"""
    def __init__(self,id, name, data = [], notes = []):
        self.id = id
        self.name = name
        self.data = data

    def __repr__(self):
        return f"Sensor {self.id} {self.name} | " \
               f"data: {self.data}\n"

    def __str__(self):
        return f"Sensor {self.id} {self.name} | " \
               f"data: {self.data}\n"
