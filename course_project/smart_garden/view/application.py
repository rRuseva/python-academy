from dao.garden_repo import GardenRepository
import config
import os.path

from tkinter import *
from view.app_main_window import AppMainWindow
# from view.add_garden_dialog import AddGardenDialog

class Application:
    def __init__(self, garden_repository = GardenRepository(), db_file = None):
        self.garden_repository = garden_repository
        self.db_file = db_file

    def start(self):
        self.garden_repository.load_garden_data_from_file(self.db_file)
        self.root = Tk()
        self.main_window = AppMainWindow(self.root, self)

        self.root.mainloop()

    # def addGarden(self):
    #     self.add_book_dialog = AddGardenDialog(self.root, books_repo=self.book_repository)
