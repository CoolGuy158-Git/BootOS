import tkinter as tk
from time import strftime


def update_clock(label, root):
    current_time = strftime("%H:%M:%S")
    label.config(text=current_time)
    root.after(1000, lambda: update_clock(label, root))
