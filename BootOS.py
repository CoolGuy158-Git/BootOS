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

#apps

def Calculator():
    root_x = root.winfo_x() + (root.winfo_width() // 2) - 300
    root_y = root.winfo_y() + (root.winfo_height() // 2) - 300
    calc = tk.Frame(root, bg="grey", height=400, width=500, borderwidth=2, relief="ridge")
    calc.place(x=root_x, y=root_y)
    root.lift()
    make_draggable(calc)
    #Screen
    Screen = tk.Label(calc, width=15, height=1, text=" ", bg="#0000CC", bd=5, relief="ridge",
                      font=("Courier", 40, "bold"), fg="green")
    Screen.place(x=0, y=0, width=500, height=80)

    cancel1 = tk.Button(calc, text="x", command=calc.destroy, fg="red", height=1, font=("Arial", 10))
    cancel1.place(relx=1, rely=0, anchor="ne")
    cancel1.lift()

    # The Math
    # Show answer
    def show_input(value):
        current = Screen.cget("text")
        Screen.config(text=current + str(value))

    # Calculations
    def calculate():
        try:
            expression = Screen.cget("text")
            result = eval(expression)
            Screen.config(text=str(result))
        except (SyntaxError, ZeroDivisionError, TypeError, NameError):
            Screen.config(text="Error")
            Screen.after(1000, lambda: Screen.config(text=""))

    # for those who want press
    def keypress(event):
        key = event.char
        if key.isdigit() or key in "+-*/":
            show_input(key)
        elif key == "\r":
            calculate()
        elif key.lower() == "c":
            Screen.config(text="")

    calc.bind("<Key>", keypress)

    # numbers
    one = tk.Button(calc, width=10, height=2, text="1", bg="tan", activebackground="#a67c52", activeforeground="white",
                    command=lambda: show_input(1))
    one.place(x=34, y=110)
    two = tk.Button(calc, width=10, height=2, text="2", bg="tan", activebackground="#a67c52", activeforeground="white",
                    command=lambda: show_input("2"))
    two.place(x=34, y=160)
    three = tk.Button(calc, width=10, height=2, text="3", bg="tan", activebackground="#a67c52",
                      activeforeground="white", command=lambda: show_input("3"))
    three.place(x=34, y=210)
    four = tk.Button(calc, width=10, height=2, text="4", bg="tan", activebackground="#a67c52", activeforeground="white",
                     command=lambda: show_input("4"))
    four.place(x=34, y=260)
    five = tk.Button(calc, width=10, height=2, text="5", bg="tan", activebackground="#a67c52", activeforeground="white",
                     command=lambda: show_input("5"))
    five.place(x=34, y=310)
    six = tk.Button(calc, width=10, height=2, text="6", bg="tan", activebackground="#a67c52", activeforeground="white",
                    command=lambda: show_input("6"))
    six.place(x=134, y=110)
    seven = tk.Button(calc, width=10, height=2, text="7", bg="tan", activebackground="#a67c52",
                      activeforeground="white", command=lambda: show_input("7"))
    seven.place(x=134, y=160)
    eight = tk.Button(calc, width=10, height=2, text="8", bg="tan", activebackground="#a67c52",
                      activeforeground="white", command=lambda: show_input("8"))
    eight.place(x=134, y=210)
    nine = tk.Button(calc, width=10, height=2, text="9", bg="tan", activebackground="#a67c52", activeforeground="white",
                     command=lambda: show_input("9"))
    nine.place(x=134, y=260)
    zero = tk.Button(calc, width=10, height=2, text="0", bg="tan", activebackground="#a67c52", activeforeground="white",
                     command=lambda: show_input("0"))
    zero.place(x=134, y=310)
    # operation symbol
    addition = tk.Button(calc, width=15, height=2, text="+", bg="tan", activebackground="#a67c52",
                         activeforeground="white", command=lambda: show_input("+"))
    addition.place(x=234, y=110)
    subtraction = tk.Button(calc, width=15, height=2, text="-", bg="tan", activebackground="#a67c52",
                            activeforeground="white", command=lambda: show_input("-"))
    subtraction.place(x=234, y=160)
    division = tk.Button(calc, width=15, height=2, text="/", bg="tan", activebackground="#a67c52",
                         activeforeground="white", command=lambda: show_input("/"))
    division.place(x=234, y=210)
    multiplication = tk.Button(calc, width=15, height=2, text="*", bg="tan", activebackground="#a67c52",
                               activeforeground="white", command=lambda: show_input("*"))
    multiplication.place(x=234, y=260)
    equal = tk.Button(calc, width=15, height=10, text="=", bg="tan", activebackground="#a67c52",
                      activeforeground="white", command=calculate)
    equal.place(x=360, y=145)
    # The Extras
    Clear = tk.Button(calc, width=15, height=2, text="Clear", bg="tan", activebackground="#a67c52",
                      activeforeground="white", command=lambda: Screen.config(text=""))
    Clear.place(x=234, y=310)


def cookie():
    root_x = root.winfo_x() + (root.winfo_width() // 2) - 300
    root_y = root.winfo_y() + (root.winfo_height() // 2) - 300
    score = 0
    high_score_file = "high_score.txt"
    highscore = 0
    if os.path.exists(high_score_file):
        with open(high_score_file, "r") as f:
            highscore = int(f.read().strip())

    def score1():
        nonlocal score, highscore
        score += 1
        scoreshow.config(text=f"Score: {score}")
        if score > highscore:
            highscore = score
            highshow.config(text=f"High Score: {highscore}")
            with open(high_score_file, "w") as f:
                f.write(str(highscore))

    cookiewindow = tk.Frame(root, bg="white", height=600, width=600, borderwidth=2, relief="ridge")
    cookiewindow.place(x=root_x, y=root_y)
    root.lift()
    make_draggable(cookiewindow)

    scoreshow = tk.Label(cookiewindow, text=f"Score: {score}", bg="white", fg="black")
    scoreshow.place(x=300, y=50, anchor="center")

    highshow = tk.Label(cookiewindow, text=f"High Score: {highscore}", bg="white", fg="black")
    highshow.place(x=300, y=70, anchor="center")

    image = Image.open("cookie.png")
    photo = ImageTk.PhotoImage(image)
    cookiebutton = tk.Button(cookiewindow, image=photo, text="Cookie", command=score1)
    cookiebutton.place(x=300, y=310, anchor="center")
    cookiebutton.image = photo

    cancel = tk.Button(cookiewindow, text="x", command=cookiewindow.destroy, fg="red", height=1, font=("Arial", 10))
    cancel.place(relx=1, rely=0, anchor="ne")

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

    label4 = tk.Label(VerWindows, text="BootOS Ver 1.2", bg="white", fg="black", font=("Arial", 12, "bold"))
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

def notepad():
    root_x = root.winfo_x() + (root.winfo_width() // 2) - 300
    root_y = root.winfo_y() + (root.winfo_height() // 2) - 300
    notewindow = tk.Frame(root, bg="grey", height=400, width=500, borderwidth=2, relief="ridge")
    notewindow.place(x=root_x, y=root_y)
    make_draggable(notewindow)

    text_box = tk.Text(notewindow, bg="white", fg="black", font=("Courier", 12))
    text_box.place(x=10, y=10, width=480, height=380)

    cancel = tk.Button(notewindow, text="x", command=notewindow.destroy, fg="red", height=1, font=("Arial", 10))
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

    cookieclick = tk.Button(root, text="CookieClicker.exe", command=cookie,)
    cookieclick.place(x=28, y=56,)

    BootVer1 = tk.Button(root, text="BootVer", command=BootVer)
    BootVer1.place(x=28, y=106,)

    notepad1 = tk.Button(root, text="Notepad.exe", command=notepad,)
    notepad1.place(x=28, y=156,)

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