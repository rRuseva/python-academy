from dataclasses import dataclass, field
from datetime import datetime

from plant import Plant


@dataclass
class SensorReading:
    sensor_id : int
    value: int
    timestamp : datetime = datetime.now()

    sensor_data

@dataclass
class Sensor:
    sensor_id : int
    name: str
    type: str
    notes: str
    readings: list[SensorReading] = field(default_factory=list)



