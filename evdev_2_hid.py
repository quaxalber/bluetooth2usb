import logging

from evdev import ecodes
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse

logging.basicConfig(level=logging.INFO, filename='/var/log/bluetooth_2_usb.log')

class Converter:
    def __init__(self):
        # Mapping from evdev ecode to HID Keycode
        self.evdev_to_hid = {
            ecodes.KEY_RESERVED: 0x00,
            ecodes.KEY_A: Keycode.A,
            ecodes.KEY_B: Keycode.B,
            ecodes.KEY_C: Keycode.C,
            ecodes.KEY_D: Keycode.D,
            ecodes.KEY_E: Keycode.E,
            ecodes.KEY_F: Keycode.F,
            ecodes.KEY_G: Keycode.G,
            ecodes.KEY_H: Keycode.H,
            ecodes.KEY_I: Keycode.I,
            ecodes.KEY_J: Keycode.J,
            ecodes.KEY_K: Keycode.K,
            ecodes.KEY_L: Keycode.L,
            ecodes.KEY_M: Keycode.M,
            ecodes.KEY_N: Keycode.N,
            ecodes.KEY_O: Keycode.O,
            ecodes.KEY_P: Keycode.P,
            ecodes.KEY_Q: Keycode.Q,
            ecodes.KEY_R: Keycode.R,
            ecodes.KEY_S: Keycode.S,
            ecodes.KEY_T: Keycode.T,
            ecodes.KEY_U: Keycode.U,
            ecodes.KEY_V: Keycode.V,
            ecodes.KEY_W: Keycode.W,
            ecodes.KEY_X: Keycode.X,
            ecodes.KEY_Y: Keycode.Y,
            ecodes.KEY_Z: Keycode.Z,
            ecodes.KEY_1: Keycode.ONE,
            ecodes.KEY_2: Keycode.TWO,
            ecodes.KEY_3: Keycode.THREE,
            ecodes.KEY_4: Keycode.FOUR,
            ecodes.KEY_5: Keycode.FIVE,
            ecodes.KEY_6: Keycode.SIX,
            ecodes.KEY_7: Keycode.SEVEN,
            ecodes.KEY_8: Keycode.EIGHT,
            ecodes.KEY_9: Keycode.NINE,
            ecodes.KEY_0: Keycode.ZERO,
            ecodes.KEY_ENTER: Keycode.ENTER,
            ecodes.KEY_ESC: Keycode.ESCAPE,
            ecodes.KEY_BACKSPACE: Keycode.BACKSPACE,
            ecodes.KEY_TAB: Keycode.TAB,
            ecodes.KEY_SPACE: Keycode.SPACEBAR,
            ecodes.KEY_MINUS: Keycode.MINUS,
            ecodes.KEY_EQUAL: Keycode.EQUALS,
            ecodes.KEY_LEFTBRACE: Keycode.LEFT_BRACKET,
            ecodes.KEY_RIGHTBRACE: Keycode.RIGHT_BRACKET,
            ecodes.KEY_BACKSLASH: Keycode.POUND,
            ecodes.KEY_SEMICOLON: Keycode.SEMICOLON,
            ecodes.KEY_APOSTROPHE: Keycode.QUOTE,
            ecodes.KEY_GRAVE: Keycode.GRAVE_ACCENT,
            ecodes.KEY_COMMA: Keycode.COMMA,
            ecodes.KEY_DOT: Keycode.PERIOD,
            ecodes.KEY_SLASH: Keycode.FORWARD_SLASH,
            ecodes.KEY_CAPSLOCK: Keycode.CAPS_LOCK,
            ecodes.KEY_F1: Keycode.F1,
            ecodes.KEY_F2: Keycode.F2,
            ecodes.KEY_F3: Keycode.F3,
            ecodes.KEY_F4: Keycode.F4,
            ecodes.KEY_F5: Keycode.F5,
            ecodes.KEY_F6: Keycode.F6,
            ecodes.KEY_F7: Keycode.F7,
            ecodes.KEY_F8: Keycode.F8,
            ecodes.KEY_F9: Keycode.F9,
            ecodes.KEY_F10: Keycode.F10,
            ecodes.KEY_F11: Keycode.F11,
            ecodes.KEY_F12: Keycode.F12,
            ecodes.KEY_SYSRQ: Keycode.PRINT_SCREEN,
            ecodes.KEY_SCROLLLOCK: Keycode.SCROLL_LOCK,
            ecodes.KEY_PAUSE: Keycode.PAUSE,
            ecodes.KEY_INSERT: Keycode.INSERT,
            ecodes.KEY_HOME: Keycode.HOME,
            ecodes.KEY_PAGEUP: Keycode.PAGE_UP,
            ecodes.KEY_DELETE: Keycode.DELETE,
            ecodes.KEY_END: Keycode.END,
            ecodes.KEY_PAGEDOWN: Keycode.PAGE_DOWN,
            ecodes.KEY_RIGHT: Keycode.RIGHT_ARROW,
            ecodes.KEY_LEFT: Keycode.LEFT_ARROW,
            ecodes.KEY_DOWN: Keycode.DOWN_ARROW,
            ecodes.KEY_UP: Keycode.UP_ARROW,
            ecodes.KEY_NUMLOCK: Keycode.KEYPAD_NUMLOCK,
            ecodes.KEY_KPSLASH: Keycode.KEYPAD_FORWARD_SLASH,
            ecodes.KEY_KPASTERISK: Keycode.KEYPAD_ASTERISK,
            ecodes.KEY_KPMINUS: Keycode.KEYPAD_MINUS,
            ecodes.KEY_KPPLUS: Keycode.KEYPAD_PLUS,
            ecodes.KEY_KPENTER: Keycode.KEYPAD_ENTER,
            ecodes.KEY_KP1: Keycode.KEYPAD_ONE,
            ecodes.KEY_KP2: Keycode.KEYPAD_TWO,
            ecodes.KEY_KP3: Keycode.KEYPAD_THREE,
            ecodes.KEY_KP4: Keycode.KEYPAD_FOUR,
            ecodes.KEY_KP5: Keycode.KEYPAD_FIVE,
            ecodes.KEY_KP6: Keycode.KEYPAD_SIX,
            ecodes.KEY_KP7: Keycode.KEYPAD_SEVEN,
            ecodes.KEY_KP8: Keycode.KEYPAD_EIGHT,
            ecodes.KEY_KP9: Keycode.KEYPAD_NINE,
            ecodes.KEY_KP0: Keycode.KEYPAD_ZERO,
            ecodes.KEY_KPDOT: Keycode.KEYPAD_PERIOD,
            ecodes.KEY_102ND: Keycode.KEYPAD_BACKSLASH,
            ecodes.KEY_COMPOSE: Keycode.APPLICATION,
            ecodes.KEY_POWER: Keycode.POWER,
            ecodes.KEY_KPEQUAL: Keycode.KEYPAD_EQUALS,
            ecodes.KEY_F13: Keycode.F13,
            ecodes.KEY_F14: Keycode.F14,
            ecodes.KEY_F15: Keycode.F15,
            ecodes.KEY_F16: Keycode.F16,
            ecodes.KEY_F17: Keycode.F17,
            ecodes.KEY_F18: Keycode.F18,
            ecodes.KEY_F19: Keycode.F19,
            ecodes.KEY_F20: Keycode.F20,
            ecodes.KEY_F21: Keycode.F21,
            ecodes.KEY_F22: Keycode.F22,
            ecodes.KEY_F23: Keycode.F23,
            ecodes.KEY_F24: Keycode.F24,
            ecodes.KEY_OPEN: 0x74,
            ecodes.KEY_HELP: 0x75,
            ecodes.KEY_PROPS: 0x76,
            ecodes.KEY_FRONT: 0x77,
            ecodes.KEY_MENU: 0x79,
            ecodes.KEY_UNDO: 0x7A,
            ecodes.KEY_CUT: 0x7B,
            ecodes.KEY_COPY: 0x7C,
            ecodes.KEY_PASTE: 0x7D,
            ecodes.KEY_AGAIN: 0x85,
            ecodes.KEY_RO: 0x87,
            ecodes.KEY_KATAKANAHIRAGANA: 0x88,
            ecodes.KEY_YEN: 0x89,
            ecodes.KEY_HENKAN: 0x8A,
            ecodes.KEY_HANJA: 0x8B,
            ecodes.KEY_KPCOMMA: 0x8C,
            ecodes.KEY_SCALE: 0x91,
            ecodes.KEY_HIRAGANA: 0x92,
            ecodes.KEY_KATAKANA: 0x93,
            ecodes.KEY_MUHENKAN: 0x94,
            ecodes.KEY_LEFTCTRL: Keycode.LEFT_CONTROL,
            ecodes.KEY_LEFTSHIFT: Keycode.LEFT_SHIFT,
            ecodes.KEY_LEFTALT: Keycode.LEFT_ALT,
            ecodes.KEY_LEFTMETA: Keycode.LEFT_GUI,
            ecodes.KEY_RIGHTCTRL: Keycode.RIGHT_CONTROL,
            ecodes.KEY_RIGHTSHIFT: Keycode.RIGHT_SHIFT,
            ecodes.KEY_RIGHTALT: Keycode.RIGHT_ALT,
            ecodes.KEY_RIGHTMETA: Keycode.RIGHT_GUI,
            ecodes.KEY_PLAYPAUSE: 0xE8,
            ecodes.KEY_STOPCD: 0xE9,
            ecodes.KEY_PREVIOUSSONG: 0xEA,
            ecodes.KEY_NEXTSONG: 0xEB,
            ecodes.KEY_EJECTCD: 0xEC,
            ecodes.KEY_VOLUMEUP: 0xED,
            ecodes.KEY_VOLUMEDOWN: 0xEE,
            ecodes.KEY_WWW: 0xF0,
            ecodes.KEY_MAIL: 0xF1,
            ecodes.KEY_FORWARD: 0xF2,
            ecodes.KEY_STOP: 0xF3,
            ecodes.KEY_FIND: 0xF4,
            ecodes.KEY_SCROLLUP: 0xF5,
            ecodes.KEY_SCROLLDOWN: 0xF6,
            ecodes.KEY_EDIT: 0xF7,
            ecodes.KEY_SLEEP: 0xF8,
            ecodes.KEY_REFRESH: 0xFA,
            ecodes.KEY_CALC: 0xFB,
        }
    
    def to_hid_key(self, event):
        key = self.evdev_to_hid.get(event.code, None)
        if key is None:
            logging.warning(f"Unsupported key pressed: {event}")
        return key
    
    def to_hid_mouse_button(self, event):
        button = None  

        if event.code == ecodes.BTN_LEFT:
            button = Mouse.LEFT_BUTTON
        elif event.code == ecodes.BTN_RIGHT:
            button = Mouse.RIGHT_BUTTON
        elif event.code == ecodes.BTN_MIDDLE:
            button = Mouse.MIDDLE_BUTTON  

        if button is None:
            logging.warning(f"Unsupported mouse button pressed: {event}")
        return button
