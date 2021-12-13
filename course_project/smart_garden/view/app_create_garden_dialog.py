import os
import datetime
from functools import partial
from tkinter import *
from tkinter import ttk
from model.garden import Garden
import view.style_config as style
import utils.global_utils as gu
from utils.tkinter_utils import get_center_window_left_top

class CreateGardenDialog:
    def __init__(self, parent, garden_repository, application):
        self.application = application
        self.parent = parent
        self.garden_repo = garden_repository
        self.garden_dlg = Toplevel(parent)
        self.garden_dlg.title("Add Garden")
        left, top = get_center_window_left_top(parent, style.MAIN_WIDTH/2, style.MAIN_HEIGHT*2/3)
        self.garden_dlg .geometry("+%d+%d" %(left//2,top))
        self.mainframe = ttk.Frame(self.garden_dlg, padding="10 10 10 10")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        # form model fields
        # self.id = StringVar()
        # ttk.Label(self.mainframe, text="ID", justify=CENTER).grid(column=0, row=0, sticky=(E, W))
        # self.id_entry = ttk.Entry(self.mainframe, textvariable=self.id, width=40).grid(column=1, row=0, sticky=(E, W))
        # self.id_errors = Label(self.mainframe, text="", justify=LEFT, fg='red')

        self.name = StringVar()
        ttk.Label(self.mainframe, text="name", justify=CENTER).grid(column=0, row=1, sticky=(E, W))
        self.name_entry = ttk.Entry(self.mainframe, textvariable=self.name, width=40).grid(column=1, row=1, sticky=(E, W))
        self.name_errors = Label(self.mainframe, text="", justify=LEFT, fg='red')

        self.status = StringVar()
        ttk.Label(self.mainframe, text="status", justify=CENTER).grid(column=0, row=2, sticky=(E, W))
        self.status_cb = ttk.Combobox(self.mainframe, textvariable=self.status)
        self.status_cb["values"] = ["new"]
        self.status_cb["state"] = 'readonly'
        self.status_cb.grid(column=1, row=2, sticky=(E, W))

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

        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=15, pady=15)

        self.garden_dlg.protocol("WM_DELETE_WINDOW", self.dismiss)
        self.garden_dlg.transient(self.parent )
        self.garden_dlg.wait_visibility()
        self.garden_dlg.grab_set()
        self.garden_dlg.wait_window()

    def select_status(self):
        self.selected_statust =  self.status.get()

    def onSubmit(self):
        self.status_cb.bind('<<ComboboxSelected>>', self.select_status() )
        garden = Garden(self.name.get(), location=self.location.get(),
                        dimensions=self.dimensions.get())
        print(garden)
        self.application.set_garden(garden)
        self.dismiss()

    def dismiss(self):
        self.garden_dlg.grab_release()
        self.garden_dlg.destroy()
