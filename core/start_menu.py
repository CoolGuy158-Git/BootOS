import tkinter as tk


def start_menu(root):
    global start
    start = tk.Frame(
        root, bg="white", height=100, width=100, borderwidth=2, relief="ridge"
    )
    start.place(relx=0.5, rely=0.5, anchor="center")
    shut_down = tk.Button(start, text="Shutdown", command=root.destroy)
    shut_down.place(relx=0.5, rely=0.5, anchor="center")
    cancel = tk.Button(
        start, text="x", command=start.destroy, fg="red", height=1, font=("Arial", 10)
    )
    cancel.place(relx=1, rely=0, anchor="ne")
