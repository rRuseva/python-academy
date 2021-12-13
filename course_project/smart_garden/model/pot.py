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
    dimensions: str = None
    notes: str = None
    pot_id  : Union[uuid.UUID, None] = field(default_factory=uuid.uuid4)

    def __repr__(self):
        return f"\npot: {str(self.pot_id):>5.5s}_{self.name} \n " \
               f"plant: {self.plant} \n " \
               f"sensors: \n{[s for s in self.sensors]} \n " \
               f"location {self.location} \n " \
               f"dimensions {self.dimensions} \n " \
               f"additional notes: {self.notes};"

    def __str__(self):
        return f"pot {str(self.pot_id):>5.5s} - {self.name} |\n" \
               f"plant: {self.plant.__repr__()} |\n " \
               f"sensors: {[s for s in self.sensors]} | \n" \
               f"location {self.location}\n| " \
               f"dimensions {self.dimensions} \n " \
               f"additional notes: {self.notes};\n"

    def short_repr(self):
        # print("shot_repr", self.plant)
        dict =  {
            "pot_id"    : str(self.pot_id),
            "pot_name"  : self.name,
            "plant"     : self.plant,
            "location"  : self.location,
            "dimensions" : self.dimensions,
            "notes"     : self.notes
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
                "plant": self.plant.__dict__(),
                "location": self.location,
                "dimensions": self.dimensions,
                "notes": self.notes,
                "measurements": self.get_pot_measurements()
                # "measurements": list(zip(*[s.sensor_data for s in self.sensors]))
            }

    def get_pot_measurements(self):
        """Prepare pot measurements for saving to file """
        # print("***",self.sensors[0].get_sensor_data())
        return list(zip(*[s.get_sensor_data() for s in self.sensors]))

    def update_pot_from_dict(self,dict_data):
        self.pot_id = dict_data["pot_id"]
        self.name = dict_data["pot_name"]
        self.plant = Plant(**dict_data["plant"])
        self.location = dict_data["location"]
        self.dimensions = dict_data["dimensions"]
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
#
    def get_sensors(self):
        return self.sensors
