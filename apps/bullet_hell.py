import json
import math
import os
import random
import time
import tkinter as tk
from tkinter import messagebox

from core.drag import make_draggable

SAVE_FILE = "bullet_hell_save.json"


class BulletHellGame:
    def __init__(self, master, game_win):
        self.master = master
        self.game_win = game_win
        self.width = 800
        self.height = 600

        self.pattern_colors = {
            "straight": "#ffffff",
            "circle": "#00ffff",
            "wave": "#ffff00",
            "spiral": "#ff00ff",
            "cross": "#ff8800",
            "rain": "#00ff88",
            "burst": "#ff0088",
        }

        self.levels = [
            {
                "duration": 10,
                "bullet_speed": 2,
                "spawn_rate": 30,
                "patterns": ["straight"],
            },
            {
                "duration": 15,
                "bullet_speed": 2.5,
                "spawn_rate": 25,
                "patterns": ["straight", "circle"],
            },
            {
                "duration": 20,
                "bullet_speed": 3,
                "spawn_rate": 20,
                "patterns": ["straight", "circle", "wave"],
            },
            {
                "duration": 20,
                "bullet_speed": 3.5,
                "spawn_rate": 18,
                "patterns": ["straight", "circle", "wave", "spiral"],
            },
            {
                "duration": 25,
                "bullet_speed": 4,
                "spawn_rate": 15,
                "patterns": ["straight", "circle", "wave", "spiral"],
            },
            {
                "duration": 25,
                "bullet_speed": 4.5,
                "spawn_rate": 13,
                "patterns": ["straight", "circle", "wave", "spiral", "cross"],
            },
            {
                "duration": 30,
                "bullet_speed": 5,
                "spawn_rate": 12,
                "patterns": ["straight", "circle", "wave", "spiral", "cross"],
            },
            {
                "duration": 30,
                "bullet_speed": 5.5,
                "spawn_rate": 10,
                "patterns": ["straight", "circle", "wave", "spiral", "cross", "rain"],
            },
            {
                "duration": 35,
                "bullet_speed": 6,
                "spawn_rate": 9,
                "patterns": ["straight", "circle", "wave", "spiral", "cross", "rain"],
            },
            {
                "duration": 40,
                "bullet_speed": 6.5,
                "spawn_rate": 8,
                "patterns": [
                    "straight",
                    "circle",
                    "wave",
                    "spiral",
                    "cross",
                    "rain",
                    "burst",
                ],
            },
        ]

        self.load_progress()
        self.create_menu()

    def load_progress(self):
        if os.path.exists(SAVE_FILE):
            try:
                with open(SAVE_FILE, "r") as f:
                    data = json.load(f)
                    self.max_level = data.get("max_level", 0)
                    self.completed_levels = data.get("completed_levels", [])
            except:
                self.max_level = 0
                self.completed_levels = []
        else:
            self.max_level = 0
            self.completed_levels = []

    def save_progress(self):
        data = {"max_level": self.max_level, "completed_levels": self.completed_levels}
        with open(SAVE_FILE, "w") as f:
            json.dump(data, f)

    def create_menu(self):
        self.menu_frame = tk.Frame(self.game_win, bg="#1a1a2e")
        self.menu_frame.place(x=0, y=0, width=self.width, height=self.height)

        title = tk.Label(
            self.menu_frame,
            text="BULLET HELL",
            font=("Arial", 48, "bold"),
            bg="#1a1a2e",
            fg="#ff00ff",
        )
        title.pack(pady=40)

        levels_frame = tk.Frame(self.menu_frame, bg="#1a1a2e")
        levels_frame.pack(pady=20)

        for i in range(10):
            row = i // 5
            col = i % 5

            btn_text = str(i + 1)
            if i in self.completed_levels:
                btn_text += " ✓"

            btn = tk.Button(
                levels_frame,
                text=btn_text,
                font=("Arial", 20, "bold"),
                width=4,
                height=2,
                bg="#00ffff" if i <= self.max_level else "#333333",
                fg="white" if i <= self.max_level else "#666666",
                state="normal" if i <= self.max_level else "disabled",
                command=lambda lvl=i: self.start_level(lvl),
            )
            btn.grid(row=row, column=col, padx=10, pady=10)

        endless_btn = tk.Button(
            self.menu_frame,
            text="ENDLESS MODE",
            font=("Arial", 16, "bold"),
            bg="#ff00ff" if self.max_level >= 4 else "#333333",
            fg="white" if self.max_level >= 4 else "#666666",
            state="normal" if self.max_level >= 4 else "disabled",
            width=20,
            height=2,
            command=self.start_endless,
        )
        endless_btn.pack(pady=20)

    def start_level(self, level_index):
        self.current_level = level_index
        self.is_endless = False
        self.is_playing = True
        self.start_time = time.time()
        self.frame_count = 0

        self.menu_frame.destroy()
        self.create_game()

    def start_endless(self):
        self.is_endless = True
        self.is_playing = True
        self.start_time = time.time()
        self.endless_score = 0
        self.frame_count = 0

        self.menu_frame.destroy()
        self.create_game()

    def create_game(self):
        self.canvas = tk.Canvas(
            self.game_win,
            width=self.width,
            height=self.height,
            bg="black",
            highlightthickness=0,
        )
        self.canvas.place(x=0, y=0)

        self.ui_label = tk.Label(
            self.game_win, text="", font=("Arial", 14, "bold"), bg="black", fg="white"
        )
        self.ui_label.place(x=10, y=10)

        back_btn = tk.Button(
            self.game_win,
            text="MENU",
            font=("Arial", 12),
            bg="#333333",
            fg="white",
            command=self.return_to_menu,
        )
        back_btn.place(x=self.width - 80, y=10)

        self.player = {
            "x": self.width / 2,
            "y": self.height / 2,
            "size": 15,
            "speed": 5,
        }

        self.bullets = []
        self.warnings = []
        self.keys = set()

        self.game_win.bind("<KeyPress>", self.key_press)
        self.game_win.bind("<KeyRelease>", self.key_release)
        self.game_win.focus_set()

        self.game_loop()

    def key_press(self, event):
        self.keys.add(event.keysym.lower())

    def key_release(self, event):
        self.keys.discard(event.keysym.lower())

    def spawn_bullets(self):
        if self.is_endless:
            level = {
                "bullet_speed": 3 + (self.endless_score // 10) * 0.5,
                "patterns": [
                    "straight",
                    "circle",
                    "wave",
                    "spiral",
                    "cross",
                    "rain",
                    "burst",
                ],
            }
        else:
            level = self.levels[self.current_level]

        pattern = random.choice(level["patterns"])
        self.create_warning(pattern, level["bullet_speed"])

    def create_warning(self, pattern, speed):
        warning = {
            "pattern": pattern,
            "speed": speed,
            "created_at": time.time(),
            "duration": 0.5,
            "data": {},
        }

        if pattern == "straight":
            side = random.randint(0, 3)
            if side == 0:
                x = random.randint(0, self.width)
                warning["data"] = {"side": 0, "x": x, "y": 0}
            elif side == 1:
                y = random.randint(0, self.height)
                warning["data"] = {"side": 1, "x": self.width, "y": y}
            elif side == 2:
                x = random.randint(0, self.width)
                warning["data"] = {"side": 2, "x": x, "y": self.height}
            else:
                y = random.randint(0, self.height)
                warning["data"] = {"side": 3, "x": 0, "y": y}

        elif pattern in ["circle", "spiral", "burst"]:
            if pattern == "burst":
                x = self.player["x"] + random.randint(-100, 100)
                y = self.player["y"] + random.randint(-100, 100)
            else:
                x = random.randint(50, self.width - 50)
                y = random.randint(50, self.height - 50)
            warning["data"] = {"x": x, "y": y}

        elif pattern == "wave":
            y = 0 if random.random() < 0.5 else self.height
            warning["data"] = {"y": y}

        elif pattern == "cross":
            x = random.randint(100, self.width - 100)
            y = random.randint(100, self.height - 100)
            warning["data"] = {"x": x, "y": y}

        elif pattern == "rain":
            warning["data"] = {}

        self.warnings.append(warning)

    def spawn_bullets_from_warning(self, warning):
        pattern = warning["pattern"]
        speed = warning["speed"]
        data = warning["data"]
        color = self.pattern_colors[pattern]

        if pattern == "straight":
            side = data["side"]
            if side == 0:
                self.bullets.append(
                    {
                        "x": data["x"],
                        "y": -10,
                        "vx": 0,
                        "vy": speed,
                        "size": 8,
                        "color": color,
                    }
                )
            elif side == 1:
                self.bullets.append(
                    {
                        "x": self.width + 10,
                        "y": data["y"],
                        "vx": -speed,
                        "vy": 0,
                        "size": 8,
                        "color": color,
                    }
                )
            elif side == 2:
                self.bullets.append(
                    {
                        "x": data["x"],
                        "y": self.height + 10,
                        "vx": 0,
                        "vy": -speed,
                        "size": 8,
                        "color": color,
                    }
                )
            else:
                self.bullets.append(
                    {
                        "x": -10,
                        "y": data["y"],
                        "vx": speed,
                        "vy": 0,
                        "size": 8,
                        "color": color,
                    }
                )

        elif pattern == "circle":
            for i in range(12):
                angle = (math.pi * 2 * i) / 12
                self.bullets.append(
                    {
                        "x": data["x"],
                        "y": data["y"],
                        "vx": math.cos(angle) * speed,
                        "vy": math.sin(angle) * speed,
                        "size": 7,
                        "color": color,
                    }
                )

        elif pattern == "wave":
            for i in range(8):
                self.bullets.append(
                    {
                        "x": (self.width / 8) * i,
                        "y": -10 if data["y"] < self.height / 2 else self.height + 10,
                        "vx": math.sin(i) * speed * 0.5,
                        "vy": speed if data["y"] < self.height / 2 else -speed,
                        "size": 6,
                        "color": color,
                    }
                )

        elif pattern == "spiral":
            rotation = time.time()
            for i in range(6):
                angle = (math.pi * 2 * i) / 6 + rotation
                self.bullets.append(
                    {
                        "x": data["x"],
                        "y": data["y"],
                        "vx": math.cos(angle) * speed,
                        "vy": math.sin(angle) * speed,
                        "size": 8,
                        "color": color,
                    }
                )

        elif pattern == "cross":
            for dx, dy in [(speed, 0), (-speed, 0), (0, speed), (0, -speed)]:
                self.bullets.append(
                    {
                        "x": data["x"],
                        "y": data["y"],
                        "vx": dx,
                        "vy": dy,
                        "size": 7,
                        "color": color,
                    }
                )

        elif pattern == "rain":
            for _ in range(10):
                self.bullets.append(
                    {
                        "x": random.randint(0, self.width),
                        "y": -10,
                        "vx": (random.random() - 0.5) * speed * 0.5,
                        "vy": speed,
                        "size": 5,
                        "color": color,
                    }
                )

        elif pattern == "burst":
            for i in range(16):
                angle = (math.pi * 2 * i) / 16
                self.bullets.append(
                    {
                        "x": data["x"],
                        "y": data["y"],
                        "vx": math.cos(angle) * speed * 1.2,
                        "vy": math.sin(angle) * speed * 1.2,
                        "size": 6,
                        "color": color,
                    }
                )

    def update(self):
        if "left" in self.keys or "a" in self.keys:
            self.player["x"] -= self.player["speed"]
        if "right" in self.keys or "d" in self.keys:
            self.player["x"] += self.player["speed"]
        if "up" in self.keys or "w" in self.keys:
            self.player["y"] -= self.player["speed"]
        if "down" in self.keys or "s" in self.keys:
            self.player["y"] += self.player["speed"]

        self.player["x"] = max(
            self.player["size"], min(self.width - self.player["size"], self.player["x"])
        )
        self.player["y"] = max(
            self.player["size"],
            min(self.height - self.player["size"], self.player["y"]),
        )

        if self.is_endless:
            spawn_rate = max(5, 20 - (self.endless_score // 10))
        else:
            spawn_rate = self.levels[self.current_level]["spawn_rate"]

        if self.frame_count % spawn_rate == 0:
            self.spawn_bullets()
        self.frame_count += 1

        current_time = time.time()
        new_warnings = []
        for warning in self.warnings:
            if current_time - warning["created_at"] >= warning["duration"]:
                self.spawn_bullets_from_warning(warning)
            else:
                new_warnings.append(warning)
        self.warnings = new_warnings

        for bullet in self.bullets:
            bullet["x"] += bullet["vx"]
            bullet["y"] += bullet["vy"]

        self.bullets = [
            b
            for b in self.bullets
            if -50 < b["x"] < self.width + 50 and -50 < b["y"] < self.height + 50
        ]

        for bullet in self.bullets:
            dist = math.hypot(
                bullet["x"] - self.player["x"], bullet["y"] - self.player["y"]
            )
            if dist < self.player["size"] + bullet["size"]:
                self.game_over()
                return

        if not self.is_endless:
            elapsed = time.time() - self.start_time
            if elapsed >= self.levels[self.current_level]["duration"]:
                self.victory()
        else:
            self.endless_score = int(time.time() - self.start_time)

    def draw(self):
        self.canvas.delete("all")

        current_time = time.time()
        for warning in self.warnings:
            elapsed = current_time - warning["created_at"]
            progress = elapsed / warning["duration"]
            alpha_val = int((0.3 + math.sin(progress * math.pi * 8) * 0.3) * 255)

            pattern = warning["pattern"]
            data = warning["data"]
            color = self.pattern_colors[pattern]

            r = int(color[1:3], 16)
            g = int(color[3:5], 16)
            b = int(color[5:7], 16)
            warning_color = f"#{r:02x}{g:02x}{b:02x}"

            if pattern == "straight":
                side = data["side"]
                if side == 0:
                    self.canvas.create_line(
                        data["x"], 0, data["x"], 0, fill=warning_color, width=3
                    )
                    for i in range(5):
                        y = i * 20
                        self.canvas.create_polygon(
                            data["x"],
                            y + 10,
                            data["x"] - 5,
                            y,
                            data["x"] + 5,
                            y,
                            fill=warning_color,
                        )
                elif side == 1:
                    self.canvas.create_line(
                        self.width,
                        data["y"],
                        self.width,
                        data["y"],
                        fill=warning_color,
                        width=3,
                    )
                    for i in range(5):
                        x = self.width - i * 20
                        self.canvas.create_polygon(
                            x - 10,
                            data["y"],
                            x,
                            data["y"] - 5,
                            x,
                            data["y"] + 5,
                            fill=warning_color,
                        )
                elif side == 2:
                    self.canvas.create_line(
                        data["x"],
                        self.height,
                        data["x"],
                        self.height,
                        fill=warning_color,
                        width=3,
                    )
                    for i in range(5):
                        y = self.height - i * 20
                        self.canvas.create_polygon(
                            data["x"],
                            y - 10,
                            data["x"] - 5,
                            y,
                            data["x"] + 5,
                            y,
                            fill=warning_color,
                        )
                else:
                    self.canvas.create_line(
                        0, data["y"], 0, data["y"], fill=warning_color, width=3
                    )
                    for i in range(5):
                        x = i * 20
                        self.canvas.create_polygon(
                            x + 10,
                            data["y"],
                            x,
                            data["y"] - 5,
                            x,
                            data["y"] + 5,
                            fill=warning_color,
                        )

            elif pattern in ["circle", "spiral", "burst"]:
                radius = 30 + math.sin(progress * math.pi * 6) * 5
                self.canvas.create_oval(
                    data["x"] - radius,
                    data["y"] - radius,
                    data["x"] + radius,
                    data["y"] + radius,
                    outline=warning_color,
                    width=3,
                )
                self.canvas.create_oval(
                    data["x"] - 5,
                    data["y"] - 5,
                    data["x"] + 5,
                    data["y"] + 5,
                    fill=warning_color,
                )

            elif pattern == "wave":
                y = data["y"]
                self.canvas.create_line(
                    0, y, self.width, y, fill=warning_color, width=3
                )
                for i in range(5):
                    x = i * (self.width // 4)
                    if y < self.height / 2:
                        self.canvas.create_polygon(
                            x, y + 10, x - 5, y, x + 5, y, fill=warning_color
                        )
                    else:
                        self.canvas.create_polygon(
                            x, y - 10, x - 5, y, x + 5, y, fill=warning_color
                        )

            elif pattern == "cross":
                x, y = data["x"], data["y"]
                size = 40
                self.canvas.create_line(
                    x - size, y, x + size, y, fill=warning_color, width=3
                )
                self.canvas.create_line(
                    x, y - size, x, y + size, fill=warning_color, width=3
                )
                self.canvas.create_polygon(
                    x + size + 10,
                    y,
                    x + size,
                    y - 5,
                    x + size,
                    y + 5,
                    fill=warning_color,
                )
                self.canvas.create_polygon(
                    x - size - 10,
                    y,
                    x - size,
                    y - 5,
                    x - size,
                    y + 5,
                    fill=warning_color,
                )
                self.canvas.create_polygon(
                    x,
                    y + size + 10,
                    x - 5,
                    y + size,
                    x + 5,
                    y + size,
                    fill=warning_color,
                )
                self.canvas.create_polygon(
                    x,
                    y - size - 10,
                    x - 5,
                    y - size,
                    x + 5,
                    y - size,
                    fill=warning_color,
                )

            elif pattern == "rain":
                self.canvas.create_line(
                    0, 0, self.width, 0, fill=warning_color, width=3
                )

        for bullet in self.bullets:
            self.canvas.create_oval(
                bullet["x"] - bullet["size"],
                bullet["y"] - bullet["size"],
                bullet["x"] + bullet["size"],
                bullet["y"] + bullet["size"],
                fill=bullet["color"],
                outline="",
            )

        x, y = self.player["x"], self.player["y"]
        size = self.player["size"]
        self.canvas.create_polygon(
            x,
            y + size * 1.5,
            x - size,
            y + size / 4,
            x - size,
            y - size / 2,
            x,
            y + size / 4,
            x + size,
            y - size / 2,
            x + size,
            y + size / 4,
            fill="#ff0000",
            outline="",
            smooth=True,
        )

        if self.is_endless:
            self.ui_label.config(text=f"Score: {self.endless_score}")
        else:
            elapsed = time.time() - self.start_time
            remaining = max(0, self.levels[self.current_level]["duration"] - elapsed)
            self.ui_label.config(
                text=f"Level {self.current_level + 1} | Time: {remaining:.1f}s"
            )

    def game_loop(self):
        if not self.is_playing:
            return

        self.update()
        self.draw()
        self.master.after(16, self.game_loop)

    def game_over(self):
        self.is_playing = False
        messagebox.showinfo("Game Over", "GAME OVER!", parent=self.game_win)
        self.return_to_menu()

    def victory(self):
        self.is_playing = False

        if self.current_level not in self.completed_levels:
            self.completed_levels.append(self.current_level)

        if self.current_level >= self.max_level:
            self.max_level = min(9, self.current_level + 1)

        self.save_progress()

        if self.current_level < 9:
            result = messagebox.askyesno(
                "Victory!", "VICTORY!\n\nPlay next level?", parent=self.game_win
            )
            if result:
                self.canvas.destroy()
                self.ui_label.destroy()
                self.start_level(self.current_level + 1)
            else:
                self.return_to_menu()
        else:
            messagebox.showinfo(
                "Victory!",
                "VICTORY!\n\nYou completed all levels!",
                parent=self.game_win,
            )
            self.return_to_menu()

    def return_to_menu(self):
        self.is_playing = False
        for widget in self.game_win.winfo_children():
            widget.destroy()
        self.create_menu()


def bullet_hell(root):
    root_x = root.winfo_x() + (root.winfo_width() // 2) - 400
    root_y = root.winfo_y() + (root.winfo_height() // 2) - 300

    game_win = tk.Frame(
        root, bg="#1a1a2e", height=800, width=600, borderwidth=2, relief="ridge"
    )
    game_win.place(x=root_x, y=root_y)
    root.lift()
    make_draggable(game_win)

    title_bar = tk.Frame(game_win, bg="#333", height=25)
    title_bar.place(x=0, y=0, width=800, height=25)
    tk.Label(
        title_bar, text="Bullet Hell", bg="#333", fg="white", font=("Arial", 9)
    ).pack(side="left", padx=5)

    tk.Button(
        title_bar, text="x", command=game_win.destroy, bg="#333", fg="red", bd=0
    ).pack(side="right", padx=5)

    game = BulletHellGame(root, game_win)
