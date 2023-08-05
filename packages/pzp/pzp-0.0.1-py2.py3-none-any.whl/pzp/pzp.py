#!/usr/bin/env python

import os
import sys
import itertools
from enum import Enum
from typing import Any, Callable, List, Optional, Sequence, TextIO, Union

try:
    import termios
    import tty
except ImportError:
    termios = None
    tty = None
try:
    from msvcrt import getwch
except ImportError:
    getwch = None


__all__ = [ "pzp" ]


NULL = "\0"
UP = "↑"
DOWN = "↓"
RIGHT = "→"
LEFT = "←"
NL = "\n"
CR = "\r"
BS = "\x7f"
ESC = "\u001b"
CTRL_C = "\x03"
CTRL_E = "\x05"
CTRL_G = "\x07"
CTRL_H = "\x08"
CTRL_J = "\x0a"
CTRL_K = "\x0b"
CTRL_P = "\x10"
CTRL_Q = "\x11"
CTRL_N = "\x0e"
SPACE = " "
CURSOR_SAVE_POS = f"{ESC}7"
CURSOR_RESTORE_POS = f"{ESC}8"
ERASE_LINE = f"{ESC}[2K"
RED = f"{ESC}[31m"
GREEN = f"{ESC}[32m"
YELLOW = f"{ESC}[33m"
BLUE = f"{ESC}[34m"
PURPLE = f"{ESC}[35m"
CYAN = f"{ESC}[36m"
WHITE = f"{ESC}[37m"
NORMAL = f"{ESC}[0m"
BOLD = f"{ESC}[1m"
NEGATIVE = f"{ESC}[7m"

DEFAULT_MARGIN = 3

def get_char():
    if getwch is not None:
        return getwch()
    try:
        fd = sys.stdin.fileno()
        attrs = termios.tcgetattr(fd)
        tty.setraw(fd)
        ch = sys.stdin.read(1)
        if termios is not None:
            if ch == ESC:
                ch = sys.stdin.read(1)
                if ch == "[":
                    ch = sys.stdin.read(1)
                    if ch == '\x41':
                        ch = UP
                    elif ch == '\x42':
                        ch = DOWN
                    elif ch == '\x43':
                        ch = RIGHT
                    elif ch == '\x44':
                        ch = LEFT
                    else:
                        ch = NULL
        return ch
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, attrs)


class Done(Exception):
    pass

class Cancel(Exception):
    pass


class Layout(Enum):
    REVERSE_LIST="reverse-list"

class Screen:
    def __init__(self, stream: TextIO = sys.stdout):
        self.stream = stream
        self.data: List[str] = [];

    def write(self, line: str) -> None:
        "Add data to be written on the stream"
        self.data.append(line)

    def flush(self) -> None:
        "Write data to the stream and flush it"
        self.stream.write("".join(self.data))
        self.data = [];
        self.stream.flush()

    def init(self):
        "Save cursor position"
        self.write(f"{CURSOR_SAVE_POS}")
        self.flush()

    def cleanup(self):
        "Clean screen and restore cursor position"
        self.write(f"{CURSOR_RESTORE_POS}{ERASE_LINE}{CURSOR_SAVE_POS}")
        self.flush()

    def erase_lines(self, lines: int):
        "Erase n lines"
        self.move_up(lines)
        # self.write(f"{ERASE_LINE}{CURSOR_RESTORE_POS}")
        # self.write(f"{CURSOR_RESTORE_POS}")
        self.write(f"{ERASE_LINE}{NL}" * lines)
        self.move_up(lines)
        # self.write(f"{CURSOR_RESTORE_POS}")

    def move_up(self, lines: int):
        self.write(f"{ESC}[{lines}A")

