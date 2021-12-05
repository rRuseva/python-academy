import json
from dataclasses import dataclass, field, asdict, astuple
from datetime import datetime
import itertools
from model.plant import Plant
from typing import List, Union
import uuid


@dataclass
class SensorEntry:
    """Data model class describing readings from sensor """
    entry_id : int
    value: int
    timestamp : datetime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def __repr__(self):
        return f"\n{str(self.entry_id):>5.5s} {self.timestamp} | " \
               f"data: {self.value:>4}"

    def __str__(self):
        return f"\n{str(self.entry_id):>5.5s} {self.timestamp} | " \
               f"data: {self.value:>4}"

    def measurement_as_tuple(self):
        return astuple(self)

    def measurement_as_dict(self):
        return asdict(self)

    # def update_measurement_from_dict(data_dict):
    #     entry_id = data_dict["entry_id"]
    #     value = data_dict["value"]
    #     timestamp = data_dict["timestamp"]
    #     return SensorEntry(entry_id,value,timestamp)

@dataclass
class Sensor:
    """Data model class for sensor"""
    name: str
    data_units: str = "%"
    type: str = None
    notes: str = None
    sensor_data: List[SensorEntry] = field(default_factory=list)
    sensor_id : Union[uuid.UUID, None] = field(default_factory=uuid.uuid4)

    def __repr__(self):
        return f"sensor_{str(self.sensor_id):>5.5s}-{self.name}: " \
               f"\ndata: {self.sensor_data}\n"

    def __str__(self):
        return f"sensor_{str(self.sensor_id):>5.5s}-{self.name}: " \
               f"\ndata: {self.sensor_data}\n"

    def sensor_as_tuple(self):
        return astuple(self)

    def __dict__(self):
        return asdict(self)

    def get_sensor_data(self):
        return ({"sensor_name":self.name, "sensor_id":str(self.sensor_id), "data_units": self.data_units, "entry": entry} for entry in self.sensor_data)

    def update_sensor_data(self, se:SensorEntry):
        self.sensor_data.append(se)

    def update_sensor_from_dict(self,data_dict):
        self.name = data_dict["name"]
        self.data_units = data_dict["data_units"]
        self.type = data_dict["type"]
        self.notes = data_dict["notes"]
        self.sensor_id = data_dict["sensor_id"]
        se = SensorEntry(data_dict["entry"]["entry_id"], data_dict["entry"]["value"], data_dict["entry"]["timestamp"])
        self.update_sensor_data(se)

