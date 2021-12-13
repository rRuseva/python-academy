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
        # self.size = root.grid_size()
        left, top = get_center_window_left_top(root, style.MAIN_WIDTH, style.MAIN_HEIGHT)
        # root.geometry(f"{style.MAIN_WIDTH}x{style.MAIN_HEIGHT}+{left//2}+{top}")
        root.geometry("+%d+%d" %(left//2,top))
        root.minsize(style.MAIN_WIDTH,style.MAIN_HEIGHT)
        root.maxsize(style.MAX_WIDTH, style.MAX_HEIGHT)
        root.attributes('-alpha',0.5)

        self.grid(row=0, column=0, columnspan=3, rowspan=5, sticky=(N, W, E, S) ) #columnspan=5,
        # self.frame_size = self.mainframe.grid_size()

        self.canvas_root = Canvas(root, width=style.MAIN_WIDTH, height=style.MAIN_HEIGHT)
        self.canvas_root.create_window(0,0, anchor="center")
        # self.canvas_root.grid(row=0, column=0)
        self.canvas_root.grid(row=0, column=0, columnspan=3, rowspan=5, sticky=(N, W, E, S) )
        # self.canvas_root.attributes('-alpha',0.5)

        # # ### set  logo as background image
        self.set_background_image(root)

        # # add a vertical scrollbar
        self.scrollbar = ttk.Scrollbar(self.canvas_root, orient=VERTICAL)
        self.scrollbar.grid(column=3, row=0, rowspan=5, sticky=(N,S) )
        self.scrollbar.config(command=self.canvas_root.yview)
        self.canvas_root.config(yscrollcommand=self.scrollbar.set)
        # self.canvas_root.grid()


    def set_background_image(self, root):
        self.logo_img = Image.open(os.path.join(config.ASSETS_PATH,'logo4.png'))
        self.logo_img = self.logo_img.resize(style.LOGO_SIZE)
        self.logo = ImageTk.PhotoImage(self.logo_img)
        self.label_logo = ttk.Label(root, image=self.logo)
        self.label_logo.grid(column=3, row=5,sticky=(S,E))
        # self.label_logo.place(x=0, y=0, relwidth=1, relheight=1)
        # self.label_logo.place(x=(style.MAIN_WIDTH-style.LOGO_SIZE[0]), y=(style.MAIN_HEIGHT-style.LOGO_SIZE[1]), relwidth=1, relheight=1)
        #
        # print(style.MAIN_WIDTH-style.LOGO_SIZE[0])
        # self.label_logo.place(x=(self.size[0]-style.LOGO_SIZE[0]), y=(self.size[1]-style.LOGO_SIZE[1]), relwidth=1, relheight=1)

