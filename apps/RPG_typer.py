import json
import os
import random
import time
import tkinter as tk
from tkinter import messagebox

from core.drag import make_draggable

SAVE_FILE = "rpg_typer_save.json"

WORDS_DB = [
    "python",
    "terminal",
    "coding",
    "keyboard",
    "algorithm",
    "variable",
    "function",
    "class",
    "monitor",
    "system",
    "linux",
    "interface",
    "gamification",
    "experience",
    "level",
    "stat",
    "windows",
    "sudo",
    "cd",
]


def rpg_typer(root):
    def load_data():
        default_data = {
            "level": 1,
            "xp": 0,
            "xp_to_next": 100,
            "gold": 0,
            "best_wpm": 0,
        }
        if os.path.exists(SAVE_FILE):
            try:
                with open(SAVE_FILE, "r") as f:
                    return json.load(f)
            except:
                return default_data
        return default_data

    def save_data():
        with open(SAVE_FILE, "w") as f:
            json.dump(state, f)

    state = load_data()
    session = {"target_text": "", "start_time": None}

    root_x = root.winfo_x() + (root.winfo_width() // 2) - 275
    root_y = root.winfo_y() + (root.winfo_height() // 2) - 225

    game_win = tk.Frame(
        root, bg="#1e1e1e", height=450, width=550, borderwidth=2, relief="ridge"
    )
    game_win.place(x=root_x, y=root_y)
    root.lift()
    make_draggable(game_win)

    title_bar = tk.Frame(game_win, bg="#333", height=25)
    title_bar.place(x=0, y=0, width=550, height=25)
    tk.Label(
        title_bar, text="RPG Typer + AutoSave", bg="#333", fg="white", font=("Arial", 9)
    ).pack(side="left", padx=5)

    tk.Button(
        title_bar, text="x", command=game_win.destroy, bg="#333", fg="red", bd=0
    ).pack(side="right", padx=5)

    stats_lbl = tk.Label(
        game_win, bg="#1e1e1e", fg="yellow", font=("Courier", 10), justify="left"
    )
    stats_lbl.place(x=25, y=35)

    text_display = tk.Text(
        game_win,
        font=("Courier", 14),
        bg="#2d2d2d",
        fg="white",
        wrap="word",
        state="disabled",
        bd=0,
        padx=10,
        pady=10,
    )
    text_display.place(x=25, y=80, width=500, height=120)
    text_display.tag_config("correct", foreground="#00FF00")
    text_display.tag_config("wrong", foreground="white", background="red")

    input_entry = tk.Entry(
        game_win, font=("Courier", 16), bg="black", fg="white", insertbackground="white"
    )
    input_entry.place(x=25, y=210, width=500, height=40)

    def update_ui():
        stats_lbl.config(
            text=f"LVL: {state['level']} | XP: {state['xp']}/{state['xp_to_next']} | GOLD: {state['gold']} | Best WPM: {state['best_wpm']:.1f}"
        )

    def generate_round():
        session["target_text"] = " ".join(random.choices(WORDS_DB, k=6))
        text_display.config(state="normal")
        text_display.delete("1.0", tk.END)
        text_display.insert("1.0", session["target_text"])
        text_display.config(state="disabled")
        input_entry.delete(0, tk.END)
        session["start_time"] = None
        input_entry.focus_set()

    def finish_round(typed):
        elapsed = time.time() - session["start_time"]
        wpm = (len(typed) / 5) / (elapsed / 60)

        xp_gain = int(wpm * 1.5)
        state["xp"] += xp_gain
        state["gold"] += xp_gain // 5
        if wpm > state["best_wpm"]:
            state["best_wpm"] = wpm

        leveled_up = False
        while state["xp"] >= state["xp_to_next"]:
            state["xp"] -= state["xp_to_next"]
            state["level"] += 1
            state["xp_to_next"] = int(state["xp_to_next"] * 1.3)
            leveled_up = True

        save_data()
        update_ui()

        msg = f"Koniec!\nWPM: {wpm:.1f}\nXP: +{xp_gain}"
        if leveled_up:
            msg += "\n\n!!! AWANS !!!"
        messagebox.showinfo("Wynik", msg, parent=game_win)
        generate_round()

    def check_input(event):
        if not session["target_text"]:
            return
        if not session["start_time"]:
            session["start_time"] = time.time()

        typed = input_entry.get()
        text_display.config(state="normal")
        text_display.tag_remove("correct", "1.0", tk.END)
        text_display.tag_remove("wrong", "1.0", tk.END)

        for i, char in enumerate(typed):
            if i < len(session["target_text"]):
                tag = "correct" if char == session["target_text"][i] else "wrong"
                text_display.tag_add(tag, f"1.{i}")
        text_display.config(state="disabled")

        if typed == session["target_text"]:
            finish_round(typed)

    input_entry.bind("<KeyRelease>", check_input)

    start_btn = tk.Button(
        game_win, text="START", command=generate_round, bg="#444", fg="white"
    )
    start_btn.place(x=225, y=280, width=100, height=40)

    update_ui()
