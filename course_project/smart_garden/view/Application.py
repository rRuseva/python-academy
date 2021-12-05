from dao.garden_repo import GardenRepository
import config
import os.path

from tkinter import *
from view.app_main_window import AppMainWindow
# from view.add_garden_dialog import AddGardenDialog

class Application:
    def __init__(self, book_repository = BookRepositoryJson()):
        self.book_repository = book_repository

    def start(self):
        self.book_repository.load()
        self.root = Tk()
        self.main_window = AppMainWindow(self.root, self)

        self.root.mainloop()

    def addBook(self):
        self.add_book_dialog = AddBookDialog(self.root, books_repo=self.book_repository)
