#!/usr/bin/env python

import sys

__all__ = ["get_char"]

import termios
import tty

NULL = "\0"
ESC = "\u001b"


def get_char() -> str:
    try:
        fd = sys.stdin.fileno()
        attrs = termios.tcgetattr(fd)
        tty.setraw(fd)
        ch = sys.stdin.read(1)
        if ch == ESC:
            ch = sys.stdin.read(1)
            if ch == "[":
                ch = sys.stdin.read(1)
                if ch == "A":
                    ch = "up"
                elif ch == "B":
                    ch = "down"
                elif ch == "C":
                    ch = "right"
                elif ch == "D":
                    ch = "left"
                elif ch == "2":
                    ch = "insert"
                    sys.stdin.read(1)  # skip ~
                elif ch == "3":
                    ch = "del"
                    sys.stdin.read(1)  # skip ~
                elif ch == "5":
                    ch = "pgup"
                    sys.stdin.read(1)  # skip ~
                elif ch == "6":
                    ch = "pgdn"
                    sys.stdin.read(1)  # skip ~
                else:
                    ch = NULL
        return ch
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, attrs)
