# Enigma Console

**Enigma Console** is a custom furniture automation project.  
It uses a **Raspberry Pi Zero 2 W** running a **Python GUI** and communicates over **UART** with a **Raspberry Pi Pico**, which drives a servo/motor to open and close a console lid like a bridge.

Designed as a **special product** for digital control of a furniture console.

---

## 🚀 Features
- Touch-friendly **PyQt5 GUI** (`enigma-gui.ui`, `main.py`)
- Secure password management (bcrypt) with reset mechanism
- Configuration stored in `parameters.json`
- UART communication between Pi Zero and Pico
- **RPi Pico firmware (`main_pico.py`)** for motor control with soft start/stop
- Reset password generator utility (`sifirlama_sifresi.py`)

---

## 📂 Project Structure
├── enigma-gui.ui # Qt Designer file for GUI
├── main.py # Python GUI (RPi Zero 2 W)
├── parameters.json # Runtime configuration
├── main_pico.py # Pico firmware (MicroPython)
├── sifirlama_sifresi.py # Reset password generator tool


---

## ⚙️ Requirements (RPi Zero 2 W)
Install Python dependencies:

```bash
sudo apt update
sudo apt install python3-pyqt5 python3-serial python3-bcrypt wmctrl
```
Or via pip:
```bash
sudo pip install pyqt5 pyserial bcrypt
```

## ▶️ Running the GUI
```bash
python3 main.py
```
Open/Close buttons → send UART commands (0,50,2000\n or 1,50,2000\n)
GUI displays current state and requires password if enabled
parameters.json keeps last position, working mode, and hashed keys

---
## 🔧 RPi Pico Firmware
- main_pico.py runs on Raspberry Pi Pico (MicroPython).
- Receives UART messages in format:
  <direction>,<duty_cycle>,<duration>
Example:
0,50,2000   # Open
1,50,2000   # Close

Controls PWM output on pin GP3 with soft start.
Replies back over UART:
open
close

🔑 Reset Password Utility
 - python3 sifirlama_sifresi.py

Enter the values shown in settings screen corners
Utility calculates a unique reset code for the device.

🧑‍🤝‍🧑 Project Team
UI Designer: @kursattoz
Project Coordinator: @atilganmali
Software & Hardware Developer: @seckinsertaclalli
