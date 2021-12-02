import json
from dataclasses import dataclass, field, asdict
from datetime import datetime
import itertools
from plant import Plant
from typing import List, Union
import uuid


@dataclass
class SensorEntry:
    value: int
    timestamp : datetime = datetime.now().timestamp()
    entry_id : (Union[uuid.UUID, None]) = (field(default_factory=uuid.uuid4))

    def __repr__(self):
        return f"\n{str(self.entry_id):>5.5s} {self.timestamp} | " \
               f"data: {self.value:>5}"

    def __str__(self):
        return f"\n{str(self.entry_id):>5.5s} {self.timestamp} | " \
               f"data: {self.value:>5}"

    def print_as_dict(self):
        print(asdict(self))





@dataclass
class Sensor:
    name: str
    type: str = None
    notes: str = None
    sensor_data: List[SensorEntry] = field(default_factory=list)
    sensor_id : (Union[uuid.UUID, None]) = (field(default_factory=uuid.uuid4))

    def __repr__(self):
        return f"Sensor {str(self.sensor_id):>5.5s} {self.name} | " \
               f"\ndata: {self.sensor_data}\n"
    def __str__(self):
        return f"Sensor {str(self.sensor_id):>5.5s} {self.name} | " \
               f"\ndata: {self.sensor_data}\n"

    def update_sensor_data(self, se:SensorEntry):
        self.sensor_data.append(se)

    # def persist(self, filename, write_mode):
    #     save_to_file([asdict(data) for data in self.sensor_data] , filename, write_mode)

