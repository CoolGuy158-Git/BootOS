import tkinter as tk

from core.drag import make_draggable


def notepad(root):
    root_x = root.winfo_x() + (root.winfo_width() // 2) - 300
    root_y = root.winfo_y() + (root.winfo_height() // 2) - 300
    notewindow = tk.Frame(
        root, bg="grey", height=400, width=500, borderwidth=2, relief="ridge"
    )
    notewindow.place(x=root_x, y=root_y)
    make_draggable(notewindow)

    text_box = tk.Text(notewindow, bg="white", fg="black", font=("Courier", 12))
    text_box.place(x=10, y=10, width=480, height=380)

    cancel = tk.Button(
        notewindow,
        text="x",
        command=notewindow.destroy,
        fg="red",
        height=1,
        font=("Arial", 10),
    )
    cancel.place(relx=1, rely=0, anchor="ne")
