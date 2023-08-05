#!/usr/bin/env python

from msvcrt import getwch  # type: ignore

__all__ = ["get_char"]

NULL = "\0"
WIN_ESC = "\xe0"
KEYS_MAPPING = {
    "H": "up",
    "P": "down",
    "M": "right",
    "K": "left",
    "R": "insert",
    "S": "del",
    "I": "pgup",
    "Q": "pgdn",
}


def get_char() -> str:
    ch: str = getwch()
    if ch == WIN_ESC:
        ch = getwch()
        return KEYS_MAPPING.get(ch, NULL)
    return ch
