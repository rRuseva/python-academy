from tkinter import *
from tkinter import ttk
from turtle import width, window_height

if __name__ == '__main__':
    root = Tk()
    root.title("")
    mainframe = ttk.Frame(root, padding="50 30 50 30")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    l = ttk.Label(mainframe, text="Starting ...", width=130)
    l.grid()


    root.bind('<Enter>', lambda e:l.configure(text="Moved mouse inside."))
    root.bind('<Leave>', lambda e:l.configure(text="Moved mouse outside."))
    root.bind('<3>', lambda e:l.configure(text="Clicked right mouse button."))
    root.bind('<Double-1>', lambda e:l.configure(text="Double clicked left mouse button."))
    root.bind('<ButtonPress-1>', lambda e:l.configure(text="Clicked left mouse button."))
    l.bind('<B3-Motion>', lambda e:l.configure(text=f"Dragged with right button to {e.x}x{e.y}."))

    root.mainloop()
