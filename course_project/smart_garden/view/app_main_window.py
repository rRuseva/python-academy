import os
from tkinter import *
from tkinter import ttk, messagebox

from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

import config
from dao.garden_repo import GardenRepository
# from view.add_garden_dialog import AddGardenDialog
from utils.tkinter_utils import get_ceter_window_left_top


MAIN_WIDTH = 800
MAIN_HEIGHT = 600

LOGO_SIZE = (MAIN_WIDTH*3//4, MAIN_HEIGHT*3//4)


class AppMainWindow:
    def __init__(self, root, application, name):
        self.application = application
        self.root = root
        self.name = name
        name = "SmartGarden"
        self.root.title(self.name)
        self.root.option_add('*tearOff', FALSE) # remove menu tear off ability
        left, top = get_ceter_window_left_top(self.root, MAIN_WIDTH, MAIN_HEIGHT)
        self.root.geometry(f"{MAIN_WIDTH}x{MAIN_HEIGHT}+{left//2}+{top}")
        self.mainframe = ttk.Frame(self.root, padding="3 3 3 3", width=MAIN_WIDTH, height=MAIN_HEIGHT)
        self.mainframe.grid(columnspan=2, rowspan=3,column=0, row=0, sticky=(N, W, E, S) )
        self.frame_size = self.mainframe.grid_size()

        self.menu_bar = Menu(self.root)
        self.root['menu'] = self.menu_bar

        # # File menu
        # menu_file = Menu(self.menu_bar)
        # self.menu_bar.add_cascade(menu=menu_file, label="File", underline=0)
        # menu_file.add_command(label='New', command = self.newFile, underline=0, accelerator="Alt+N")
        # self.mainframe.bind("<Alt-N>", self.newFile)
        # menu_file.add_command(label="Open ...", command = self.openFile)
        # menu_file.add_command(label='Close', command = self.closeFile)
        # menu_file.entryconfigure('Close', state=DISABLED)

        # Garden menu
        menu_garden = Menu(self.menu_bar)
        self.menu_bar.add_cascade(menu=menu_garden, label="Garden", underline=0)
        # menu_garden.add_command(label='Load', command=self.onLoadGarden, underline=0)
        # menu_garden.add_command(label='Edit', command=self.onEditGarden, underline=0)

        # self.canvas = Canvas(self.mainframe, width=MAIN_WIDTH, height=MAIN_HEIGHT)
        # self.canvas.grid(columnspan=3, rowspan=4)

        #logo
        self.logo_img = Image.open(os.path.join(config.ASSETS_PATH,'logo.gif'))
        self.logo_img = self.logo_img.resize(LOGO_SIZE)
        self.logo = ImageTk.PhotoImage(self.logo_img)
        self.label_logo = ttk.Label(self.mainframe, image=self.logo)
        self.label_logo.grid(columnspan=2, rowspan=3, column=2, row=3,sticky=(S,E))
        # label_logo.image = self.logo

        #instructions
        instructions = ttk.Label(self.mainframe, text="Select a garden to load")
        instructions.grid(columnspan=2, column=0, row=1)

        #browse button
        browse_text = StringVar()
        browse_btn = Button(self.mainframe, textvariable=browse_text, command=self.onLoadGarden, font="Arial", bg="#20bebe", fg="white", height=2, width=15)
        browse_text.set("Load Garden")
        browse_btn.grid(column=0, row=2)

        # canvas = Canvas(self.root, width=600, height=250)
        # canvas.grid(columnspan=3)

    # def onNewGarden(self):
    #     self.application.addGarden()
    #
    def onLoadGarden(self):
        file = askopenfile(parent=self.mainframe, mode='rb', title="Choose a file",
                           initialdir=config.DATA_PATH, filetypes=[("JSON file", "*.json")])

        if file:
            self.application.garden_filename = os.path.abspath(file.name)
            print("loaded file is: ", self.application.garden_filename)
            self.application.load_garden_repo()
            self.name = os.path.basename( self.application.garden_filename).split(".")[0]
            print('name: ', self.name)
            print(self.application.garden_repository)
            # self.show_garden_view = ShowGardenView(self.self.root, entity_cls=Garden ,garden_repo=self.g)

    # def onEditGarden(self):
    #     messagebox.showinfo(title="File Open Dialog", message="Opening DB file ...")

    # def closeFile(self):
    #     messagebox.showinfo(title="File Close Dialog", message="Closing DB file ...")



