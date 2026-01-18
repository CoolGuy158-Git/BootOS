import tkinter as tk


def paint(root):
    root_x = root.winfo_x() + (root.winfo_width() // 2) - 300
    root_y = root.winfo_y() + (root.winfo_height() // 2) - 300

    paintwindows = tk.Frame(
        root, bg="black", height=400, width=500, borderwidth=2, relief="ridge"
    )
    paintwindows.place(x=root_x, y=root_y)
    canvas = tk.Canvas(paintwindows, width=500, height=370, bg="white")
    canvas.place(x=0, y=30)

    colors = ["black", "red", "blue", "green", "white"]
    current_color_index = 0

    def paint1(event):
        x1, y1 = (event.x - 2), (event.y - 2)
        x2, y2 = (event.x + 2), (event.y + 2)
        canvas.create_oval(
            x1,
            y1,
            x2,
            y2,
            fill=colors[current_color_index],
            outline=colors[current_color_index],
        )

    canvas.bind("<B1-Motion>", paint1)

    def toggle_color():
        nonlocal current_color_index
        current_color_index = (current_color_index + 1) % len(colors)
        color_btn.config(text=colors[current_color_index])

    color_btn = tk.Button(
        paintwindows,
        width=5,
        text=colors[current_color_index],
        bg="tan",
        fg="black",
        activebackground="burlywood",
        activeforeground="white",
        command=toggle_color,
    )
    color_btn.place(x=55, y=0)

    def clear_canvas():
        canvas.delete("all")

    def fill():
        canvas.config(bg=colors[current_color_index])

    clear_btn = tk.Button(
        paintwindows,
        text="Clear",
        command=clear_canvas,
        bg="red",
        fg="black",
        activebackground="pink",
        activeforeground="white",
    )
    clear_btn.place(x=10, y=0)

    fill_btn = tk.Button(
        paintwindows,
        text="Fill",
        command=fill,
        bg="tan",
        fg="black",
        activebackground="burlywood",
        activeforeground="white",
    )
    fill_btn.place(x=105, y=0)

    cancel_btn = tk.Button(
        paintwindows,
        text="x",
        command=paintwindows.destroy,
        fg="red",
        height=1,
        font=("Arial", 10),
    )
    cancel_btn.place(relx=1, rely=0, anchor="ne")
