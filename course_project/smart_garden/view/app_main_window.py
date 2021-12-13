import os
from tkinter import *
from tkinter import ttk, font

from PIL import Image, ImageTk

import config
import view.style_config as style
from utils.tkinter_utils import get_center_window_left_top

class AppRootWindow(ttk.Frame):
    def __init__(self, root, application, name = "SmartGarden"):
        super().__init__(root, padding="10 10 10 10")
        self.application = application

        self.name = name
        root.title(self.name)
        self.size = self.grid_size()
        left, top = get_center_window_left_top(root, style.MAIN_WIDTH, style.MAIN_HEIGHT)
        # root.geometry(f"{style.MAIN_WIDTH}x{style.MAIN_HEIGHT}+{left//2}+{top}")
        root.geometry("+%d+%d" %(left//2,top))
        root.minsize(style.MAIN_WIDTH,style.MAIN_HEIGHT)
        root.maxsize(style.MAX_WIDTH, style.MAX_HEIGHT)
        root.attributes('-alpha',0.5)

        self.grid(row=0, column=0,  sticky=(N, W, E, S) ) #columnspan=5,
        # self.frame_size = self.mainframe.grid_size()

        self.canvas_root = Canvas(root, width=self.size[0], height=self.size[1])
        self.canvas_root.create_window(0,0, anchor="center")
        self.canvas_root.grid(row=0, column=0)

        # # ### background logo with label
        self.logo_img = Image.open(os.path.join(config.ASSETS_PATH,'logo2.png'))

        self.logo_img = self.logo_img.resize(style.LOGO_SIZE)
        self.logo = ImageTk.PhotoImage(self.logo_img)
        self.label_logo = ttk.Label(root, image=self.logo)
        self.label_logo.grid(column=15, row=4,sticky=(S,E))
        # self.label_logo.place(x=(style.MAIN_WIDTH-style.LOGO_SIZE[0]), y=(style.MAIN_HEIGHT-style.LOGO_SIZE[1])) #, relwidth=1, relheight=1)

        # # add a vertical scrollbar
        self.scrollbar = ttk.Scrollbar(self.canvas_root, orient=VERTICAL)
        self.scrollbar.grid(column=15, row=0, rowspan=17, sticky=(N,S) )
        self.scrollbar.config(command=self.canvas_root.yview)
        self.canvas_root.config(yscrollcommand=self.scrollbar.set)
        self.canvas_root.grid()


