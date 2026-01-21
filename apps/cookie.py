import json
import os
import tkinter as tk

from PIL import Image, ImageTk

from core.drag import make_draggable


def cookie(root):
    width, height = 900, 900
    root_x = root.winfo_x() + (root.winfo_width() // 2) - (width // 2)
    root_y = root.winfo_y() + (root.winfo_height() // 2) - (height // 2)

    save_file = "cookie_save.json"

    state = {
        "score": 0.0,
        "highscore": 0,
        "click_value": 1,
        "auto_cps": 0.0,
        "upgrades": {
            "cursor": {"level": 0, "base_cost": 15, "power": 0.5, "name": "cursor"},
            "grandma": {"level": 0, "base_cost": 100, "power": 1.0, "name": "grandma"},
            "farm": {"level": 0, "base_cost": 500, "power": 5.0, "name": "farm"},
            "bakery": {"level": 0, "base_cost": 1000, "power": 10, "name": "bakery"},
            "factory": {
                "level": 0,
                "base_cost": 2000,
                "power": 21.5,
                "name": "Factory",
            },
        },
    }

    if os.path.exists(save_file):
        try:
            with open(save_file, "r") as f:
                saved_data = json.load(f)
                state.update(saved_data)
        except:
            pass

    def save_game():
        with open(save_file, "w") as f:
            json.dump(state, f)

    def get_cost(upgrade_key):
        upg = state["upgrades"][upgrade_key]
        return int(upg["base_cost"] * (1.15 ** upg["level"]))

    def update_display():
        score_label.config(text=f"Ciastka: {int(state['score'])}")
        cps_label.config(
            text=f"Na sekundę: {round(state['auto_cps'], 1)} | Klik: {state['click_value']}"
        )
        high_label.config(text=f"Rekord: {int(state['highscore'])}")

        for key, btn in upgrade_buttons.items():
            cost = get_cost(key)
            lvl = state["upgrades"][key]["level"]
            btn.config(
                text=f"{state['upgrades'][key]['name']}\nKoszt: {cost} | Poz: {lvl}"
            )

    def score1():
        state["score"] += state["click_value"]
        if state["score"] > state["highscore"]:
            state["highscore"] = state["score"]
        update_display()
        save_game()

    def buy_upgrade(key):
        cost = get_cost(key)
        if state["score"] >= cost:
            state["score"] -= cost
            state["upgrades"][key]["level"] += 1

            if key == "grandma":
                state["click_value"] += 1
            else:
                state["auto_cps"] += state["upgrades"][key]["power"]

            update_display()
            save_game()

    def auto_clicker():
        if state["auto_cps"] > 0:
            state["score"] += state["auto_cps"] / 10
            if state["score"] > state["highscore"]:
                state["highscore"] = state["score"]
            update_display()
        cookiewindow.after(100, auto_clicker)

    cookiewindow = tk.Frame(
        root, bg="#fcfcfc", height=height, width=width, borderwidth=2, relief="ridge"
    )
    cookiewindow.place(x=root_x, y=root_y)
    make_draggable(cookiewindow)

    side_panel = tk.Frame(cookiewindow, bg="#f0f0f0", width=500, height=height)
    side_panel.pack(side="right", fill="y")
    side_panel.pack_propagate(False)

    tk.Label(side_panel, text="SKLEP", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(
        pady=20
    )

    upgrade_buttons = {}
    for key in state["upgrades"]:
        btn = tk.Button(
            side_panel,
            text="",
            font=("Arial", 10),
            command=lambda k=key: buy_upgrade(k),
            bg="#ffffff",
            activebackground="#e0e0e0",
            pady=10,
        )
        btn.pack(fill="x", padx=10, pady=5)
        upgrade_buttons[key] = btn

    main_area = tk.Frame(cookiewindow, bg="white")
    main_area.pack(side="left", expand=True, fill="both")

    score_label = tk.Label(main_area, text="", font=("Arial", 30, "bold"), bg="white")
    score_label.pack(pady=(50, 0))

    cps_label = tk.Label(main_area, text="", font=("Arial", 12), bg="white", fg="#555")
    cps_label.pack()

    high_label = tk.Label(main_area, text="", font=("Arial", 10), bg="white", fg="gray")
    high_label.pack(pady=5)

    try:
        img = Image.open("cookie.png").resize((300, 300), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        cookie_btn = tk.Button(
            main_area,
            image=photo,
            command=score1,
            bd=0,
            bg="white",
            activebackground="white",
        )
        cookie_btn.image = photo
    except:
        cookie_btn = tk.Button(
            main_area, text="Ciasteczko", command=score1, width=20, height=10
        )

    cookie_btn.pack(expand=True)

    tk.Button(
        cookiewindow,
        text="✕",
        command=cookiewindow.destroy,
        bg="#ff4d4d",
        fg="white",
        bd=0,
    ).place(relx=1, rely=0, anchor="ne")

    update_display()
    auto_clicker()
