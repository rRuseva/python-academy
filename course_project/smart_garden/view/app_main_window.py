from tkinter import *
from tkinter import ttk, messagebox

from dao.garden_repo import GardenRepository
# from view.add_garden_dialog import AddGardenDialog
from utils.tkinter_utils import get_ceter_window_left_top

MAIN_WIDTH = 800
MAIN_HEIGHT = 600


class AppMainWindow:
    def __init__(self, root, application):
        self.application = application

        root.title("Garden")
        print(f"Windowing system: {root.tk.call('tk', 'windowingsystem')}") # return  x11, win32, aqua
        root.option_add('*tearOff', FALSE) # remove menu tear off ability
        left, top = get_ceter_window_left_top(root, MAIN_WIDTH, MAIN_HEIGHT)
        root.geometry(f"{MAIN_WIDTH}x{MAIN_HEIGHT}+{left}+{top}")
        self.mainframe = ttk.Frame(root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S) )

        self.menu_bar = Menu(root)
        root['menu'] = self.menu_bar

        # File menu
        menu_file = Menu(self.menu_bar)
        self.menu_bar.add_cascade(menu=menu_file, label="File", underline=0)
        menu_file.add_command(label='New', command = self.newFile, underline=0, accelerator="Alt+N")
        self.mainframe.bind("<Alt-N>", self.newFile)
        print(menu_file.entryconfigure(0))
        menu_file.add_command(label="Open ...", command = self.openFile)
        menu_file.add_command(label='Close', command = self.closeFile)
        menu_file.entryconfigure('Close', state=DISABLED)

        # Books menu
        menu_garden = Menu(self.menu_bar)
        self.menu_bar.add_cascade(menu=menu_garden, label="Garden", underline=0)
        menu_garden.add_command(label='New', command=self.onNewGarden, underline=0)

    def onNewGarden(self):
        self.application.addGarden()

    def newFile(self):
        messagebox.showinfo(title="New File Dialog", message="Creating DB file ...")

    def openFile(self):
        messagebox.showinfo(title="File Open Dialog", message="Opening DB file ...")

    def closeFile(self):
        messagebox.showinfo(title="File Close Dialog", message="Closing DB file ...")



