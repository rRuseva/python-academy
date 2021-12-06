import datetime
import json
from dataclasses import dataclass, field, asdict
from typing import List
from model.plant import Plant
# from model.quality_report import QualityReport
from model.sensor import Sensor, SensorEntry
from typing import List, Union
import uuid

@dataclass
class Pot:
    name: str
    plant: Plant = None
    sensors: List[Sensor] = field(default_factory=list)
    location: str = None
    notes: str = None
    pot_id  : Union[uuid.UUID, None] = field(default_factory=uuid.uuid4)

    def __repr__(self):
        return f"\npot: {str(self.pot_id):>5.5s}_{self.name} \n " \
               f"plant: {self.plant} \n " \
               f"sensors: \n{[s for s in self.sensors]} \n " \
               f"location {self.location} \n " \
               f"additional notes: {self.notes};"

    def __str__(self):
        return f"pot {str(self.pot_id):>5.5s} - {self.name} |\n" \
               f"plant: {self.plant.__repr__()} |\n " \
               f"sensors: {[s for s in self.sensors]} | \n" \
               f"location {self.location}\n| " \
               f"additional notes: {self.notes};\n"

    def short_repr(self):
        # print("shot_repr", self.plant)
        dict =  {
            "pot_id" : str(self.pot_id),
            "pot_name": self.name,
            "plant": self.plant,
            "location": self.location,
            "notes": self.notes
        }
        # print("shot_repr", dict['plant'])
        return dict
    def get_sensors_count(self):
        return len(self.sensors)

    def __dict__(self):
        """Prepare full pot data for saving to file """
        return {
                "pot_id" : str(self.pot_id),
                "pot_name": self.name,
                "plant": self.plant,
                "location": self.location,
                "notes": self.notes,
                "measurements": self.get_pot_measurements()
                # "measurements": list(zip(*[s.sensor_data for s in self.sensors]))
            }

    def get_pot_measurements(self):
        """Prepare pot measurements for saving to file """
        return list(zip(*[s.get_sensor_data() for s in self.sensors]))

    def update_pot_from_dict(self,dict_data):
        self.pot_id = dict_data["pot_id"]
        self.name = dict_data["pot_name"]
        self.plant = Plant(**dict_data["plant"])
        self.location = dict_data["location"]
        self.notes = dict_data["notes"]
        self.sensors = self.unzip_pot_measurements(dict_data["measurements"])

    def unzip_pot_measurements(self, measurements):
        sensors = list(zip(*measurements))
        list_sensors = []
        for sdata in sensors:
            sens_measurements = []
            sensor = Sensor()
            sensor.name=sdata[0]['sensor_name']
            sensor.sensor_id = sdata[0]['sensor_id']
            sensor.data_units = sdata[0]['data_units']
            for mes in sdata:
                se = SensorEntry(mes['entry']['entry_id'], mes['entry']['value'], mes['entry']['timestamp'])
                sensor.update_sensor_data(se)
            # sensor.sensor_data = sens_measurements
            list_sensors.append(sensor)
        return list_sensors

    def add_sensor(self, sensor):
        self.sensors.append(sensor)

    def remove_sensor_by_id(self, id):
        removed = [s if s['sensor_id'] == id else None for s in self.sensors]
        if removed is not None:
            self.sensors.remove(removed)
        else:
            print("No such sensor in this pot!")
        return removed
#     def save_pot_to_file(self,filename):
#         data = {
#                 "pot_id" : str(self.pot_id),
#                 "pot_name": self.name,
#                 "measurements" : self.get_pot_measurements()
#         }
#         save_to_file(data, filename, 'w', encoding='utf-8')
#         print(f"Data saved to {filename}")
#
#     def load_data_from_file(self, filename):
#         return load_from_file(filename)
#
#     def update_pot_date(self, filename):
#         new_data = self.get_pot_measurements()
#         file_data = load_from_file(filename)
#         file_data["measurements"] += new_data
#         save_to_file(file_data, filename, 'w', encoding='utf-8')
#
# #helpers
# def dumper(obj):
#     try:
#         return obj.toJSON()
#     except:
#         return obj.__dict__
#
# def save_to_file(data,filename, write_mode, encoding):
#     "Saving data to JSON file"
#     try:
#         with open(filename, write_mode, encoding=encoding) as f:
#             json.dump(data, f, indent=4, default=dumper)
#     except OSError as ex:
#         print("OS Error writing to file: {ex}")
#     except Exception as ex:
#         print("Error writing to file: {ex}")
#
# def load_from_file(filename):
#     """Load data from JSON file"""
#     try:
#         with open(filename, "rt") as f:
#             return json.load(f)
#     except Exception as ex:
#         print("Error reading file: {ex}")

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
