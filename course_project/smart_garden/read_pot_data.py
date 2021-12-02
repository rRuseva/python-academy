import json
from dataclasses import asdict

import serial
import datetime
import time
import config
import os.path
from sensor import SensorEntry, Sensor
from pot import Pot
from garden import Garden
from plant import Plant

# import Sensor # populate date directly int the classes !!!

"""Reading sensor information from one pot
    and saves it to JSON file with the name "pot_{pot_id}.json
    date is formed in a dictionary: 
        "pot_id" : pot_id,
        "entry_id" : entry_id,
        "timestamp" : date_time,
        "sensors_data" : {
            "sensor_name":value
        }
"""
def raed_sensor_data(pot, max_entry_counts = 3):
    pot_data = []
    try:
        # ser = serial.Serial('COM4', 9800, timeout=1)
        ser = serial.Serial(
            port = config.SERAIL_PORT,
            baudrate = config.SERIAL_BAUDRAT,
            write_timeout = config.SERAIL_WRITE_TIMEOUT
        )
        time.sleep(2)
        print(f"Serial connection to {config.SERAIL_PORT} is opened. ")

        sensor_count = pot.get_sensors_count()

        entry_count = 0

        while(ser.isOpen()):
            ct = datetime.datetime.now()

            for i in range(sensor_count):
                line = ser.readline()
                if line:
                    s_data = line.decode("utf-8")  # decode arduino data to utf-8 string
                    s_data = s_data.strip().split(": ")
                    print(s_data)
                    se = SensorEntry(s_data[1])
                    pot.sensors[i].update_sensor_data(se)

            entry_count += 1

            if entry_count == max_entry_counts:
                ser.close()
                print("Serial connection closed!")

    except serial.SerialException as er:
        print(f"1.Error opening port: {er}")
    # except Exception as e:
    #     print(f"2.Error: {e}")
    finally:
        ser.close()
        print("Serial connection is finally closed!")

    # print(pot_data)
    return pot_data

def format_data(entry:list):
    return {
        "pot_id" : entry[0],
        "entry_id" : entry[1],
        "timestamp" : entry[2],
        "sensors_data" : entry[3]
    }

def save_data_to_json(pot_data,filename, write_mode ):
    with open(filename, write_mode, encoding='utf-8') as f:
        json.dump(pot_data, f, indent=4)
    print(f"Data saved to {filename}")

if __name__ == '__main__':
    herbs = Plant("Herbs", 40,50, 22, 6, "")
    cherry_tomato = Plant("Cherry Tomatoes", 50, 70, 21, 8, "")

    herbs_pot = Pot("Herbs Pot", herbs, [Sensor("Soil Moisture"), Sensor("Light intensity")])
    cherry_tomato_pot = Pot("Cherry tomatoes", cherry_tomato,[Sensor("Soil Moisture"), Sensor("Light intensity")])

    my_garden = Garden("Home garden", "New", [herbs_pot, cherry_tomato_pot], (0.2, 0.2), "home" )


    raed_sensor_data(herbs_pot, 2)
    print(herbs_pot.sensors)
    print("--------------------")
    print(asdict(herbs_pot))
    filename = os.path.join(config.DATA_PATH, "pot_" + str(herbs_pot.pot_id)[:5] + ".json")
    if os.path.exists(filename):
        write_mode = 'a'
    else:
        write_mode = 'w'

    herbs_pot.save_to_file(filename,write_mode)
    # for s in range(herbs_pot.get_sensors_count()):
    #     herbs_pot.sensors[s].persist(filename, write_mode)
