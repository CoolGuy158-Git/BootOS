import tkinter as tk

from core.drag import make_draggable


def Calculator(root):
    root_x = root.winfo_x() + (root.winfo_width() // 2) - 300
    root_y = root.winfo_y() + (root.winfo_height() // 2) - 300
    calc = tk.Frame(
        root, bg="grey", height=400, width=500, borderwidth=2, relief="ridge"
    )
    calc.place(x=root_x, y=root_y)
    root.lift()
    make_draggable(calc)
    # Screen
    Screen = tk.Label(
        calc,
        width=15,
        height=1,
        text=" ",
        bg="#0000CC",
        bd=5,
        relief="ridge",
        font=("Courier", 40, "bold"),
        fg="green",
    )
    Screen.place(x=0, y=0, width=500, height=80)

    cancel1 = tk.Button(
        calc, text="x", command=calc.destroy, fg="red", height=1, font=("Arial", 10)
    )
    cancel1.place(relx=1, rely=0, anchor="ne")
    cancel1.lift()

    # The Math
    # Show answer
    def show_input(value):
        current = Screen.cget("text")
        Screen.config(text=current + str(value))

    # Calculations
    def calculate():
        try:
            expression = Screen.cget("text")
            result = eval(expression)
            Screen.config(text=str(result))
        except (SyntaxError, ZeroDivisionError, TypeError, NameError):
            Screen.config(text="Error")
            Screen.after(1000, lambda: Screen.config(text=""))

    # for those who want press
    def keypress(event):
        key = event.char
        if key.isdigit() or key in "+-*/":
            show_input(key)
        elif key == "\r":
            calculate()
        elif key.lower() == "c":
            Screen.config(text="")

    calc.bind("<Key>", keypress)

    # numbers
    one = tk.Button(
        calc,
        width=10,
        height=2,
        text="1",
        bg="tan",
        activebackground="#a67c52",
        activeforeground="white",
        command=lambda: show_input(1),
    )
    one.place(x=34, y=110)
    two = tk.Button(
        calc,
        width=10,
        height=2,
        text="2",
        bg="tan",
        activebackground="#a67c52",
        activeforeground="white",
        command=lambda: show_input("2"),
    )
    two.place(x=34, y=160)
    three = tk.Button(
        calc,
        width=10,
        height=2,
        text="3",
        bg="tan",
        activebackground="#a67c52",
        activeforeground="white",
        command=lambda: show_input("3"),
    )
    three.place(x=34, y=210)
    four = tk.Button(
        calc,
        width=10,
        height=2,
        text="4",
        bg="tan",
        activebackground="#a67c52",
        activeforeground="white",
        command=lambda: show_input("4"),
    )
    four.place(x=34, y=260)
    five = tk.Button(
        calc,
        width=10,
        height=2,
        text="5",
        bg="tan",
        activebackground="#a67c52",
        activeforeground="white",
        command=lambda: show_input("5"),
    )
    five.place(x=34, y=310)
    six = tk.Button(
        calc,
        width=10,
        height=2,
        text="6",
        bg="tan",
        activebackground="#a67c52",
        activeforeground="white",
        command=lambda: show_input("6"),
    )
    six.place(x=134, y=110)
    seven = tk.Button(
        calc,
        width=10,
        height=2,
        text="7",
        bg="tan",
        activebackground="#a67c52",
        activeforeground="white",
        command=lambda: show_input("7"),
    )
    seven.place(x=134, y=160)
    eight = tk.Button(
        calc,
        width=10,
        height=2,
        text="8",
        bg="tan",
        activebackground="#a67c52",
        activeforeground="white",
        command=lambda: show_input("8"),
    )
    eight.place(x=134, y=210)
    nine = tk.Button(
        calc,
        width=10,
        height=2,
        text="9",
        bg="tan",
        activebackground="#a67c52",
        activeforeground="white",
        command=lambda: show_input("9"),
    )
    nine.place(x=134, y=260)
    zero = tk.Button(
        calc,
        width=10,
        height=2,
        text="0",
        bg="tan",
        activebackground="#a67c52",
        activeforeground="white",
        command=lambda: show_input("0"),
    )
    zero.place(x=134, y=310)
    # operation symbol
    addition = tk.Button(
        calc,
        width=15,
        height=2,
        text="+",
        bg="tan",
        activebackground="#a67c52",
        activeforeground="white",
        command=lambda: show_input("+"),
    )
    addition.place(x=234, y=110)
    subtraction = tk.Button(
        calc,
        width=15,
        height=2,
        text="-",
        bg="tan",
        activebackground="#a67c52",
        activeforeground="white",
        command=lambda: show_input("-"),
    )
    subtraction.place(x=234, y=160)
    division = tk.Button(
        calc,
        width=15,
        height=2,
        text="/",
        bg="tan",
        activebackground="#a67c52",
        activeforeground="white",
        command=lambda: show_input("/"),
    )
    division.place(x=234, y=210)
    multiplication = tk.Button(
        calc,
        width=15,
        height=2,
        text="*",
        bg="tan",
        activebackground="#a67c52",
        activeforeground="white",
        command=lambda: show_input("*"),
    )
    multiplication.place(x=234, y=260)
    equal = tk.Button(
        calc,
        width=15,
        height=10,
        text="=",
        bg="tan",
        activebackground="#a67c52",
        activeforeground="white",
        command=calculate,
    )
    equal.place(x=360, y=145)
    # The Extras
    Clear = tk.Button(
        calc,
        width=15,
        height=2,
        text="Clear",
        bg="tan",
        activebackground="#a67c52",
        activeforeground="white",
        command=lambda: Screen.config(text=""),
    )
    Clear.place(x=234, y=310)
