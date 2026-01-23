<h1 align='center'>BootOS: Python-Based OS Simulator</h1>

---------

**BootOS** is a lightweight Python simulation of a bootable operating system environment, implemented using Tkinter. It provides an interactive graphical user interface (GUI) that emulates a boot process, desktop, and basic applications, offering an engaging way to explore Python concepts such as event handling, window management, and user interactions. This project is ideal for educational purposes, demonstrating loops, conditionals, functions, and GUI development in a simulated OS context.

## Description
BootOS simulates a minimal bootable OS with a console-like boot sequence transitioning into a graphical desktop. Users can launch draggable applications like a calculator and a cookie-clicking game, monitor a live clock, and interact with a simple start menu. The simulation includes ASCII art for the boot screen and sequential log displays to mimic system initialization. It is designed to be fun and educational, blending nostalgia for early OS aesthetics with practical Python coding exercises.

Note: This is a GUI-focused simulation; command-line elements are emulated visually during boot for immersion.

----------
<details>
   <summary><h2>Installation guide</h2></summary>
   
- [ ] 1. **Clone the Repository**:
   
   ```
   git clone https://github.com/CoolGuy158-Git/BootOS.git
   cd BootOS
   ```

- [ ] 2. **Run the Simulator**:

   Ensure Python 3.8+ is installed. Execute the script:
   ```
   python BootOS.py
   ```
   On some systems:
   ```
   py BootOS.py
   ```

- [ ] 3. **Optional: Build Executable**:

   To create a standalone .exe file (Windows only):
   ```
   pip install pyinstaller Pillow
   pyinstaller --onefile --console BootOS.py
   ```
   The executable will be generated in the `dist/` folder as `BootOS.exe`. (Pillow is required for image handling in the cookie game.)

Place a `cookie.png` file in the project directory for the full cookie-clicker experience; otherwise, it defaults to text-only.
</details>

-------
<details>
   <summary><h2>Features</h2></summary>
      
| Apps          | Function                                           | 
|---------------|----------------------------------------------------| 
| Bullet Hell   | Dodge endless bullet patterns                      | 
| Calculator    | Perform math calculations (basic or scientific)    | 
| Cookie Clicker| Click to earn cookies, buy upgrades for idle gains | 
| Terminal      | Run commands, simulate hacking or control system   |
| Paint App     | Draw with mouse/pen tools                          |
| Rpg Typer     | Type words/phrases to battle in an RPG style       |
| Tetris        | Rotate and drop tetrominoes to clear lines         |
| Notepad       | Write, edit, and save plain text notes             |
</details>

-----
## Contributors:

[CoolGuy158-Git](https://github.com/CoolGuy158-Git)

**and**

[KamiruKun](https://github.com/KamiruKun)

## License and language used:

![Python](https://img.shields.io/badge/python-3.8+-blue)
![License](https://img.shields.io/badge/license-MIT-green)




