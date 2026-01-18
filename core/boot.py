import tkinter as tk

from apps.Calculator import Calculator
from apps.cookie import cookie
from apps.notepad import notepad
from apps.paint import paint
from apps.RPG_typer import rpg_typer
from apps.terminal import terminal
from core.clock_updater import update_clock
from core.drag import make_draggable
from core.start_menu import start_menu

root = tk.Tk()
bg_image = tk.PhotoImage(file="Windows xp start.png")


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


logs = [
    "Bootloader [OK]",
    "Kernel [OK]",
    "Command Line [OK]",
    "Drivers [OK]",
    "Packages [OK]",
    "GUI Booter [OK]",
    "Applications [OK]",
    "Calculator [OK]",
    "Booting in to BootOS",
]


def show_logs(index=0):
    if index < len(logs):
        current_text = label_log.cget("text")
        new_text = current_text + "\n" + logs[index] if current_text else logs[index]
        label_log.config(text=new_text)
        root.after(700, show_logs, index + 1)
    else:
        root.after(1000, blackout)


def blackout():
    cover = tk.Label(root, image=bg_image)
    cover.place(x=0, y=0, width=root.winfo_width(), height=root.winfo_height())


def BootVer():
    root_x = root.winfo_x() + (root.winfo_width() // 2) - 300
    root_y = root.winfo_y() + (root.winfo_height() // 2) - 300
    VerWindows = tk.Frame(
        root, bg="white", width=600, height=400, borderwidth=2, relief="ridge"
    )
    VerWindows.place(x=root_x, y=root_y)
    VerWindows.lift()
    logolabel = tk.Label(
        VerWindows,
        text=logo2(),
        bg="white",
        fg="black",
        justify="left",
        font=("Courier", 10),
    )
    logolabel.place(x=300, y=90, anchor="center")

    make_draggable(VerWindows)

    label4 = tk.Label(
        VerWindows,
        text="BootOS Ver 1.3",
        bg="white",
        fg="black",
        font=("Arial", 12, "bold"),
    )
    label4.place(relx=0.5, y=250, anchor="center")

    label5 = tk.Label(
        VerWindows,
        text=(
            "License: This project is provided for educational and personal use. "
            "It is released under a permissive license feel free to modify, extend, or distribute the code. "
            "Attribution is appreciated but not required. For commercial use, review the code for any third-party dependencies."
        ),
        bg="white",
        fg="black",
        justify="center",
        wraplength=500,
    )
    label5.place(relx=0.5, y=320, anchor="center")

    cancel = tk.Button(
        VerWindows,
        text="x",
        command=VerWindows.destroy,
        fg="red",
        height=1,
        font=("Arial", 10),
    )
    cancel.place(relx=1, rely=0, anchor="ne")


def show_os():
    global clock_label
    taskbar_height = 40
    taskbar = tk.Frame(root, bg="#C0C0C0", height=taskbar_height)
    taskbar.pack(side="bottom", fill="x")
    calculator = tk.Button(
        root, text="Calculator.exe", command=lambda: Calculator(root)
    )
    calculator.place(
        x=28,
        y=6,
    )

    clock_label = tk.Label(
        taskbar, text="", bg="#C0C0C0", fg="black", font=("Courier New", 14)
    )
    clock_label.pack(side="right", padx=5, pady=5)

    update_clock(label, root)

    startbutton = tk.Button(
        taskbar,
        text="Start Menu",
        bg="#C0C0C0",
        fg="black",
        command=lambda: start_menu(root),
        font=("Courier New", 12),
    )
    startbutton.pack(side="left", padx=5, pady=5)

    cookieclick = tk.Button(
        root,
        text="CookieClicker.exe",
        command=lambda: cookie(root),
    )
    cookieclick.place(
        x=28,
        y=56,
    )

    BootVer1 = tk.Button(root, text="BootVer", command=BootVer)
    BootVer1.place(
        x=28,
        y=106,
    )

    notepad1 = tk.Button(
        root,
        text="Notepad.exe",
        command=lambda: notepad(root),
    )
    notepad1.place(
        x=28,
        y=156,
    )

    paintapp = tk.Button(root, text="Paint.exe", command=lambda: paint(root))
    paintapp.place(
        x=28,
        y=206,
    )

    rpg_app = tk.Button(root, text="RPG_Typer.exe", command=lambda: rpg_typer(root))
    rpg_app.place(x=28, y=256)

    term_btn = tk.Button(root, text="Terminal.exe", command=lambda: terminal(root))
    term_btn.place(x=28, y=306)


# boot Screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
root.configure(bg="black")
# Boot Screen
label = tk.Label(
    root,
    text=logo(),
    bg="black",
    fg="white",
    font=(
        "Courier New",
        10,
    ),
)
label.place(
    x=28,
    y=6,
)
label_log = tk.Label(
    root, text="", bg="black", fg="white", font=("Courier New", 12), justify="left"
)
label_log.place(x=28, y=220)
root.after(1500, show_logs)
# the actual Os
root.after(9500, show_os)
root.mainloop()
