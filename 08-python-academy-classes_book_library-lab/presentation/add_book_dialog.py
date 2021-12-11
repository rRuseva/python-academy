from tkinter import *
from tkinter import ttk, messagebox

import tk

from utils.tkinter_utils import get_ceter_window_left_top

DIALOG_WIDTH = 600
DIALOG_HEIGHT = 500


class AddBookDialog:
    def __init__(self, parent, width=DIALOG_WIDTH, height=DIALOG_HEIGHT, *args):
        self.parent = parent
        self.book_dlg = Toplevel(self.parent, *args)
        self.book_dlg.title("Add Book")
        left, top = get_ceter_window_left_top(parent, width, height)
        self.book_dlg.geometry(f"{DIALOG_WIDTH}x{DIALOG_HEIGHT}+{left}+{top}")

        self.mainframe = ttk.Frame(self.book_dlg, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S) )

        # from Model fields
        self.id = StringVar()
        self.title = StringVar()
        self.subtitle = StringVar()
        self.authors = StringVar()

        #form labels
        ttk.Label(self.mainframe, text="ID", justify=CENTER, width=7).grid(column=0,row=0, sticky=(E,W))
        ttk.Label(self.mainframe, text="Title", justify=CENTER, width=7).grid(column=0,row=1, sticky=(E,W))
        ttk.Label(self.mainframe, text="Subtitle", justify=CENTER, width=7).grid(column=0,row=2, sticky=(E,W))
        ttk.Label(self.mainframe, text="Authors", justify=CENTER, width=7).grid(column=0,row=3, sticky=(E,W))

        # from entries
        self.id_entry = ttk.Entry(self.mainframe, textvariable=self.id, width=37).grid(column=1,row=0, sticky=(E,W))
        self.title_entry = ttk.Entry(self.mainframe, textvariable=self.title, width=37).grid(column=1,row=1, sticky=(E,W))
        self.subtitle_entry = ttk.Entry(self.mainframe, textvariable=self.subtitle, width=37).grid(column=1,row=2, sticky=(E,W))
        self.authors_entry = ttk.Entry(self.mainframe, textvariable=self.authors, width=37).grid(column=1,row=3, sticky=(E,W))


        # error labels
        self.id_errors = Label(self.mainframe, text="", justify=LEFT,fg='red')
        self.id_errors.grid(column=2,row=0,sticky=(E,W))
        self.title_errors = Label(self.mainframe, text="", justify=LEFT,fg='red')
        self.title_errors.grid(column=2,row=0,sticky=(E,W))
        self.subtitle_errors = Label(self.mainframe, text="", justify=LEFT,fg='red')
        self.subtitle_errors.grid(column=2,row=0,sticky=(E,W))
        self.authors_errors = Label(self.mainframe, text="", justify=LEFT,fg='red')
        self.authors_errors.grid(column=2,row=0,sticky=(E,W))

        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=15,pady=15)
        self.book_dlg.wait_window()

