import os
from functools import partial
from tkinter import *
from tkinter import ttk, messagebox, font
from model.garden import Garden
from model.pot import Pot
from view.app_sensor_view import AppSensorView
import view.style_config as style
import utils.global_utils as gu

class AppPotView(ttk.Frame):
    def __init__(self, parent, application, pot):
        super().__init__(parent, padding="10 10 10 10")
        self.parent = parent
        self.pot = pot
        self.grid(row=0, column=0,columnspan=8, sticky=(N, W, E, S) ) #columnspan=5,

        ### Displey pot info
        info = gu.dict_repr(self.pot.short_repr())
        pot_name = StringVar()
        pot_name.set(f"{pot.name:<20.20}")
        self.label_pot_name = Label(self, textvariable=pot_name, font=(style.FONT_FAMILY, 18, 'bold'), fg=style.COLOR2, justify='left')
        self.label_pot_name.grid(columnspan=5, column=0, row=0)

        start_readings = StringVar()
        readings_btn = Button(self, textvariable=start_readings, command=partial(application.start_readings,pot, 1), font=(style.FONT_FAMILY, 10), bg=style.COLOR2, fg="white", height=2, width=10)
        start_readings.set("Start Readings")
        readings_btn.grid(column=6, row=0, sticky=(N,E))

        pot_info_text = StringVar()
        pot_info_text.set(info)
        self.label_pot_info = Label(self, textvariable=pot_info_text, font=style.FONT, fg=style.FONT_FG,justify='left')
        self.label_pot_info.grid(columnspan=5, column=0, row=1)

        self.sensors = pot.get_sensors()

        for i, sensor in enumerate(self.sensors):
            frame = Frame(self, width=style.MAIN_WIDTH,)
            frame.grid(column=i, row=2)
            self.pot_view = AppSensorView(frame, sensor)
