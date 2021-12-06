from dataclasses import dataclass, field, asdict, astuple
from datetime import datetime
from typing import List, Union
from model.plant import Plant
import uuid

@dataclass
class QualityReport:
    """Template for evaluation of plant progress"""
    plant_characterizations : dict = None # plant_characterization
    author : str = None
    id : Union[uuid.UUID, None] = field(default_factory=uuid.uuid4)
    date_created : datetime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    pot_id: str = None

    def __repr__(self):
        return f"id_{self.id}_{self.timestamp}" \
               f"date_created: {self.date_created}\n" \
               f"author: {self.author} \n" \
               f"plant_characterizations: {self.plant_characterizations}" \
               f"pot: {self.pot_id}"

    def __str__(self):
        return f"id_{self.id}_{self.timestamp}" \
               f"date_created: {self.date_created}\n" \
               f"author: {self.author} \n" \
               f"plant_characterizations: {self.plant_characterizations}" \
               f"pot: {self.pot_id}"
