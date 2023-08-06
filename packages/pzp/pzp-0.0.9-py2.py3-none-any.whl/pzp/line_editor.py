#!/usr/bin/env python

from inspect import getmembers
from typing import Optional, TYPE_CHECKING
from .ansi import SPACE
from .actions import Action, ActionsHandler
from .keys import KeyEvent

if TYPE_CHECKING:
    from .screen import Screen

__all__ = ["LineEditor"]


class LineEditor(ActionsHandler):
    def __init__(self, line: Optional[str] = None) -> None:
        """
        Line editor

        Args:
            line: Initial value
        """
        super().__init__()
        self.line = line or ""
        self.cursor_pos: int = len(self.line)

    def set_cursor_pos(self, cursor_pos: int) -> None:
        "Set cursor position (absolute)"
        self.cursor_pos = max(min(cursor_pos, len(self.line)), 0)

    def adj_cursor_pos(self, characters: int) -> None:
        "Set cursor position (relative to current position)"
        self.cursor_pos = max(min(self.cursor_pos + characters, len(self.line)), 0)

    def insert(self, ch: str) -> None:
        "Insert characters at the current cursor position"
        if ch >= SPACE:  # Add the character to line
            self.line = self.line[0 : self.cursor_pos] + ch + self.line[self.cursor_pos :]
            self.adj_cursor_pos(len(ch))

    @Action("backward-char")
    def backward_char(self) -> None:
        "Move the cursor back one character"
        self.set_cursor_pos(self.cursor_pos - 1)

    @Action("forward-char")
    def forward_char(self) -> None:
        "Move the cursor forward one character"
        self.set_cursor_pos(self.cursor_pos + 1)

    @Action("beginning-of-line")
    def beginning_of_line(self) -> None:
        "Move the cursor to the line start"
        self.set_cursor_pos(0)

    @Action("end-of-line")
    def end_of_line(self) -> None:
        "Move the cursor to the line end"
        self.set_cursor_pos(len(self))

    @Action("backward-delete-char")
    def delete_backward_char(self) -> None:
        "Delete the previous character"
        if self.cursor_pos > 0:
            self.line = self.line[: self.cursor_pos - 1] + self.line[self.cursor_pos :]
        self.adj_cursor_pos(-1)

    @Action("delete-char")
    def delete_char(self) -> None:
        "Delete the current character"
        self.line = self.line[: self.cursor_pos] + self.line[self.cursor_pos + 1 :]
        self.adj_cursor_pos(0)

    @Action("default")
    def default(self, key_event: KeyEvent) -> None:
        self.insert(key_event.ch)

    def print(self, screen: "Screen") -> None:
        """
        Print the line and set the cursor position

        Args:
            screen: Screen instance
        """
        screen.write(self.line).move_left(len(self) - self.cursor_pos)

    def __len__(self) -> int:
        "Return line length"
        return len(self.line)

    def __str__(self) -> str:
        "Return the line"
        return self.line
