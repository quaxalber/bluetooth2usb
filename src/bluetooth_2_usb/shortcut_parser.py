import re
from typing import Dict
from adafruit_hid.keycode import Keycode

class ParsedShortcut:
    """
    Pair of shortcut (keycode combination) and formatted shortcut description.
    """

    def __init__(self, keycodes: list[int], description: str):
        self._keycodes = keycodes
        self._description = description

    @property
    def keycodes(self) -> list[int]:
        return self._keycodes

    @property
    def description(self) -> str:
        return self._description

    @property
    def is_empty(self) -> bool:
        return len(self._keycodes) == 0

    def __str__(self) -> str:
        return self._description

    def __repr__(self) -> str:
        return self._description


class ShortcutParser:
    """
    Performs shortcut parsing.
    """

    # Preferred key names to be used on shortcut formatting
    # Also used on shortcut parsing
    _preferred_keycode_names: dict[int, str] = {
        Keycode.ONE: "1",
        Keycode.TWO: "2",
        Keycode.THREE: "3",
        Keycode.FOUR: "4",
        Keycode.FIVE: "5",
        Keycode.SIX: "6",
        Keycode.SEVEN: "7",
        Keycode.EIGHT: "8",
        Keycode.NINE: "9",
        Keycode.ZERO: "0",
        Keycode.ESCAPE: "ESC",
        Keycode.EQUALS: "=",
        Keycode.LEFT_BRACKET: "[",
        Keycode.RIGHT_BRACKET: "]",
        Keycode.BACKSLASH: "\\",
        Keycode.QUOTE: "'",
        Keycode.GRAVE_ACCENT: "`",
        Keycode.PERIOD: ".",
        Keycode.FORWARD_SLASH: "/",
        Keycode.PRINT_SCREEN: "PRTSCR",
        Keycode.PAUSE : "BREAK",
        Keycode.INSERT: "INS",
        Keycode.PAGE_UP: "PGUP",
        Keycode.DELETE: "DEL",
        Keycode.PAGE_DOWN: "PGDOWN",
        Keycode.RIGHT_ARROW: "RIGHT",
        Keycode.LEFT_ARROW: "LEFT",
        Keycode.DOWN_ARROW: "DOWN",
        Keycode.UP_ARROW: "UP",
        Keycode.APPLICATION: "APP",
        Keycode.CONTROL: "CTRL",
        Keycode.SHIFT: "SHIFT",
        Keycode.ALT: "ALT",
        Keycode.GUI: "WIN"
    }

    # Additional key names used on shortcut parsing
    _additional_keycode_aliases: dict[str, int] = {
        "EQUAL": Keycode.EQUALS,
        "BACK": Keycode.BACKSPACE,
        "LEFTBRACE": Keycode.LEFT_BRACKET,
        "RIGHTBRACE": Keycode.RIGHT_BRACKET,
        "LBRACE": Keycode.LEFT_BRACKET,
        "RBRACE": Keycode.RIGHT_BRACKET,
        "GRAVE": Keycode.GRAVE_ACCENT,
        "SLASH": Keycode.FORWARD_SLASH,
        "CAPSLOCK": Keycode.CAPS_LOCK,
        "CAPITAL": Keycode.CAPS_LOCK,
        "SCROLLLOCK": Keycode.SCROLL_LOCK,
        "PAGEUP": Keycode.PAGE_UP,
        "PAGEDOWN": Keycode.PAGE_DOWN,
        "COMPOSE": Keycode.APPLICATION,
        "LCTRL": Keycode.LEFT_CONTROL,
        "RCTRL": Keycode.RIGHT_CONTROL,
        "LSHIFT": Keycode.LEFT_SHIFT,
        "RSHIFT": Keycode.RIGHT_SHIFT,
        "LALT": Keycode.LEFT_ALT,
        "RALT": Keycode.RIGHT_ALT,
        "LWIN": Keycode.LEFT_GUI,
        "RWIN": Keycode.RIGHT_GUI,
        "META": Keycode.GUI,
        "LMETA": Keycode.LEFT_GUI,
        "RMETA": Keycode.RIGHT_GUI,
    }

    # Used to split shortcut_command to individual shortcuts
    _command_split_regex = re.compile(r'[,;\s]+')

    # Used to split shortcut to series of keycodes
    _shortcut_split_regex = re.compile(r'[-+]+')

    def __init__(self) -> None:
        # Used to map key name to Keycode
        self._key_codes: Dict = dict[str, int]()
        # Used to map Keycode to key name
        self._key_names: Dict = dict[int, str]()
        # fill mappings from adafruit_hid.keycode.Keycode
        for field in dir(Keycode):
            if not field.startswith("__"):
                field_value = getattr(Keycode, field)
                if isinstance(field_value, int):
                    self._key_codes[field] = field_value
                    self._key_names[field_value] = field
        # add key aliases
        for alias in self._additional_keycode_aliases:
            keycode = self._additional_keycode_aliases[alias]
            self._key_codes[alias] = keycode
        # add preferred key names
        for keycode in self._preferred_keycode_names:
            keycode_name = self._preferred_keycode_names[keycode]
            self._key_codes[keycode_name] = keycode
            self._key_names[keycode] = keycode_name

    # Accepts a command (string representation of multiple schortcuts) and returns a list of schortcuts for it
    # Raises an ValueError if raise_error is on and command cannot be parsed
    def parse_command(self, shortcut_command: str, raise_error: bool = True) -> list[ParsedShortcut]:
        """
        Parses a command (a series of shortcuts splitted by whitespace, ',' or ';' separators).

        A shortcut is combination of one or more keycodes splitted by '-' or '+' separators.
        Keycodes are case-insensitive and accepts values from adafruit_hid.keycode.Keycode enum
        as well as Windows Virtual-Key Codes names (https://learn.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes, 'VK_' prefix should be removed)

        Ignores invalid keycodes if raise_error arg is set to False (default: True).

        Examples
        --------
        >>> parser.parse_command('Ctrl-A Del')
        ["Ctrl-A", "Del"]

        >>> parser.parse_command('CCtrl-A, Del, Alt+Tab', raise_error: False)
        ["Del", "Alt-Tab"]
        """

        shortcuts = []
        for shortcut_candidate in self._command_split_regex.split(shortcut_command):
            try:
                shortcut = self.parse_shortcut(shortcut_candidate, raise_error)
                if shortcut:
                    shortcuts.append(shortcut)
            except ValueError as ex:
                    raise ValueError(f"Cannot parse command {shortcut_command}: {ex.args[0]}")
        return shortcuts

    # Parses shortcut. On failure returns None or raises an ValueError depending on raise_error
    def parse_shortcut(self, shortcut: str, raise_error: bool = True) -> ParsedShortcut | None:
        """
        Parses a shortcut (a combination of one or more keycodes splitted by '-' or '+' separators).

        A shortcut is combination of one or more keycodes splitted by '-' or '+' separators.
        Keycodes are case-insensitive and accepts values from adafruit_hid.keycode.Keycode enum
        as well as Windows Virtual-Key Codes names (https://learn.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes, 'VK_' prefix should be trimmed)

        Ignores invalid keycodes if raise_error arg is set to False (default: True).

        Examples
        --------
        >>> parser.parse_shortcut('Ctrl-A')
        ParsedShortcut:
            keycodes: [Keycode.CONTROL, Keycode.A]
            description: "Ctrl-A"

        >>> parser.parse_shortcut('Ctrl-AA')
        None
        """

        keycodes = []
        keynames = []
        for key_candidate in map(str.upper, self._shortcut_split_regex.split(shortcut)):
            if key_candidate in self._key_codes:
                keycode = self._key_codes[key_candidate]
                keycodes.append(keycode)

                keyname = self._key_names[keycode]
                keynames.append(keyname.capitalize())
            elif raise_error:
                raise ValueError(f"Unknown key {key_candidate} in shortcut {shortcut}")
            else:
                return None
        if not keycodes:
            return None
        return ParsedShortcut(keycodes, "-".join(keynames))