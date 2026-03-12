import time
import board
import digitalio
import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

print("StreamDeck simple mode")

kbd = Keyboard(usb_hid.devices)

# ----------------------------
# Buttons
# ----------------------------

button_pins = [board.GP2, board.GP3, board.GP4, board.GP5]

buttons = []

for pin in button_pins:

    btn = digitalio.DigitalInOut(pin)
    btn.direction = digitalio.Direction.INPUT
    btn.pull = digitalio.Pull.UP

    buttons.append(btn)

print("Buttons ready")

# ----------------------------
# Keymap
# ----------------------------

keys = [
    Keycode.F13,
    Keycode.F14,
    Keycode.F15,
    Keycode.F16
]

last_state = [True, True, True, True]

print("Entering loop")

while True:

    for i, btn in enumerate(buttons):

        state = btn.value

        if last_state[i] and not state:

            print("BUTTON", i, "PRESSED")

            try:

                kbd.press(keys[i])
                kbd.release_all()

                print("KEY SENT", keys[i])

            except Exception as e:

                print("ERROR", e)

            time.sleep(0.05)

        last_state[i] = state

    time.sleep(0.01)
