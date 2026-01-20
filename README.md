# BootOS: Python-Based OS Simulator

**BootOS** is a lightweight Python simulation of a bootable operating system environment, implemented using Tkinter. It provides an interactive graphical user interface (GUI) that emulates a boot process, desktop, and basic applications, offering an engaging way to explore Python concepts such as event handling, window management, and user interactions. This project is ideal for educational purposes, demonstrating loops, conditionals, functions, and GUI development in a simulated OS context.

## Description
BootOS simulates a minimal bootable OS with a console-like boot sequence transitioning into a graphical desktop. Users can launch draggable applications like a calculator and a cookie-clicking game, monitor a live clock, and interact with a simple start menu. The simulation includes ASCII art for the boot screen and sequential log displays to mimic system initialization. It is designed to be fun and educational, blending nostalgia for early OS aesthetics with practical Python coding exercises.

## Features
- Boot Sequence: ASCII art logo + animated system logs (“Kernel [OK]”) leading to a desktop.

- Desktop Environment: Fullscreen GUI with taskbar, live clock, start menu, and application launchers.

- Draggable Calculator: Retro-style calculator with keyboard input and error handling.

- Cookie Clicker Game: Click to increment score; high scores saved in high_score.txt.

- RPG_Typer: Typing-based mini RPG game, added by contributor KamiruKun.

- Terminal: Basic terminal emulator for command input, added by KamiruKun.

- Window Management: All windows are draggable, centered on launch, with close buttons.

- Start Menu: Popup for system shutdown.

- Visuals: Black boot screen with green text, then standard desktop layout.

Note: This is a GUI-focused simulation; command-line elements are emulated visually during boot for immersion.

## Installation
1. **Clone the Repository**:
   ```
   git clone https://github.com/CoolGuy158-Git/BootOS.git
   cd BootOS
   ```

2. **Run the Simulator**:
   Ensure Python 3.8+ is installed. Execute the script:
   ```
   python BootOS.py
   ```
   On some systems:
   ```
   py BootOS.py
   ```

3. **Optional: Build Executable**:
   To create a standalone .exe file (Windows only):
   ```
   pip install pyinstaller Pillow
   pyinstaller --onefile --console BootOS.py
   ```
   The executable will be generated in the `dist/` folder as `BootOS.exe`. (Pillow is required for image handling in the cookie game.)

Place a `cookie.png` file in the project directory for the full cookie-clicker experience; otherwise, it defaults to text-only.

## Usage
- Launch the script to initiate the boot sequence (approximately 10 seconds).
- Once the desktop loads, use the taskbar icons to open applications:
  - **Calculator.exe**: Click to open the draggable calculator window. Enter expressions via buttons or keyboard; press `=` or Enter to evaluate.
  - **CookieClicker.exe**: Click the central button to increment your score. High scores are automatically saved.
- Drag windows by clicking and holding the title area.
- Access the **Start Menu** from the taskbar for shutdown.
- Close individual windows using the red "x" button in the top-right corner.

The simulation runs in fullscreen mode for an immersive experience. Use the start menu to quit.

For a full list of interactive elements, explore the boot logs and desktop post-launch.

## Notes
- The boot delay (9.5 seconds) simulates real OS initialization; adjust `root.after()` timings in the code if needed.
- High-score data is stored in `high_score.txt` in the project directory.
- Application windows are positioned relative to the root window's dimensions for centering.
- This project is experimental and focused on Tkinter basics; extend it with additional apps or features as desired.
- Potential enhancements: Add more applications, sound effects, or persistence across sessions.

##### Image Credits
pixelartmaker.com was where the cookie.png was from

## License
This project is provided for educational and personal use. It is released under a permissive license—feel free to modify, extend, or distribute the code. Attribution is appreciated but not required. For commercial use, review the code for any third-party dependencies.

---
*I am going to be updating this project every week.*

*Project maintained by CoolGuy158-Git. Contributions via pull requests are welcome.*


