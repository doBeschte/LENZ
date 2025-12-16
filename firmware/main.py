
import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros


keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)


PINS = [board.D0, board.D1, board.D2, board.D3, board.GP6, board.GP7, board.GP0, board.GP3, board.GP4, board.GP2, board.GP1]


keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [KC.ESCAPE, KC.A, KC.W, KC.E, KC.D, KC.R, KC.Q, KC.S, KC.SPACE, KC.ENTER, KC.LSHIFT]
]

if __name__ == '__main__':
    keyboard.go()