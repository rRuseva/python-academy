import json
import os.path
from collections import namedtuple

import serial

import config
from model.sensor import SensorEntry, Sensor
from model.pot import Pot
from model.garden import Garden
from model.plant import Plant
import utils.global_utils as utils

class GardenRepository:
    def __init__(self, garden_name, garden_path = ""):
        self.garden = Garden(garden_name)
        if self.garden is not None:
            self.garden_path = os.path.join(config.DATA_PATH, utils.generate_filename(self.garden.name) )
        else:
            self.garden_path = garden_path

    def __str__(self):
        return self.garden.__repr__()

    def set_garden(self, garden):
        self.garden = garden

    def pots_count(self):
        return len(self.garden.pots)

    def garden_sensors_count(self):
        return [{"pot_name": p.name, "sensors_count": len(p.sensors)}  for p in self.garden.pots]

    def pot_sensors_count(self, pot):
        return pot.get_sensors_count()

    def get_pot_sensors(self, pot):
        return pot.get_sensors()

    def save_garden_data(self):
        try:
            os.mkdir(self.garden_path, mode=0o777)
            print("Creating garden directory!")
        except FileExistsError as er:
            print(f"Warning: Directory already exists: {er}")

        data = self.garden.get_garden_data_info()
        # print("garden data", data)
        garden_file_name = os.path.join(self.garden_path,utils.generate_filename(self.garden.name) + ".json")
        save_to_file(data, garden_file_name ,'w',encoding=config.ENCODING)
        ### PLANT info is overriden CHECK it
        for pot in self.garden.pots:
            filename = os.path.join(self.garden_path, utils.generate_pot_filename(pot.name))
            self.save_pot_data_to_file(filename, pot)
        print(f"Garden data saved to {garden_file_name}")

    def save_pot_data_to_file(self,filename, pot):
        data = pot.__dict__()
        # print("pot data to file ")
        # print(data)
        save_to_file(data, filename, 'w', encoding=config.ENCODING)
        print(f"Pot data saved to {filename}")

    def update_garden_pots(self):
        for pot in self.garden.pots:
            filename = os.path.join(self.garden_path, utils.generate_pot_filename(pot.name))
            self.update_pot_file_data(filename, pot)
        print("Garden pots are updated!")

    def update_pot_file_data(self, filename, pot):
        new_data = pot.get_pot_measurements()
        file_data = load_from_file(filename)
        file_data["measurements"] += new_data
        save_to_file(file_data, filename, 'w', encoding=config.ENCODING)

    def load_pot_data_from_file(self, filename, pot):
        # print(pot)
        data = load_from_file(filename)
        # print("********** pot data")
        # print(data)
        # pot = Pot(data["pot_name"])
        if data:
            pot.update_pot_from_dict(data)
        # return pot

    def load_garden_data_from_file(self,filename):
        self.garden_path = os.path.dirname(filename)
        garden_data = load_from_file(filename)

        self.garden = Garden(garden_data["name"])
        new_pots = []

        for pot_info in garden_data['pots']:
            filename = os.path.join(self.garden_path, utils.generate_pot_filename(pot_info["pot_name"]))
            pot = Pot(pot_info["pot_name"])
            # print("pot_file ", filename)
            self.load_pot_data_from_file(filename, pot)
            new_pots.append(pot)
        garden_data['pots'] = new_pots
        self.garden.update_garden_from_dict(garden_data)

    def read_pot_sensors_data(self,pot, max_entry_counts = 3):
        """Reading sensor information from one pot
        data is populated to class objects
        and saves it to JSON file with the name "pot_{pot_name}.json
        if the file exists the information is updated
        """
        with serial.Serial(
                port = config.SERAIL_PORT,
                baudrate = config.SERIAL_BAUDRAT,
                write_timeout = config.SERAIL_WRITE_TIMEOUT
            ) as ser:
                print(f"Serial connection to {config.SERAIL_PORT} is opened. ")

                sensor_count = pot.get_sensors_count()
                entry_count = 0
                while(entry_count != max_entry_counts):
                    for i in range(sensor_count):
                        line = ser.readline()
                        if line:
                            s_data = line.decode(config.ENCODING)  # decode arduino data to utf-8 string
                            s_data = s_data.strip().split(": ")
                            print(s_data)
                            se = SensorEntry(1000*(i+1)+entry_count+1, s_data[1])
                            pot.sensors[i].update_sensor_data(se)
                    entry_count += 1
                    # condition for quiting reading sensor information
                    # if entry_count == max_entry_counts:
                    #     ser.close()
                    #     print("Serial connection closed!")
                ser.close()
                print("Serial connection closed!")

    def get_garden_info(self):
        return self.garden.get_garden_short_repr()

    def get_plants(self):
        return [pot.plant.name for pot in self.garden.get_pots()]

# helpers
def dumper(obj):
    try:
        return obj.toJSON()
    except:
        return obj.__dict__

def save_to_file(data,filename, write_mode, encoding):
    "Saving data to JSON file"
    try:
        with open(filename, write_mode, encoding=encoding) as f:
            json.dump(data, f, indent=4, default=dumper)
    except OSError as ex:
        print(f"OS Error writing to file: {ex}")
    except Exception as ex:
        print(f"Error writing to file: {ex}")

def load_from_file(filename):
    """Load data from JSON file"""
    try:
        with open(filename, "rt") as f:
            return json.load(f)
    except Exception as ex:
        print(f"Error reading file: {ex}")
        return None


