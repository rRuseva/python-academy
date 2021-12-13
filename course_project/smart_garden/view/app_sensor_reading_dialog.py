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

class SensorRadingsDialog:
    def __init__(self, parent, garden_repository, application, pot):
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


        self.port = StringVar()
        self.readings_count = StringVar()
        # self.reset()

        ttk.Label(self.mainframe, text="port", state=DISABLED, justify=CENTER).grid(column=0, row=0, sticky=(E, W))
        ttk.Label(self.mainframe, text="readings_count", justify=CENTER).grid(column=0, row=1, sticky=(E, W))

        self.port_entry = ttk.Entry(self.mainframe, textvariable=self.port, width=40).grid(column=1, row=0, sticky=(E, W))
        self.readings_count_entry = ttk.Entry(self.mainframe, textvariable=self.readings_count, width=40).grid(column=1, row=1, sticky=(E, W))

        self.port_errors = Label(self.mainframe, text="", justify=LEFT, fg='red').grid(column=2, row=0, sticky=(E, W))
        self.readings_count_errors = Label(self.mainframe, text="", justify=LEFT, fg='red').grid(column=2, row=1, sticky=(E, W))




        # load from file button
        load_text = StringVar()
        load_btn = Button(self.mainframe, textvariable=load_text, command=self.on_start, font=(style.FONT_FAMILY, 12), bg=style.COLOR2, fg="white", height=1, width=10)
        load_text.set("Start")
        load_btn.grid(column=1, row=6, sticky=(E))


        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=15, pady=15)

        self.pot_dlg.protocol("WM_DELETE_WINDOW", self.dismiss)
        self.pot_dlg.transient(self.parent )
        self.pot_dlg.wait_visibility()
        self.pot_dlg.grab_set()
        self.pot_dlg.wait_window()


    def on_start(self):
        readings_count = self.readings_count.get()
        port = self.port.get()

        print(self.pot)
        exit_state = self.application.start_readings(self.pot, readings_count, port)
        if(exit_state):
            self.dismiss()


    def dismiss(self):
        self.pot_dlg.grab_release()
        self.pot_dlg.destroy()

