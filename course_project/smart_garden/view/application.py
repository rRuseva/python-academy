from dao.garden_repo import GardenRepository
from model.garden import Garden
import config
import serial

from model.pot import Pot
from utils import global_utils as gu
from view.app_create_garden_dialog import CreateGardenDialog
from view.app_garden_view import AppGardenView
from view.app_load_view import AppMainWindow
from view.app_main_window import AppRootWindow
from view.app_add_pot_dialog import AddPotDialog
from model.garden import Garden
import os.path
from tkinter import *
from tkinter import  messagebox
from tkinter.filedialog import askopenfile
from pandas import DataFrame



class Application:
    def __init__(self, garden_name = None, db_file = None):
        self.garden_name = garden_name
        self.garden_filename = db_file
        self.garden_repository = GardenRepository(garden_name, db_file)
        # self.logo_img = Image.open(os.path.join(config.ASSETS_PATH,'logo.gif'))

    def start(self):
        self.root = Tk()
        self.main_window = AppRootWindow(self.root, self, name=self.garden_name)
        if self.garden_filename is not None:
            self.garden_name = gu.extract_name(self.garden_filename)
            self.load_garden_repo()
            self.main_window = AppGardenView(self.root, self, name=self.garden_name)
        else:
            self.main_window = AppMainWindow(self.root, self, name="Smart Garden")

        self.root.mainloop()

    def load_garden(self):
        """Opens file dialog and loads garden data from it """
        file = askopenfile(parent=self.root, mode='rb', title="Choose a file",
                           initialdir=config.DATA_PATH, filetypes=[("JSON file", "*.json")])

        if file:
            self.garden_filename = os.path.abspath(file.name)
            print("loaded file is: ", self.garden_filename)
            self.garden_repository.load_garden_data_from_file(self.garden_filename)
                # load_garden_repo()
            # self.name = os.path.basename( self.garden_filename).split(".")[0]
            self.garden_name = gu.extract_name(self.garden_filename)
            print('loaded garden name: ', self.garden_name)
            print('pots_count', self.garden_repository.pots_count())
            # print(self.garden_repository)
            AppGardenView(self.root, self, name=self.garden_name)

    def load_garden_repo(self):
        """ Loads garden data from file"""
        self.garden_repository.load_garden_data_from_file(self.garden_filename)

    def reload_garden(self):
        self.main_window = AppGardenView(self.root, self, name=self.garden_name)

    def create_garden(self):
        """Calls dialog view for creating new garden"""
        self.create_garden_dialog = CreateGardenDialog(self.root, application=self,  garden_repository=self.garden_repository)

    def edit_garden(self):
        """Calls dialog view for editing garden"""
        print("call edit garden dialog")
    #
    # def addGarden(self):
    #     """ Calls add dialog view """

    def set_garden(self, garden):
        """set new garden for the repository"""
        self.garden_repository.set_garden(garden)
        self.save_garden_repo()

    def get_garden_info(self):
        """returns string representation ofmaingardenattributes"""
        info = self.garden_repository.get_garden_info()
        name = info['name']
        text = f"Status: {info['status']:<20.20s}\t" \
               f"Date created: {info['date_created']:<20.20s}\t\t" \
               f"Dimensions: {info['dimensions'][0] if info['dimensions'] else '0'}x{info['dimensions'][1] if info['dimensions'] else '0'} meters\t\t"\
               f"Location: {info['location'] if info['location'] else ' ':<20.20}\n"
        return (name,text)

    def get_garden_data(self):
        """returns full garden object"""
        return self.garden_repository.garden


    def start_readings(self, pot, numb_readings):
        try:
            self.garden_repository.read_pot_sensors_data(pot, numb_readings)
            self.garden_repository.update_garden_pots()
        except serial.SerialException as er:
            messagebox.showinfo(title="Error reading", message=er)

    def add_new_pot(self):
        self.plants = self.garden_repository.get_plants()
        self.add_pot_dialog = AddPotDialog(self.root, garden_repository=self.garden_repository,
                                          application=self, pot = Pot(name=""), plants=self.plants )

    def load_pot_from_file(self):
        pot = Pot(name="")
        file = askopenfile(parent=self.root, mode='rb', title="Choose a file",
                           initialdir=config.DATA_PATH, filetypes=[("JSON file", "*.json")])
        if file:
            pot_filename = os.path.abspath(file.name)
            print("loaded file is: ", pot_filename)
            self.garden_repository.load_pot_data_from_file(pot_filename, pot)
            pot_name = gu.extract_name(pot_filename)
            print('loaded pot name: ', pot_name)
            self.update_garden_pots(pot)
            self.save_garden_repo()

    def update_garden_pots(self, pot):
        self.garden_repository.garden.add_pot(pot)
        print("new pots count:")
        print(len(self.garden_repository.garden.get_pots()))
        self.reload_garden()

    def save_garden_repo(self):
        ### do checks for repos path and filenames
        self.garden_repository.save_garden_data()
