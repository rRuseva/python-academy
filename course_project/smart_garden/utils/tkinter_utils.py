def get_center_window_left_top(parent, width, height):
    """Returns the left and top coordinates of a top level window to centered on the screen"""
    screen_width = parent.winfo_screenwidth()
    screen_height = parent.winfo_screenheight()
    left, top = 0,0
    if(width > screen_width//2):
        left  = 0
    else:
        left =(screen_width - width) // 2

    if(height > screen_height//2):
        top  = 0
    else:
        top =(screen_height - height) // 2
    # return ((screen_width - width) // 2, (screen_height - height) // 2)
    return(left, top)
