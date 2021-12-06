from dataclasses import dataclass, field, asdict
from typing import List
from typing import List, Union
import uuid

#
@dataclass
class Plant:
    """Plant model cass
    stores information about:
    - conditions of which plant needs
    - plant characterisations - to evaluate plant progress"""

    name : str
    ### the needed conditions for the plant
    humidity : int # percentages
    soil_moisture : int # percentages
    temperature : int # celsius
    light_levels : int # hours sun light per day
    ### plant characterizations
    height : int = None
    leaves_density : int = None
    notes : str = None
    id : Union[uuid.UUID, None] = field(default_factory=uuid.uuid4)

    def __repr__(self):
        return f"id: {str(self.id):>5s} - {self.name} needs of " \
               f"{self.humidity} percentages of humidity, " \
               f"{self.soil_moisture} percentages of soil moisture, " \
               f"average temperature of {self.temperature} Celsius, and " \
               f"average {self.light_levels} hours per day \n"

    def __str__(self):
        return f"{str(self.id):>3s}_{self.name} needs of " \
               f"air humidity - {self.humidity} % | "\
               f"soil moisture - {self.soil_moisture} % | " \
               f"air temperature - {self.temperature} C | " \
               f"sun light per day - {self.light_levels} h;"

    def plant_as_dict(self):
        return(asdict(self))

    def get_conditions(self):
        return {
            "humidity" : self.humidity,
            "soil_temperature": self.soil_moisture,
            "temperature": self.temperature,
            "light_levels": self.light_levels
        }

    def get_characteristics(self):
        return {
            "height" : self.height,
            "leaves_density": self.leaves_density,
        }

    # def get_plant_data(self):
    def __dict__(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "humidity" : self.humidity,
            "soil_moisture" : self.soil_moisture,
            "temperature" : self.temperature,
            "light_levels" : self.light_levels,
            "height" : self.height,
            "leaves_density" : self.leaves_density,
            "notes" : self.notes,
        }
