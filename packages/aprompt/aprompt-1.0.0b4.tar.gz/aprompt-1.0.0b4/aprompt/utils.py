from __future__ import annotations

from collections.abc import Collection, Mapping
import io
import os
import re
import sys
from typing import (
    Any,
    Optional,
    TextIO,
    Union,
)

from adorable import Color3bit


ANSIRE = re.compile("\x1b\\[.*?[ABCDEFGHJKfnsumlh]")
_file = sys.stdout

def set_stream(file: TextIO) -> None:
    r"""
    Redirects any prompt output to provided
    file.
    """
    global _file
    if not isinstance(file, io.TextIOBase):
        raise ValueError("provided `file` is no text file like object")
    
    _file = file

def ansilen(string: str) -> int:
    return len(ANSIRE.sub("", string))

def hide_string(string: str, char: str = "*") -> str:
    return char * len(string)

def fill(
    text: Any,
    /, *,
    width: Optional[int] = None,
    height: Optional[int] = None,
    prepend: str = "",
) -> str:
    """
    Parameters
    ----------
    text
    
    width
        The maximum length a line can be. Defaults to
        terminal width or 80.
    
    prepend
        String to prepend first line with. All other lines
        will be indented by the length of this.
        Cannot be longer than ``width``.
    """
    string = str(text)
    
    if width is None:
        width = twidth()
    
    if ansilen(prepend) >= width:
        raise ValueError(f"{ansilen(prepend) >= width = }")
    
    lines: list[str] = []
    line = prepend
    for char in string:
        if height and len(lines) == height:
            break
        
        if char == "\n":
            lines.append(line)
            line = " " * ansilen(prepend)
            continue
        
        line += char
        
        if ansilen(line) > width:
            lines.append(line[:-1])
            line = " " * ansilen(prepend)
    
    if not line.isspace():
        lines.append(line)
    
    return "\n".join(lines)

def get_terminal_size() -> os.terminal_size:
    try:
        return os.get_terminal_size(_file.fileno())
    except OSError:
        return os.terminal_size((80, 24))

def twidth() -> int:
    return get_terminal_size().columns

def theight() -> int:
    return get_terminal_size().lines

def swap(l: list[Any], a: int, b: int) -> None:
    l[a], l[b] = l[b], l[a]

def insert(string: str, substring: str, index: int) -> str:
    return string[:index] + substring + string[:index]

def cut(string: str, start: int, lines: int) -> str:
    return "\n".join(string.splitlines()[start:start+lines])

def color(text: str, c: str) -> str:
    return Color3bit.from_name(c).fg(text)

def horizontal_line() -> str:
    return "\N{EM DASH}" * twidth()

def clear_lines(amount: int) -> str:
    return "\x1b[1A\x1b[2K\r" * amount

class Pointer:
    def __init__(self, options: str | list[Any] | tuple[Any, ...]):
        self._options = options
        self._max_idx = len(options) - 1
        self.point = 0
    
    def get(self) -> Any:
        return self._options[self.point]
    
    def down(self) -> int:
        if self.point == self._max_idx:
            self.point = 0
            return self.point
        
        self.point += 1
        return self.point
    
    def up(self) -> int:
        if self.point == 0:
            self.point = self._max_idx
            return self.point
        
        self.point -= 1
        return self.point

class Display:
    def __init__(self, navigation: Mapping[str, Union[str, list[str]]] = {}):
        nav = {"quit": "Ctrl-C"} | navigation
        self.navstr = "Navigation\n"
        
        for action, keys in nav.items():
            if isinstance(keys, str):
                keys = keys.split()
           
            self.navstr += f"  {action}    {'  '.join(keys)}\n"
        
        self.navstr = f"{horizontal_line()}\n{self.navstr}"
        self.rows = 0
        self.ring = False
    
    def __call__(
        self,
        *messages: str,
        seperate: bool = False,
        scroll: int = 0,
    ) -> str:
        if len(self.navstr.splitlines()) > theight():
            raise RuntimeError("terminal height too small")
        
        body = fill(
            ("\n" if seperate else "").join(messages),
            width = twidth()
        )
        footer_lines = theight() - len(self.navstr.splitlines()) - 1
        
        #print(f"{len(body.splitlines()) = }, {footer_lines = }")
        
        text = "".join([
            self.clear() + ("\a" if self.ring else ""),
            (cut(
                body,
                start = scroll,
                lines = footer_lines
            ) + "\n") if len(body.splitlines()) > footer_lines else body,
            self.navstr
        ])
        
        self.rows = text.count("\n")
        self.ring = False
        
        return text
    
    def clear(self) -> str:
        return clear_lines(self.rows)
    
    def alert(self) -> None:
        self.ring = True
    
