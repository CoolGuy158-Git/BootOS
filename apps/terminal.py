import platform
import tkinter as tk
from datetime import datetime

from core.drag import make_draggable


def terminal(root):
    root_x = root.winfo_x() + (root.winfo_width() // 2) - 300
    root_y = root.winfo_y() + (root.winfo_height() // 2) - 200

    term_win = tk.Frame(
        root, bg="#0c0c0c", height=400, width=600, borderwidth=2, relief="ridge"
    )
    term_win.place(x=root_x, y=root_y)
    root.lift()
    make_draggable(term_win)

    title_bar = tk.Frame(term_win, bg="#333", height=25)
    title_bar.place(x=0, y=0, width=600, height=25)
    tk.Label(
        title_bar, text="Terminal - bash", bg="#333", fg="white", font=("Consolas", 9)
    ).pack(side="left", padx=5)

    close_btn = tk.Button(
        title_bar, text="x", command=term_win.destroy, bg="#333", fg="red", bd=0, padx=5
    )
    close_btn.pack(side="right")

    output_text = tk.Text(
        term_win,
        bg="#0c0c0c",
        fg="#cccccc",
        font=("Consolas", 10),
        state="disabled",
        borderwidth=0,
        padx=10,
        pady=10,
    )
    output_text.place(x=0, y=25, width=600, height=340)

    prompt_label = tk.Label(
        term_win,
        text="user@bootos:~$",
        bg="#0c0c0c",
        fg="#00ff00",
        font=("Consolas", 10),
    )
    prompt_label.place(x=5, y=370)

    input_entry = tk.Entry(
        term_win,
        bg="#0c0c0c",
        fg="white",
        font=("Consolas", 10),
        borderwidth=0,
        insertbackground="white",
    )
    input_entry.place(x=120, y=370, width=470)
    input_entry.focus_set()

    def write_to_terminal(text, color="#cccccc"):
        output_text.config(state="normal")
        output_text.insert(tk.END, text + "\n", color)
        output_text.tag_config(color, foreground=color)
        output_text.see(tk.END)
        output_text.config(state="disabled")

    def execute_command(event):
        cmd = input_entry.get().strip().lower()
        write_to_terminal(f"user@bootos:~$ {cmd}", "#00ff00")
        input_entry.delete(0, tk.END)

        if cmd == "help":
            write_to_terminal("avalible commands:", "#00aaff")
            write_to_terminal(" help      - shows this list")
            write_to_terminal(" fastfetch - shows system information")
            write_to_terminal(" clear     - clears terminal")
            write_to_terminal(" date      - shows the date")
            write_to_terminal(" whoami    - shows who you are :)")
            write_to_terminal(" ls        - shows list of files in current directory")
            write_to_terminal(" exit      - it exits the terminal")

        elif cmd == "fastfetch":
            logo = [
                "  ▀███▀▀▀██▄        ▄▄█▀▀██▄  ▄█▀▀▀█▄█",
                "    ██    ██      ▄██▀    ▀██▄██    ▀█  ",
                "    ██    ██      ██▀      ▀█████▄      ",
                "    ██▀▀▀█▄▄ ████ ██        ██ ▀█████▄ ",
                "    ██    ▀█      ██▄      ▄██     ▀██   ",
                "    ██    ▄█      ▀██▄    ▄██▀█     ██   ",
                "  ▄████████         ▀▀████▀▀ █▀█████▀   ",
            ]
            for line in logo:
                write_to_terminal(line, "#00ff00")

            info = [
                f"OS: BootOS v1.0.2",
                f"Kernel: Python {platform.python_version()}",
                f"Uptime: Error!",
                f"Packages: Error!",
                f"Shell: bash-python",
                f"Resolution: {root.winfo_screenwidth()}x{root.winfo_screenheight()}",
                f"DE: BootOS-Desktop (Tkinter)",
                f"Memory: 124MB / 1024MB",
            ]
            for line in info:
                write_to_terminal(line, "#ffffff")

        elif cmd == "clear":
            output_text.config(state="normal")
            output_text.delete("1.0", tk.END)
            output_text.config(state="disabled")

        elif cmd == "date":
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            write_to_terminal(f"current time: {now}")

        elif cmd == "whoami":
            write_to_terminal("user (administrator)")

        elif cmd == "ls":
            write_to_terminal(
                "Calculator.exe  cookie.png  Notepad.exe  rpg_typer.exe  system32/",
                "#00aaff",
            )

        elif cmd == "exit":
            term_win.destroy()

        else:
            if cmd != "":
                write_to_terminal(f"bash: command not found: {cmd}", "#ff4444")

    input_entry.bind("<Return>", execute_command)

    write_to_terminal("BootOS Bash Shell v1.0.0", "#ffffff")
    write_to_terminal("type 'help', for commands list.", "#888888")
    write_to_terminal("-" * 40, "#444444")
