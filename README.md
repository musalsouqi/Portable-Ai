# Portable-Ai

This repository contains a Python script for controlling an LCD display via I2C. The script includes functions to initialize the LCD, send commands and data, and display text on the screen. The LCD can be connected to a Raspberry Pi or similar devices.

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Functions](#functions)
- [License](#license)

## Requirements

- Python 3
- `smbus2` library
- `i2cdetect` utility (part of the `i2c-tools` package)

## Installation

1. **Install required Python library:**
   ```sh
   pip install smbus2
   ```

2. **Install `i2c-tools` on your Raspberry Pi:**
   ```sh
   sudo apt-get install -y i2c-tools
   ```

3. **Clone this repository:**
   ```sh
   git clone https://github.com/your-username/lcd-display-controller.git
   cd lcd-display-controller
   ```

## Usage

1. **Enable I2C on your Raspberry Pi:**
   ```sh
   sudo raspi-config
   ```
   Go to `Interfacing Options` -> `I2C` -> `Enable`.

2. **Run the script:**
   ```sh
   python3 lcd_display.py
   ```

This will display "Hello" on the first line and "world!" on the second line of the LCD.

## Functions

### `write_word(addr, data)`
Writes a word to the specified I2C address.

### `send_command(comm)`
Sends a command to the LCD.

### `send_data(data)`
Sends data to the LCD.

### `i2c_scan()`
Scans for I2C devices and returns a list of found addresses.

### `init(addr=None, bl=1)`
Initializes the LCD. If no address is provided, it scans for 0x27 or 0x3f.

### `clear()`
Clears the LCD screen.

### `openlight()`
Enables the LCD backlight.

### `write(x, y, str)`
Writes a string to the LCD at the specified position.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Feel free to reach out if you have any questions or suggestions! Happy coding!
