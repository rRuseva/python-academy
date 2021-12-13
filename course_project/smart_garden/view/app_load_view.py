import os
from tkinter import *
from tkinter import ttk, messagebox, font

from PIL import Image, ImageTk

import config
import view.style_config as style
from utils.tkinter_utils import get_center_window_left_top


class AppMainWindow(ttk.Frame):
    def __init__(self, root, application, name = "SmartGarden"):
        super().__init__(root, padding="10 10 10 10")
        self.application = application

        self.name = name
        root.title(self.name)
        self.size = self.grid_size()
        left, top = get_center_window_left_top(root, style.MAIN_WIDTH, style.MAIN_HEIGHT)
        # root.geometry(f"{MAIN_WIDTH}x{MAIN_HEIGHT}+{left//2}+{top}")
        root.geometry("+%d+%d" %(left//2,top))
        root.minsize(style.MAIN_WIDTH,style.MAIN_HEIGHT)
        # self.attributes('-alpha',0.5)

        self.grid(row=0, column=0, sticky=(N, W, E, S) ) #columnspan=5,
        # self.frame_size = self.mainframe.grid_size()

        # load button
        instructions_load = Label(self, text="Select your garden file! ", fg=style.FONT_FG, font=style.FONT)
        instructions_load.grid(columnspan=3, column=0, row=1)
        load_text = StringVar()
        load_btn = Button(self, textvariable=load_text, command=self.application.load_garden, font=(style.FONT_FAMILY, 18), bg=style.COLOR2, fg="white", height=2, width=15)
        load_text.set("Load Garden")
        load_btn.grid(column=0, row=2)

        # create new button
        instructions_create = Label(self, text="Create new garden! ", fg=style.FONT_FG, font=style.FONT)
        instructions_create.grid(columnspan=3, column=0, row=3)
        create_text = StringVar()
        create_btn = Button(self, textvariable=create_text, command=self.application.create_garden, font=(style.FONT_FAMILY, 18), bg=style.COLOR2, fg="white", height=2, width=15)
        create_text.set("Create Garden")
        create_btn.grid(column=0, row=4)

        for child in self.winfo_children():
            if child.winfo_class() == "Label":
                child.grid_configure(padx=8, pady=3)
            if child.winfo_class() == "Button":
                child.grid_configure(padx=8, pady=8)

