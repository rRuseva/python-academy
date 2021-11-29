import json
import serial
import datetime
import time
import config
import os.path
# pot_data = []

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
def raed_sensor_data( entry_counts = 3):
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
        entry_id = 0
        pot_id = -1

        while(ser.isOpen()):
            ct = datetime.datetime.now()
            line = ser.readline()
            sensors_data = {}
            if line:
                entry_id += 1
                s_data = line.decode("utf-8")  # decode arduino data to utf-8 string
                s_data = s_data.strip().split(", ")
                print(s_data)
                pot_id = s_data[0].split(":")[1].strip()
                for data in s_data [1:]:
                    data = data.split(':')
                    sensors_data[data[0]] = data[1]
                # print([pot_id, entry_id, ct, sensors_data])
            pot_data.append(format_data([pot_id, entry_id, ct.__str__(), sensors_data]))

            if entry_id == entry_counts:
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
    pot_data = raed_sensor_data(5)

    if pot_data:
        pot_id = pot_data[0]["pot_id"]
        filename = os.path.join(config.DATA_PATH, "pot_" + str(pot_id) + ".json")
        if os.path.exists(filename):
            write_mode = 'a'
        else:
            write_mode = 'w'
        save_data_to_json(pot_data, filename, write_mode)
