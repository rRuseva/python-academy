js_data = {
    "pot_id": "1dd9b9cf-3429-4ac0-8a6c-d9916f40bf22",
    "pot_name": "Herbs Pot",
    "plant": {
        "id": 1,
        "name": "Herbs",
        "humidity": 40,
        "soil_moisture": 50,
        "temperature": 22,
        "light_levels": 80
    },
    "location": None,
    "notes": None,
    "measurements": [
        [
            {
                "sensor_name": "Soil Moisture",
                "sensor_id": "768dc5a8-9f60-4b15-af08-836a4679e4d0",
                "data_units": "%",
                "entry": {
                    "entry_id": 1001,
                    "value": "130",
                    "timestamp": "05/12/2021 18:58:20"
                }
            },
            {
                "sensor_name": "Light intensity",
                "sensor_id": "22faf2ed-c430-4a28-9a7e-ec414186d105",
                "data_units": "",
                "entry": {
                    "entry_id": 2001,
                    "value": "72",
                    "timestamp": "05/12/2021 18:58:20"
                }
            }
        ],
        [
            {
                "sensor_name": "Soil Moisture",
                "sensor_id": "768dc5a8-9f60-4b15-af08-836a4679e4d0",
                "data_units": "%",
                "entry": {
                    "entry_id": 1002,
                    "value": "616",
                    "timestamp": "05/12/2021 18:58:20"
                }
            },
            {
                "sensor_name": "Light intensity",
                "sensor_id": "22faf2ed-c430-4a28-9a7e-ec414186d105",
                "data_units": "",
                "entry": {
                    "entry_id": 2002,
                    "value": "84",
                    "timestamp": "05/12/2021 18:58:20"
                }
            }
        ],
        [
            {
                "sensor_name": "Soil Moisture",
                "sensor_id": "768dc5a8-9f60-4b15-af08-836a4679e4d0",
                "data_units": "%",
                "entry": {
                    "entry_id": 1003,
                    "value": "637",
                    "timestamp": "05/12/2021 18:58:20"
                }
            },
            {
                "sensor_name": "Light intensity",
                "sensor_id": "22faf2ed-c430-4a28-9a7e-ec414186d105",
                "data_units": "",
                "entry": {
                    "entry_id": 2003,
                    "value": "89",
                    "timestamp": "05/12/2021 18:58:20"
                }
            }
        ]
    ]
}
from pandas import DataFrame

if __name__ == "__main__":
	sm_d = []
	l_d =[]
	
	for e in js_data["measurements"]:
	  	sm_d.append(e[0])
	  	l_d.append(e[1])
	print(sm_d)
#	print(sm_d["entry"]["timestamp"]])
	s1_t = [x["entry"]["timestamp"] for x in sm_d]
	 #zip(sm_d["timestamp"], sm_d["value"])
	print(s1_t)
	s1_v = [x["entry"]["value"] for x in sm_d]
	
	data = {"time" : s1_t,
	"value" : s1_v
	}
	
	print(data)
	df2 = DataFrame(data,columns=["time","value"])
print (df2)