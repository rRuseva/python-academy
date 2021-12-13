import os
from functools import partial
from tkinter import *
from tkinter import ttk, messagebox, font
from model.garden import Garden
from model.pot import Pot
from view.app_sensor_view import AppSensorView
import view.style_config as style
import utils.global_utils as gu
from utils.tkinter_utils import get_center_window_left_top

class AddPotDialog:
    def __init__(self, parent, garden_repository, application, pot, plants):
        self.application = application
        self.pot = pot
        self.parent = parent
        self.garden_repo = garden_repository

        self.pot_dlg = Toplevel(self.parent)
        self.pot_dlg.title("Add Pot")
        left, top = get_center_window_left_top(parent, style.MAIN_WIDTH/2, style.MAIN_HEIGHT*2/3)
        self.pot_dlg .geometry("+%d+%d" %(left//2,top))
        self.mainframe = ttk.Frame(self.pot_dlg, padding="10 10 10 10")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        # form model fields
        self.id = StringVar()
        ttk.Label(self.mainframe, text="ID", justify=CENTER).grid(column=0, row=0, sticky=(E, W))
        self.id_entry = ttk.Entry(self.mainframe, textvariable=self.id, width=40).grid(column=1, row=0, sticky=(E, W))
        self.id_errors = Label(self.mainframe, text="", justify=LEFT, fg='red')

        self.name = StringVar()
        ttk.Label(self.mainframe, text="name", justify=CENTER).grid(column=0, row=1, sticky=(E, W))
        self.name_entry = ttk.Entry(self.mainframe, textvariable=self.name, width=40).grid(column=1, row=1, sticky=(E, W))
        self.name_errors = Label(self.mainframe, text="", justify=LEFT, fg='red')

        self.plant = StringVar()
        ttk.Label(self.mainframe, text="plant", justify=CENTER).grid(column=0, row=2, sticky=(E, W))
        self.plant_cb = ttk.Combobox(self.mainframe, textvariable=self.plant)
        self.plant_cb["values"] = plants
        self.plant_cb["state"] = 'readonly'
        self.plant_cb.grid(column=1, row=2, sticky=(E, W))

        self.location = StringVar()
        ttk.Label(self.mainframe, text="location", justify=CENTER).grid(column=0, row=3, sticky=(E, W))
        self.location_entry = ttk.Entry(self.mainframe, textvariable=self.location, width=40).grid(column=1, row=3, sticky=(E, W))
        self.location_errors = Label(self.mainframe, text="", justify=LEFT, fg='red')

        self.dimensions = StringVar()
        ttk.Label(self.mainframe, text="dimensions", justify=CENTER).grid(column=0, row=4, sticky=(E, W))
        self.dimensions_entry = ttk.Entry(self.mainframe, textvariable=self.dimensions, width=40).grid(column=1, row=4, sticky=(E, W))
        self.dimensions_errors = Label(self.mainframe, text="", justify=LEFT, fg='red')

        # submit button
        self.submit_button = Button(self.mainframe, text="Submit", command=self.onSubmit, font=(style.FONT_FAMILY, 12), bg=style.COLOR2, fg="white", height=1, width=10)
        self.submit_button.grid(column=1, row=5, sticky=(E))

        # load from file button
        load_text = StringVar()
        load_btn = Button(self.mainframe, textvariable=load_text, command=self.onLoad, font=(style.FONT_FAMILY, 12), bg=style.COLOR2, fg="white", height=1, width=10)
        load_text.set("Load from file")
        load_btn.grid(column=1, row=6, sticky=(E))


        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=15, pady=15)

        self.pot_dlg.protocol("WM_DELETE_WINDOW", self.dismiss)
        self.pot_dlg.transient(self.parent )
        self.pot_dlg.wait_visibility()
        self.pot_dlg.grab_set()
        self.pot_dlg.wait_window()

    def select_plant(self):
        self.selected_plant =  self.plant.get()

    def onSubmit(self):
        self.plant_cb.bind('<<ComboboxSelected>>', self.select_plant() )
        pot = Pot(self.id.get(), self.name.get(), location=self.location.get(),
                 plant=self.selected_plant, dimensions=self.dimensions.get())
        print(pot)
        self.application.update_garden_pots(pot)
        self.dismiss()

    def onLoad(self):
        pot = self.application.load_pot_from_file()
        self.dismiss()

    def dismiss(self):
        self.pot_dlg.grab_release()
        self.pot_dlg.destroy()

    def select_plant_name(self,event):
        self.plant_entry.bind()
