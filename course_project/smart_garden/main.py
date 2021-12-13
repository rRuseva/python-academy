from model.sensor import SensorEntry, Sensor
from model.pot import Pot
from model.garden import Garden
from model.plant import Plant
from dao.garden_repo import GardenRepository
import config
import os.path
from pandas import DataFrame
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import Subplot
from view.application import Application
import utils.global_utils as utils


if __name__ == '__main1__':
    """console app"""
    ### read data and create garden

    # my_garden = Garden("My mini grocery", dimensions=(40,40), location="Sofia")
    # garden_repo = GardenRepository("My mini grocery")
    # # # print(type(my_garden))
    # # print(my_garden)
    # herbs = Plant("Herbs", 40,50, 22, 6, "")
    # # # # print(herbs)
    # cherry_tomato = Plant("Cherry Tomatoes", 50, 70, 24, 8, notes="Doesn't like direct sunlight.")
    # # #
    # herbs_pot = Pot("Herbs Pot", herbs, [Sensor("Soil Moisture","%"), Sensor("Light intensity","luminous intensity")], dimensions=(20,20), location="South window")
    # cherry_tomato_pot = Pot("Cherry tomatoes", cherry_tomato,[Sensor("Soil Moisture","%"), Sensor("Light intensity","luminous intensity")], dimensions=(20,20), location="Balcony")
    # #
    # my_garden.add_pot(herbs_pot)
    # my_garden.add_pot(cherry_tomato_pot)
    # #
    # # # reading pot sensors data:
    # # garden_repo.read_pot_sensors_data(herbs_pot, 15)
    # garden_repo.read_pot_sensors_data(cherry_tomato_pot, 15)
    # #
    # # # saving / updating data files
    # # garden_repo.save_garden_data()
    # garden_repo.update_garden_pots()


    ### load new created garden
    # dirname = os.path.join(config.DATA_PATH, "Home_garden")
    # filename = os.path.join(dirname, "Home_garden.json")
    # print("garden, ", garden_repo.garden_path)
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

###gui app
if __name__ == '__main__':
    garden_name = "My mini grocery"
    garden_dirname = os.path.join(config.DATA_PATH, utils.construct_filename(garden_name))
    garden_filename = os.path.join(garden_dirname, utils.generate_file_path(garden_name, ""))

    # garden_repo = GardenRepository("Home_garden", garden_filename)
    # garden_repo.load_garden_data_from_file(garden_filename)
    #
    # print("My 'Home Garden'")
    # # print(garden_repo.garden.__repr__())
    # pot = garden_repo.garden.pots[0]
    # sensor = pot.sensors[0]


    # app = Application(db_file=garden_filename)
    app = Application()
    app.start()
