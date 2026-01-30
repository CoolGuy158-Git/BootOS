from time import strftime
import tkinter as tk
from PIL import Image, ImageTk
import os

root = tk.Tk()
def make_draggable(widget):
        widget.bind("<Button-1>", on_drag_start)
        widget.bind("<B1-Motion>", on_drag_motion)
def on_drag_start(event):
        widget = event.widget
        widget._drag_start_x = event.x
        widget._drag_start_y = event.y
def on_drag_motion(event):
        widget = event.widget
        x = widget.winfo_x() - widget._drag_start_x + event.x
        y = widget.winfo_y() - widget._drag_start_y + event.y
        widget.place(x=x, y=y)



def logo():
    ascii_logo = r"""                                                         
▀███▀▀▀██▄                   ██        ▄▄█▀▀██▄  ▄█▀▀▀█▄█
  ██    ██                   ██      ▄██▀    ▀██▄██    ▀█
  ██    ██ ▄██▀██▄  ▄██▀██▄██████    ██▀      ▀█████▄    
  ██▀▀▀█▄▄██▀   ▀████▀   ▀██ ██      ██        ██ ▀█████▄
  ██    ▀███     ████     ██ ██      ██▄      ▄██     ▀██
  ██    ▄███▄   ▄████▄   ▄██ ██      ▀██▄    ▄██▀█     ██
▄████████  ▀█████▀  ▀█████▀  ▀████     ▀▀████▀▀ █▀█████▀ 


"""
    return ascii_logo
def logo2():
    ascii_logo2 = r"""     
▀███▀▀▀██▄        ▄▄█▀▀██▄  ▄█▀▀▀█▄█
  ██    ██      ▄██▀    ▀██▄██    ▀█
  ██    ██      ██▀      ▀█████▄  
  ██▀▀▀█▄▄ ████ ██        ██ ▀█████▄
  ██    ▀█      ██▄      ▄██     ▀██
  ██    ▄█      ▀██▄    ▄██▀█     ██
▄████████         ▀▀████▀▀ █▀█████▀ 
"""
    return ascii_logo2

def BootVer():
    root_x = root.winfo_x() + (root.winfo_width() // 2) - 300
    root_y = root.winfo_y() + (root.winfo_height() // 2) - 300
    VerWindows = tk.Frame(root, bg="white", width=600, height=400, borderwidth=2, relief="ridge")
    VerWindows.place(x=root_x, y=root_y)
    VerWindows.lift()
    logolabel = tk.Label(VerWindows, text=logo2(), bg="white", fg="black", justify="left", font=("Courier", 10),)
    logolabel.place(x=300, y=90, anchor="center")

    make_draggable(VerWindows)

    label4 = tk.Label(VerWindows, text="BootOS Ver 1.3", bg="white", fg="black", font=("Arial", 12, "bold"))
    label4.place(relx=0.5, y=250, anchor="center")

    label5 = tk.Label(
        VerWindows,
        text=("License: This project is provided for educational and personal use. "
              "It is released under a permissive license—feel free to modify, extend, or distribute the code. "
              "Attribution is appreciated but not required. For commercial use, review the code for any third-party dependencies."),
        bg="white",
        fg="black",
        justify="center",
        wraplength=500
    )
    label5.place(relx=0.5, y=320, anchor="center")

    cancel = tk.Button(VerWindows, text="x", command=VerWindows.destroy, fg="red", height=1, font=("Arial", 10))
    cancel.place(relx=1, rely=0, anchor="ne")



logs = [
    "Bootloader [OK]",
    "Kernel [OK]",
    "Command Line [OK]",
    "Drivers [OK]",
    "Packages [OK]",
    "GUI Booter [OK]",
    "Applications [OK]",
    "Calculator [OK]",
    "Booting in to BootOS"
]


bg_image = tk.PhotoImage(file="Windows xp start.png")
def start_menu():
    global start
    start = tk.Frame(root, bg="white", height=100, width=100, borderwidth=2, relief="ridge")
    start.place(relx=0.5, rely=0.5, anchor="center")
    shut_down = tk.Button(start, text="Shutdown", command=root.destroy)
    shut_down.place(relx=0.5, rely=0.5, anchor="center")
    cancel = tk.Button(start, text="x", command=start.destroy, fg="red", height=1, font=("Arial", 10))
    cancel.place(relx=1, rely=0, anchor="ne")
def update_clock():
    current_time = strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    root.after(1000, update_clock)
def blackout():
    cover = tk.Label(root,image=bg_image )
    cover.place(x=0, y=0, width=root.winfo_width(), height=root.winfo_height())

def show_logs(index=0):
    if index < len(logs):
        current_text = label_log.cget("text")
        new_text = current_text + "\n" + logs[index] if current_text else logs[index]
        label_log.config(text=new_text)
        root.after(700, show_logs, index + 1)
    else:
        root.after(1000, blackout)

def show_os():
    global clock_label
    taskbar_height = 40
    taskbar = tk.Frame(root, bg="#C0C0C0", height=taskbar_height)
    taskbar.pack(side="bottom", fill="x")
    calculator = tk.Button(root, text="Calculator.exe", command=Calculator)
    calculator.place(x=28, y=6,)

    clock_label = tk.Label(taskbar, text="", bg="#C0C0C0", fg="black", font=("Courier New", 14))
    clock_label.pack(side="right", padx=5, pady=5)

    update_clock()

    startbutton = tk.Button(taskbar, text="Start Menu", bg="#C0C0C0", fg="black", command=start_menu, font=("Courier New", 12))
    startbutton.pack(side="left", padx=5, pady=5)

#boot Screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
root.configure(bg="black")
#Boot Screen
label = tk.Label(root, text=logo(), bg="black", fg="white", font=("Courier New", 10,))
label.place(x=28, y=6,)
label_log = tk.Label(root, text="", bg="black", fg="white", font=("Courier New", 12), justify="left")
label_log.place(x=28, y=220)
root.after(1500, show_logs)
# the actual Os
root.after(9500, show_os)
root.mainloop()