class PZP:

    def __init__(self, items: Union[Callable, Sequence[Any]], max_lines: Optional[int] = None, margin: int = DEFAULT_MARGIN, accessor_fn=lambda x: x, format_fn=lambda x: str(x), layout=Layout.REVERSE_LIST):
        if max_lines is None:
            self.max_lines = os.get_terminal_size().lines - margin
        else:
            self.max_lines = max_lines
        if callable(items):
            self.get_items_fn = items
            self.filtered_items = self.items = self.get_items_fn()
        else:
            self.get_items_fn = None
            self.filtered_items = self.items = items
        self.accessor_fn = accessor_fn
        self.format_fn = format_fn
        self.screen = Screen()
        self.layout = layout

    def pzp(self):
        self.line = ""
        self.selected = 0
        self.display_items = 0
        self.screen.init()
        self.update_screen()
        try:
            while True:
                self.process_key(get_char())
                self.filtered_items = list(filter(self.match, self.items))
                self.selected = max(min(self.selected, len(self.filtered_items) - 1), 0)
                self.update_screen()
                self.screen.erase_lines(self.printed_items_num)
                self.display_items = [self.accessor_fn(x) for x in itertools.islice(self.filtered_items, None, self.max_lines)]
                self.print_items()
                self.print_empty_lines()
                self.print_counter()
                self.print_prompt()
                self.screen.flush()
        except Done:
            return self.prepare_result()
        except Cancel:
            return None
        finally:
            self.screen.cleanup()

    @property
    def printed_items_num(self):
        return len(self.display_items) if self.display_items else 0

    def process_key(self, ch: str) -> None:
        "Process the pressed key"
        if ch == CR:  # Done
            raise Done
        elif ch in (ESC, CTRL_C, CTRL_G, CTRL_Q):  # Cancel
            self.cancel = True
            raise Cancel
        elif ch in (DOWN, CTRL_J, CTRL_N):  # Move one line down
            self.selected = self.selected + 1
        elif ch in (UP, CTRL_K, CTRL_P):  # Mode one line up
            self.selected = self.selected - 1
        elif ch in (BS, CTRL_H):  # Delete one characted
            if self.line:
                self.line = self.line[:-1]
        elif ch in (NULL, LEFT, RIGHT):  # Skip
            pass
        elif ch >= SPACE:  # Append the character to line
            self.line = self.line + ch

    def update_screen(self) -> None:
        "Update the screen - erase the old items, print the filtered items and the prompt"
        self.screen.erase_lines(self.printed_items_num)
        self.display_items = [self.accessor_fn(x) for x in itertools.islice(self.filtered_items, None, self.max_lines)]
        if self.layout == Layout.REVERSE_LIST:
            self.print_items()
            self.print_empty_lines()
            self.print_counter()
            self.print_prompt()
        self.screen.flush()

    def print_items(self) -> None:
        for i, item in enumerate(self.display_items):
            if i == self.selected:
                self.screen.write(f"{ERASE_LINE}{RED}{BOLD}>{NORMAL} {BOLD}{self.format_fn(item)}{NORMAL}{NL}")
            else:
                self.screen.write(f"{ERASE_LINE}  {self.format_fn(item)}{NL}")

    def print_empty_lines(self) -> None:
        self.screen.write(f"{NL}" * (min(len(self.items), self.max_lines - self.printed_items_num)))

    def print_counter(self) -> None:
        self.screen.write(f"  {ERASE_LINE}{YELLOW}{len(self.filtered_items)}/{len(self.items)}{NORMAL}{NL}")

    def print_prompt(self) -> None:
        self.screen.write(f"{ERASE_LINE}> {self.line}")

    def match(self, item: Any) -> bool:
        return self.line.lower() in self.accessor_fn(item).lower()

    def prepare_result(self) -> Any:
        "Output the selected item, if any"
        try:
            return self.filtered_items[self.selected]
        except IndexError:
            return None

def accessor(item):
    return f"{item.rowid:2d}) {item}"


def match(item: Any, pattern: str, accessor_fn) -> bool:
    return pattern.lower() in accessor_fn(item).lower()


def pzp(items: Union[Callable, Sequence[Any]],
        max_lines: Optional[int] = None,
        accessor_fn=lambda x: x,
        format_fn=lambda x: str(x),
        layout: Layout = Layout.REVERSE_LIST):
    pzp = PZP(
        items=items,
        max_lines=max_lines,
        accessor_fn=accessor_fn,
        format_fn=format_fn,
        layout=layout,
    )
    return pzp.pzp()
