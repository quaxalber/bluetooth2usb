from evdev import ecodes

import lib.logger
from adafruit_hid.keycode import Keycode, MouseButton

logger = lib.logger.get_logger()

_EVDEV_TO_HID_MAPPING = {
    ecodes.KEY_RESERVED: None,
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
    ecodes.KEY_KPCOMMA: Keycode.KEYPAD_COMMA,
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
    ecodes.KEY_OPEN: None,
    ecodes.KEY_HELP: None,
    ecodes.KEY_PROPS: None,
    ecodes.KEY_FRONT: None,
    ecodes.KEY_MENU: None,
    ecodes.KEY_UNDO: None,
    ecodes.KEY_CUT: None,
    ecodes.KEY_COPY: None,
    ecodes.KEY_PASTE: None,
    ecodes.KEY_AGAIN: None,
    ecodes.KEY_LEFTCTRL: Keycode.LEFT_CONTROL,
    ecodes.KEY_LEFTSHIFT: Keycode.LEFT_SHIFT,
    ecodes.KEY_LEFTALT: Keycode.LEFT_ALT,
    ecodes.KEY_LEFTMETA: Keycode.LEFT_GUI,
    ecodes.KEY_RIGHTCTRL: Keycode.RIGHT_CONTROL,
    ecodes.KEY_RIGHTSHIFT: Keycode.RIGHT_SHIFT,
    ecodes.KEY_RIGHTALT: Keycode.RIGHT_ALT,
    ecodes.KEY_RIGHTMETA: Keycode.RIGHT_GUI,
    ecodes.KEY_PLAYPAUSE: None,
    ecodes.KEY_STOPCD: None,
    ecodes.KEY_PREVIOUSSONG: None,
    ecodes.KEY_NEXTSONG: None,
    ecodes.KEY_EJECTCD: None,
    ecodes.KEY_VOLUMEUP: None,
    ecodes.KEY_VOLUMEDOWN: None,
    ecodes.KEY_WWW: None,
    ecodes.KEY_MAIL: None,
    ecodes.KEY_FORWARD: None,
    ecodes.KEY_STOP: None,
    ecodes.KEY_FIND: None,
    ecodes.KEY_SCROLLUP: None,
    ecodes.KEY_SCROLLDOWN: None,
    ecodes.KEY_EDIT: None,
    ecodes.KEY_SLEEP: None,
    ecodes.KEY_REFRESH: None,
    ecodes.KEY_CALC: None,
    ecodes.KEY_MUTE: None,
    ecodes.KEY_COFFEE: None,
    ecodes.KEY_BACK: None,
    ecodes.BTN_LEFT: MouseButton.LEFT,
    ecodes.BTN_RIGHT: MouseButton.RIGHT,
    ecodes.BTN_MIDDLE: MouseButton.MIDDLE,
}
"""
Mapping from evdev ecode to HID Keycode
"""


def to_hid_key(ecode: int) -> int | None:
    hid_key = _EVDEV_TO_HID_MAPPING.get(ecode, None)
    logger.debug(f"Converted ecode {ecode} to HID keycode {hid_key}")
    if hid_key is None:
        logger.warning(f"Unsupported key pressed: {ecode}")
    return hid_key
