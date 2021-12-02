import datetime
import json
from dataclasses import dataclass, field, asdict
from typing import List
from plant import Plant
from sensor import Sensor
from typing import List, Union
import uuid

@dataclass
class Pot:
    name: str
    plant: Plant
    sensors: List[Sensor] = field(default_factory=list)
    place: str = None
    notes: str = None
    pot_id  : Union[uuid.UUID, None] = field(default_factory=uuid.uuid4)

    def __repr__(self):
        return f"Pot {str(self.pot_id):>5.5s} - {self.name} | " \
               f"plants: {self.plant} \n| " \
               f"Sensors: {self.sensors} \n| " \
               f"additional notes: {self.notes};\n"

    def __str__(self):
        return f"Pot {str(self.pot_id):>5.5s}  - {self.name} | " \
               f"plants: {self.plant} \n| " \
               f"Sensors: {self.sensors} \n| " \
               f"additional notes: {self.notes};\n"

    def get_sensors_count(self):
        return len(self.sensors)

    def save_to_file(self,filename, write_mode):
        with open(filename, write_mode, encoding='utf-8') as f:
            data= {
                "pot_id" : str(self.pot_id),
                "data": list(zip([(s.sensor_data) for s in self.sensors]))
            }
            # print(list(zip( self.sensors)))
            print(data)
            json.dump(data, f, indent=4)
        print(f"Data saved to {filename}")


#helpers
def dumper(obj):
    try:
        return obj.toJSON()
    except:
        return obj.__dict__


def save_to_file(data,filename, write_mode):
    with open(filename, write_mode, encoding='utf-8') as f:
        json.dump(data, f, indent=4, default=dumper)
    print(f"Data saved to {filename}")

###
# def load_from_file(filename, entity_class):
#     """Load books data from JSON file"""
#     with open(filename, "rt") as f:
#         return json.load(f, object_hook=obj_hook(entity_class))
#
# def obj_hook(clazz):
#     def obj_hook(dict):
#         obj = clazz()
#         obj.__dict__ = dict
#         return obj
#     return obj_hook
