import datetime
from typing import List, Union
from model.pot import Pot
import uuid

class Garden:
    """A garden model class:
    a single garden may have more than one pot """
    def __init__(self, name, id=None, status = "new", pots = [],  dimensions = [], location = []):
        self.name = name
        self.status = status
        self.date_created = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.pots = pots
        self.dimensions = dimensions
        self.location = location
        self.id = uuid.uuid4().hex

    def __repr__(self):
        return f"Garden         : {str(self.id)} - {self.name} \n" \
               f"status         : {self.status}\n" \
               f"date_created   : {self.date_created} \n" \
               f"pots           : \n{[p for p in self.pots]} \n" \
               f"dimensions     : {self.dimensions[0] if len(self.dimensions) != 0 else '0'}x{self.dimensions[1] if len(self.dimensions) != 0 else '0'} meters\n"\
               f"location       : {self.location}"

    def __str__(self):
        return f"id: {str(self.id)}\n" \
               f"name: {self.name}\n" \
               f"status: {self.status}\n" \
               f"date_created: {self.date_created}\n" \
               f"pots: {[(p.name, str(p.pot_id)) for p in self.pots]}\n" \
               f"size: {self.dimensions[0] if len(self.dimensions) != 0 else '0'}x{self.dimensions[1] if len(self.dimensions) != 0 else '0'} meters\n"\
               f"location: {self.location}"

    def __dict__(self):
        return {
            "id" : str(self.id),
            "name" : self.name,
            "status" : self.status,
            "date_created" : self.date_created,
            "pots" : self.pots,
            "dimensions" : self.dimensions,
            "location" : self.location
        }

    def get_garden_data_info(self):
        dict = {
            "id"             : str(self.id),
            "name"           : self.name,
            "status"         : self.status,
            "date_created"   : self.date_created,
            "pots"           : [p.short_repr() for p in self.pots],
            "dimensions"     : self.dimensions,
            "location"       : self.location
        }
        # print("get_garden_info", dict["pots"])
        return dict

    def add_pot(self, pot):
        self.pots.append(pot)

    def remove_pot_by_id(self, id):
        removed = [p if p['pot_id'] == id else None for p in self.pots]
        if removed is not None:
            self.pots.remove(removed)
        else:
            print("No such pot in this garden!")
        return removed

    def update_garden_from_dict(self, dict_data):
        self.id = dict_data["id"]
        self.name = dict_data["name"]
        self.status = dict_data["status"]
        self.date_created = dict_data["date_created"]
        self.pots = dict_data["pots"]
        self.dimensions = dict_data["dimensions"]
        self.location = dict_data["location"]


