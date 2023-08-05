from abc import ABC, abstractmethod
from pathlib import Path
from time import struct_time
from typing import Any

from .utils import color, fill, horizontal_line


class Formatter(ABC):
    """
    Abstract base class for formatters. Formatters
    are used to retrieve information via the prompt
    and format it into a readable string.
    """
    @staticmethod
    @abstractmethod
    def adjust_number(_: int) -> str:
        """
        Used by :func:`prompts.amount`. This displays
        the current number and hints that the number may
        by increased or decreased.
        """
    
    @staticmethod
    @abstractmethod
    def ask(_: str) -> str:
        """
        Used by :func:`prompt`. This displays the
        message/question passed into :func:`prompt`.
        """
    
    @staticmethod
    @abstractmethod
    def check(_: str) -> str:
        ...
    
    @staticmethod
    @abstractmethod
    def confirm(_: bool) -> str:
        ...
    
    @staticmethod
    @abstractmethod
    def datetime(_: struct_time) -> str:
        ...
    
    @staticmethod
    @abstractmethod
    def final(_: Any) -> str:
        """
        Used by all provides prompts. This displays
        the result shortly.
        """
    
    @staticmethod
    @abstractmethod
    def grab(_: str) -> str:
        """
        Used by :func:`prompts.sort`. This displays
        an option that can be moved around.
        """
    
    @staticmethod
    @abstractmethod
    def option(_: str) -> str:
        ...
    
    @staticmethod
    @abstractmethod
    def path(_: Path) -> str:
        """
        Used by :func:`prompts.path`. This displays
        a file, directory, etc. Different symbols
        may be used for different path types.
        """
    
    @staticmethod
    @abstractmethod
    def prompt(_: str) -> str:
        ...
    
    @staticmethod
    @abstractmethod
    def select(_: str) -> str:
        ...
    
    @staticmethod
    @abstractmethod
    def selected_files(_: list[Path]) -> str:
        ...
    
    @staticmethod
    @abstractmethod
    def uncheck(_: str) -> str:
        ...
    
    @staticmethod
    @abstractmethod
    def unselect(_: str) -> str:
        ...


class ColoredFormatter(Formatter):
    @staticmethod
    def adjust_number(value: int) -> str:
        return f"+ {value:>3} -\n"
    
    @staticmethod
    def ask(value: str) -> str:
        return fill(
            value,
            prepend = color("? ", "green"),
        ) + "\n"
    
    @staticmethod
    def check(value: str) -> str:
        return fill(
            value,
            prepend = color("\N{CHECK MARK} ", "green")
        ) + "\n"
    
    @staticmethod
    def confirm(value: bool) -> str:
        y, n = ("Y", "n") if value else ("y", "N")
        return f": [{y}/{n}]\n"
    
    @staticmethod
    def datetime(value: struct_time) -> str:
        ...
    
    @staticmethod
    def final(value: Any) -> str:
        if isinstance(value, list):
            if all(isinstance(i, Path) for i in value):
                value = "\n".join(map(str, value))
            
            else:
                value = ", ".join(map(str, value))
        
        return fill(
            value,
            prepend = color("~ ", "yellow")
        ) + "\n"
    
    @staticmethod
    def grab(value: str) -> str:
        return fill(
            value,
            prepend = color("> ", "yellow")
        ) + "\n"
    
    @staticmethod
    def option(value: str) -> str:
        return f"  {value}"
    
    @staticmethod
    def path(value: Path) -> str:
        if value.is_dir():
            pre = "\N{FILE FOLDER} "
        
        elif value.is_symlink():
            pre = "\N{LINK SYMBOL} "
        
        elif value.is_file():
            pre = "\N{PAGE FACING UP} "
        
        else:
            pre = f"  "
        
        return fill(
            value.name,
            prepend = pre
        )
    
    @staticmethod
    def prompt(value: str) -> str:
        return fill(
            value,
            prepend = color(": ", "yellow"),
        ) + "\n"
    
    @staticmethod
    def select(value: str) -> str:
        return f"{color(value, 'yellow')}\n"
    
    @staticmethod
    def selected_files(value: list[Path]) -> str:
        if not value:
            return ""
        
        return "".join(fill(file, prepend = "- ") + "\n" for file in value)
    
    @staticmethod
    def uncheck(value: str) -> str:
        return fill(
            value,
            prepend = color("\N{MULTIPLICATION SIGN} ", "red")
        ) + "\n"
    
    @staticmethod
    def unselect(value: str) -> str:
        return f"{value}\n"


#class BasicFormatter(Formatter):
#    ...


#class EmojiFormatter(Formatter):
#    ...

