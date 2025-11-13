# BootOS: Python-Based OS Simulator

**BootOS** is a lightweight Python simulation of a bootable operating system environment, implemented using Tkinter. It provides an interactive graphical user interface (GUI) that emulates a boot process, desktop, and basic applications, offering an engaging way to explore Python concepts such as event handling, window management, and user interactions. This project is ideal for educational purposes, demonstrating loops, conditionals, functions, and GUI development in a simulated OS context.

## Description
BootOS simulates a minimal bootable OS with a console-like boot sequence transitioning into a graphical desktop. Users can launch draggable applications like a calculator and a cookie-clicking game, monitor a live clock, and interact with a simple start menu. The simulation includes ASCII art for the boot screen and sequential log displays to mimic system initialization. It is designed to be fun and educational, blending nostalgia for early OS aesthetics with practical Python coding exercises.

## Features
- **Boot Sequence**: ASCII art logo followed by animated system logs (e.g., "Kernel [OK]") that culminate in a desktop reveal after a simulated delay.
- **Desktop Environment**: Fullscreen GUI with a taskbar featuring a live clock, start menu button, and application launchers.
- **Draggable Calculator Application**: A retro-style calculator with a digital display, numeric keypad, arithmetic operations (+, -, *, /), clear function, and keyboard input support. Handles errors gracefully (e.g., division by zero).
- **Cookie Clicker Game**: A simple idle game where users click a central image to increment a score, with persistent high-score tracking via a text file.
- **Window Management**: All application windows are draggable, centered on launch, and include close buttons for user control.
- **Start Menu**: A basic popup for system shutdown, maintaining a clean and minimal interface.
- **Visual Elements**: Black boot screen with green text for authenticity, transitioning to a standard desktop layout with a gray taskbar.

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

**Dependencies**:
- Tkinter (included with standard Python installations).
- Time (included with standard Python installations).
- Os (included with standard Python installations).
- Pillow (`pip install Pillow`) for image processing (e.g., `cookie.png`).

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

## Application Overview
| Application          | Description                                                                 | Controls |
|----------------------|-----------------------------------------------------------------------------|----------|
| **Calculator.exe**  | Basic arithmetic calculator with error handling.                            | Buttons for digits/operators; keyboard support for input and Enter for calculation. |
| **CookieClicker.exe** | Score-based clicking game with high-score persistence.                     | Click the central "Cookie" button to increment score. |
| **Clock**           | Live time display in the taskbar.                                           | Automatic updates every second. |
| **Start Menu**      | System control popup.                                                       | "Shutdown" button to exit the simulation. |
| **BootVer**         | Shows "OS" version.                                                         | Read Only. |
| **Notepad.exe**     | Allows you to write                                                         | Click any key to write, enter to add a new line of text. |
| **Paint.exe**       | Allows you to draw                                                          | Hold left key to draw, toggle colors using "color" button, fill using "fill" button, and clear using "clear" button. |

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

