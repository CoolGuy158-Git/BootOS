import os
import tkinter as tk

from PIL import Image, ImageTk

from core.drag import make_draggable


def cookie(root):
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

    cookiewindow = tk.Frame(
        root, bg="white", height=600, width=600, borderwidth=2, relief="ridge"
    )
    cookiewindow.place(x=root_x, y=root_y)
    root.lift()
    make_draggable(cookiewindow)

    scoreshow = tk.Label(cookiewindow, text=f"Score: {score}", bg="white", fg="black")
    scoreshow.place(x=300, y=50, anchor="center")

    highshow = tk.Label(
        cookiewindow, text=f"High Score: {highscore}", bg="white", fg="black"
    )
    highshow.place(x=300, y=70, anchor="center")

    image = Image.open("cookie.png")
    photo = ImageTk.PhotoImage(image)
    cookiebutton = tk.Button(cookiewindow, image=photo, text="Cookie", command=score1)
    cookiebutton.place(x=300, y=310, anchor="center")
    cookiebutton.image = photo

    cancel = tk.Button(
        cookiewindow,
        text="x",
        command=cookiewindow.destroy,
        fg="red",
        height=1,
        font=("Arial", 10),
    )
    cancel.place(relx=1, rely=0, anchor="ne")
