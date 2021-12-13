import os
from tkinter import *
from tkinter import ttk

import matplotlib

from model.sensor  import Sensor
import view.style_config as style
import utils.global_utils as gu

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

class AppSensorView(ttk.Frame):
    def __init__(self, parent, sensor):
        super().__init__(parent, padding="2 5 2 5")
        self.parent = parent
        self.sensor = sensor
        self.grid(row=0, column=0, sticky=(N, W, E, S) ) #columnspan=5,

        ### Displey pot info
        info = gu.dict_repr(self.sensor.short_repr())
        sensor_name = StringVar()
        sensor_name.set(f"{sensor.name:<20.20}")
        self.label_sensor_name = Label(self, textvariable=sensor_name, font=(style.FONT_FAMILY, 18, 'bold'), fg=style.COLOR2, justify='left')
        self.label_sensor_name.grid(columnspan=5, column=0, row=0)

        sensor_info_text = StringVar()
        sensor_info_text.set(info)
        self.label_sensor_info = Label(self, textvariable=sensor_info_text, font=style.FONT, fg=style.FONT_FG,justify='left')
        self.label_sensor_info.grid(columnspan=5, column=0, row=1)

        # create_text = StringVar()
        # create_btn = Button(self, textvariable=create_text, command=self.show_graph, font=(style.FONT_FAMILY, 18), bg=style.COLOR2, fg="white", height=2, width=15)
        # create_text.set("Show Graphs")
        # create_btn.grid(column=0, row=2)

        ### show data grafs
        sd = sensor.get_data_frame()
        self.show_graph(sd, sensor.name)


        # # add a vertical scrollbar
        # vsb = ttk.Scrollbar(parent, orient="vertical", command=self.parent.yview)
        # vsb.grid(row=0, column=1, sticky=(N, W, S), padx=0)
        # self.parent.configure(yscrollcommand=vsb.set)

    def show_graph(self, sd, title ):
        self.df = pd.DataFrame(sd['value'], index=sd['timestamp'])
        self.figure = plt.Figure(figsize=(5,4), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.df.plot(ax=self.ax, kind='line', legend=False, marker='o', fontsize=10, color=style.COLOR2)
        self.ax.set_xlabel('Timestamp')
        self.ax.set_title(title)
        self.line = FigureCanvasTkAgg(self.figure, self)
        self.line.get_tk_widget().grid(column=0, row=0)
