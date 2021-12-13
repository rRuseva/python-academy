from tkinter import ttk, font

MAIN_WIDTH = 900
MAIN_HEIGHT = 700
MAX_WIDTH = 1920
MAX_HEIGHT = 1080
# LOGO_SIZE = (MAIN_WIDTH, MAIN_HEIGHT)
LOGO_SIZE = (MAIN_WIDTH*3//4, MAIN_HEIGHT*3//4)
FONT_FAMILY = "Comic Sans MS"
FONT_SIZE = 12
FONT = ("Comic Sans MS", 12, 'italic')
FONT_FG = "#3f3f3f"
COLOR1 = "#c6e5c8"
COLOR2 = "#20bebe"
COLOR3 = "#f1bb41"
COLOR4 = "#fac490"

def set_tab_style(style_name):
    TAB_STYLE = ttk.Style()
    try:
        TAB_STYLE.theme_create( style_name, parent="alt", settings={
            "TNotebook": {"configure": {"tabmargins": [0, 6, 0, 0] } },
            "TNotebook.Tab": {
                "configure": {"padding": [10, 5] },
                "map":       {"background": [("selected", COLOR3)],
                              "expand": [("selected", [1, 1, 1, 0])] } } } )
    except:
        print("theme already created")
    return TAB_STYLE
