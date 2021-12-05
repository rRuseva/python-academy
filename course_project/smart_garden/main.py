from model.garden import Garden
from model.pot import Pot
from model.plant import Plant
from model.sensor import Sensor
from dao.garden_repo import GardenRepository
import config
import os.path

from tkinter import *
from dao.garden_repo import GardenRepository
from view.app_main_window import AppMainWindow

if __name__ == '__main1__':
    pass
    # my_garden = Garden("Home garden")
    # garden_repo = GardenRepository(my_garden)
    # # print(type(my_garden))
    # # print(my_garden)
    # # herbs = Plant("Herbs", 40,50, 22, 6, "")
    # # # print(herbs)
    # cherry_tomato = Plant("Cherry Tomatoes", 50, 70, 21, 8, "")
    # #
    # # herbs_pot = Pot("Herbs Pot", herbs, [Sensor("Soil Moisture","%"), Sensor("Light intensity","")])
    # cherry_tomato_pot = Pot("Cherry tomatoes", cherry_tomato,[Sensor("Soil Moisture","%"), Sensor("Light intensity","")])
    # #
    # # my_garden.add_pot(herbs_pot)
    # my_garden.add_pot(cherry_tomato_pot)
    #
    # # reading pot sensors data:
    # # garden_repo.read_pot_sensors_data(herbs_pot, 3)
    # garden_repo.read_pot_sensors_data(cherry_tomato_pot, 1)
    #
    # # saving / updating data files
    # garden_repo.save_garden_data()
    # garden_repo.update_garden_pots()


    # dirname = os.path.join(config.DATA_PATH, "Home_garden")
    # filename = os.path.join(dirname, "Home_garden.json")
    # #
    # garden_repo.load_garden_data_from_file(filename)
    # print("my garden pots: ", garden_repo.garden.pots)

    # print(garden_repo.garden.__str__)
    # print(garden_repo.garden.pots[1].sensors[0].sensor_data)

    # # print(herbs_pot.sensors)
    # print("--------------------")
    # # print(asdict(herbs_pot))
    # filename = os.path.join(config.DATA_PATH, "pot_" + str(herbs_pot.name).replace(" ", "_")  + ".json")  #+ str(herbs_pot.pot_id)[:5]
    # if os.path.exists(filename) and os.path.getsize(filename) != 0:
    #     herbs_pot.update_pot_date(filename)
    # else:
    #     herbs_pot.save_pot_to_file(filename)

if __name__ == '__main__':
    dirname = os.path.join(config.DATA_PATH, "Home_garden")
    filename = os.path.join(dirname, "Home_garden.json")

    garden_repo = GardenRepository(garden_path=dirname)



    garden_repo.load_garden_data_from_file(filename)
