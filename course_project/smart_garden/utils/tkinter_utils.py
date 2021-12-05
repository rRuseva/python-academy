def get_ceter_window_left_top(parent, width, height):
    """Returns the left and top coordinates of a top level window to centwred on the screen"""
    screen_width = parent.winfo_screenwidth()
    screen_height = parent.winfo_screenheight()
    return ((screen_width - width) // 2, (screen_height - height) // 2)
