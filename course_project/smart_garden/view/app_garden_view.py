# import os
from functools import partial
from tkinter import *
from tkinter import ttk, messagebox, font
# from tkinter.ttk import Notebook, Style
# from dao import garden_repo
# from model.garden import Garden
# from model.pot import Pot
import view.style_config as style
from view.app_pot_view import AppPotView

class AppGardenView(ttk.Frame):
    def __init__(self, root, application, name = "SmartGarden"):
        super().__init__(root, padding="5 10 5 10")
        self.application = application
        self.name = name
        # self.attributes('-alpha',0.5)
        self.grid(row=0, column=0, columnspan=8, sticky=(N, W, E, S) ) #columnspan=5,
        root.title(self.name)
        # add menu
        self.add_menu(root)

        ### Displey garden basic info
        self.garden = self.application.garden_repository.garden
        garden_name = StringVar()
        garden_name.set(f"{self.garden.name:<20.20}")
        self.label_garden_name = Label(self, textvariable=garden_name, font=(style.FONT_FAMILY, 18, 'bold'), fg=style.COLOR2, justify='left')
        self.label_garden_name.grid(columnspan=6, column=0, row=0)


        info = self.application.get_garden_info()
        garden_info_text = StringVar()
        garden_info_text.set(info[1])
        self.label_garden_info = Label(self, textvariable=garden_info_text, font=style.FONT, fg=style.FONT_FG,justify='left')
        self.label_garden_info.grid(columnspan=5, column=0, row=1)

        # garden actions
        # add pot button as new tab
        add_pot_str = StringVar()
        add_pot_btn = Button(self, textvariable=add_pot_str, command=application.add_new_pot, font=(style.FONT_FAMILY, 10), bg=style.COLOR2, fg="white", height=2, width=10)
        add_pot_str.set("Add pot")
        add_pot_btn.grid(column=5, row=1, columnspan=1, sticky=(N,E))
        self.update_idletasks()
        ### tab view for each pot
        self.pots_notebook = ttk.Notebook(self)
        self.pots_notebook.grid(columnspan=6, column=0, row=2)

        self.pots = self.garden.get_pots()

        ### create tabs
        tab_style = style.set_tab_style("tabs_style")

        tab_style.theme_use("tabs_style")
        tab_width = style.MAIN_WIDTH
        for i, pot in enumerate(self.pots):
            self.frame = Frame(self.pots_notebook, width=tab_width)
            self.frame.grid(column=0, row=2, columnspan=6)

            self.frame.grid_configure(padx=6,pady=6)
            tab_name = pot.name
            self.pot_view = AppPotView(self.frame, self.application, pot)
            self.pots_notebook.add(self.frame, text=tab_name)

        self.pots_notebook.grid_configure(padx=8, pady=8)

        # # add a vertical scrollbar
        # vsb = ttk.Scrollbar(root, orient="vertical", command=self.yview)
        # vsb.grid(row=0, column=6, sticky=(N, W, S), padx=0)
        # self.configure(yscrollcommand=vsb.set)


    def add_menu(self, root):
        """Constructs menu elements"""
        root.option_add('*tearOff', FALSE) # remove menu tear off ability
        self.menu_bar = Menu(root)
        root['menu'] = self.menu_bar

        # File menu
        # menu_file = Menu(self.menu_bar)
        # self.menu_bar.add_cascade(menu=menu_file, label="File", underline=0)
        # menu_file.add_command(label='New', command = self.newFile, underline=0, accelerator="Alt+N")
        # self.mainframe.bind("<Alt-N>", self.newFile)
        # menu_file.add_command(label="Open ...", command = self.openFile)
        # menu_file.add_command(label='Close', command = self.closeFile)
        # menu_file.entryconfigure('Close', state=DISABLED)

        # # Garden menu
        menu_garden = Menu(self.menu_bar)
        self.menu_bar.add_cascade(menu=menu_garden, label="Garden", underline=0)
        menu_garden.add_command(label='Add', command=self.on_new_garden, underline=0)
        menu_garden.add_command(label='Load', command=self.on_load_garden, underline=0)
        menu_garden.add_command(label='Reload', command=self.on_reload_garden, underline=0)
        menu_garden.add_command(label='Edit', command=self.on_edit_garden, underline=0)


    def on_new_garden(self):
        print("add garden")
        self.application.create_garden()

    def on_load_garden(self):
        self.application.load_garden()
        # messagebox.showinfo(title="File Open Dialog", message="Opening DB file ...")

    def on_reload_garden(self):
        self.application.reload_garden()

    def on_edit_garden(self):
        self.application.edit_garden()
        messagebox.showinfo(title="File Open Dialog", message="Opening DB file ...")

