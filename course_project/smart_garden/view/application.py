from dao.garden_repo import GardenRepository
from model.garden import Garden
import config
# from view.add_garden_dialog import AddGardenDialogfrom presentation.add_book_dialog import AddBookDialog
from view.show_garden_view import ShowGardenView
from view.app_main_window import AppMainWindow

import os.path
from tkinter import *
from pandas import DataFrame



class Application:
    def __init__(self, garden_name = None, db_file = None):
        self.garden_name = garden_name
        self.garden_filename = db_file
        self.garden_repository = GardenRepository(garden_name, db_file)
        self.logo_img = Image.open(os.path.join(config.ASSETS_PATH,'logo.gif'))

    def start(self):

        self.root = Tk()
        self.main_window = AppMainWindow(self.root, self, name="Smart Garden")

        self.root.mainloop()

    def load_garden_repo(self):
        self.garden_repository.load_garden_data_from_file(self.garden_filename)

    # def show_sensor_data_plot(self):
    #     df = self.garden_repository.garden.p
    # def addGarden(self):
    #     self.add_book_dialog = AddGardenDialog(self.root, books_repo=self.book_repository)
