import random
import tkinter as tk

from core.drag import make_draggable


class TetrisGame:
    def __init__(self, master):
        self.master = master
        self.rows = 20
        self.cols = 10
        self.cell_size = 25

        self.colors = [
            "#00f0f0",
            "#0000f0",
            "#f0a000",
            "#f0f000",
            "#00f000",
            "#a000f0",
            "#f00000",
        ]
        self.shapes = [
            [[1, 1, 1, 1]],
            [[1, 1, 1], [0, 0, 1]],
            [[1, 1, 1], [1, 0, 0]],
            [[1, 1], [1, 1]],
            [[0, 1, 1], [1, 1, 0]],
            [[1, 1, 1], [0, 1, 0]],
            [[1, 1, 0], [0, 1, 1]],
        ]

        self.canvas = tk.Canvas(
            master,
            width=self.cols * self.cell_size,
            height=self.rows * self.cell_size,
            bg="#111",
            highlightthickness=0,
        )
        self.canvas.pack(padx=10, pady=10, side="left")

        self.stats_frame = tk.Frame(master, bg="#333", width=150)
        self.stats_frame.pack(side="right", fill="y", padx=5)

        self.score_label = tk.Label(
            self.stats_frame, text="Score: 0", bg="#333", fg="white", font=("Arial", 12)
        )
        self.score_label.pack(pady=20)

        self.reset_game()

    def reset_game(self):
        self.board = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        self.score = 0
        self.game_over = False
        self.current_piece = self.new_piece()
        self.update_score(0)
        self.run_game()

    def new_piece(self):
        shape = random.choice(self.shapes)
        color = random.choice(self.colors)
        return {
            "shape": shape,
            "color": color,
            "x": self.cols // 2 - len(shape[0]) // 2,
            "y": 0,
        }

    def check_collision(self, dx=0, dy=0, shape=None):
        if shape is None:
            shape = self.current_piece["shape"]
        for r, row in enumerate(shape):
            for c, val in enumerate(row):
                if val:
                    new_x = self.current_piece["x"] + c + dx
                    new_y = self.current_piece["y"] + r + dy
                    if new_x < 0 or new_x >= self.cols or new_y >= self.rows:
                        return True
                    if new_y >= 0 and self.board[new_y][new_x]:
                        return True
        return False

    def merge_piece(self):
        for r, row in enumerate(self.current_piece["shape"]):
            for c, val in enumerate(row):
                if val:
                    self.board[self.current_piece["y"] + r][
                        self.current_piece["x"] + c
                    ] = self.current_piece["color"]
        self.clear_lines()
        self.current_piece = self.new_piece()
        if self.check_collision():
            self.game_over = True

    def clear_lines(self):
        lines_to_clear = [i for i, row in enumerate(self.board) if all(row)]
        for i in lines_to_clear:
            del self.board[i]
            self.board.insert(0, [None for _ in range(self.cols)])
        if lines_to_clear:
            self.update_score(len(lines_to_clear) * 100)

    def update_score(self, points):
        self.score += points
        self.score_label.config(text=f"Score: {self.score}")

    def move(self, dx, dy):
        if not self.game_over:
            if not self.check_collision(dx, dy):
                self.current_piece["x"] += dx
                self.current_piece["y"] += dy
                self.draw()
            elif dy > 0:
                self.merge_piece()
                self.draw()

    def rotate(self):
        if not self.game_over:
            new_shape = list(zip(*self.current_piece["shape"][::-1]))
            if not self.check_collision(shape=new_shape):
                self.current_piece["shape"] = new_shape
                self.draw()

    def draw(self):
        self.canvas.delete("all")
        for r, row in enumerate(self.board):
            for c, color in enumerate(row):
                if color:
                    self.draw_block(c, r, color)

        if not self.game_over:
            for r, row in enumerate(self.current_piece["shape"]):
                for c, val in enumerate(row):
                    if val:
                        self.draw_block(
                            self.current_piece["x"] + c,
                            self.current_piece["y"] + r,
                            self.current_piece["color"],
                        )
        else:
            self.canvas.create_text(
                self.cols * self.cell_size // 2,
                self.rows * self.cell_size // 2,
                text="GAME OVER",
                fill="white",
                font=("Arial", 20, "bold"),
            )

    def draw_block(self, x, y, color):
        self.canvas.create_rectangle(
            x * self.cell_size,
            y * self.cell_size,
            (x + 1) * self.cell_size,
            (y + 1) * self.cell_size,
            fill=color,
            outline="#222",
        )

    def run_game(self):
        if not self.game_over:
            self.move(0, 1)
            self.master.after(500, self.run_game)


def tetris_app(root):
    tetris_win = tk.Frame(root, bg="#333", borderwidth=10, relief="ridge")
    tetris_win.place(x=200, y=100)
    make_draggable(tetris_win)

    title_bar = tk.Frame(tetris_win, bg="#111", height=25)
    title_bar.pack(side="top", fill="x")
    tk.Label(title_bar, text="Tetris.exe", bg="#111", fg="white").pack(
        side="left", padx=5
    )
    tk.Button(
        title_bar, text="x", command=tetris_win.destroy, bg="#111", fg="red", bd=0
    ).pack(side="right")

    game = TetrisGame(tetris_win)

    def handle_key(event):
        if event.keysym == "Left":
            game.move(-1, 0)
        if event.keysym == "Right":
            game.move(1, 0)
        if event.keysym == "Down":
            game.move(0, 1)
        if event.keysym == "Up":
            game.rotate()

    root.bind("<Left>", handle_key)
    root.bind("<Right>", handle_key)
    root.bind("<Down>", handle_key)
    root.bind("<Up>", handle_key)
