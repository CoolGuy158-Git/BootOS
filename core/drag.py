def make_draggable(widget, handle=None):
    if handle is None:
        handle = widget
    handle.bind("<Button-1>", lambda e: on_drag_start(e, widget))
    handle.bind("<B1-Motion>", lambda e: on_drag_motion(e, widget))

def on_drag_start(event, widget):
    widget._drag_start_x = event.x
    widget._drag_start_y = event.y
    widget.lift()

def on_drag_motion(event, widget):
    x = widget.winfo_x() - widget._drag_start_x + event.x
    y = widget.winfo_y() - widget._drag_start_y + event.y
    widget.place(x=x, y=y)


