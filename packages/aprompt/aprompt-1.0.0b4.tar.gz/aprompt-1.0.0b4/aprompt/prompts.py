from __future__ import annotations

from collections.abc import Generator, Iterable
import datetime as dtlib
from pathlib import Path
import string
from time import struct_time
from typing import (
    Any,
    Callable,
    Optional,
    TypeVar,
    Union,
)
import warnings

import adorable
from readchar import key as Key

from .formatters import Formatter
from .utils import Display, hide_string, Pointer, swap


# type defs

T = TypeVar("T")
PromptType = Generator[str, str, tuple[T, str]]
DatetimeType = Union[
    dtlib.datetime,
    dtlib.date,
    dtlib.time
]
DatetimeTypeVar = TypeVar("DatetimeTypeVar", bound = DatetimeType)


# symbol defs

SYM_ARROW_UP = "\N{UPWARDS ARROW}"
SYM_ARROW_DOWN = "\N{DOWNWARDS ARROW}"
SYM_ARROW_LEFT = "\N{LEFTWARDS ARROW}"
SYM_ARROW_RIGHT = "\N{RIGHTWARDS ARROW}"

SYM_ENTER = "\N{RETURN SYMBOL}"
SYM_BACKSPACE = "\N{ERASE TO THE LEFT}"
SYM_SPACE = "Space"


# other defs

SPACE = " \t"


# prompt defs

def text(
    *,
    hide: bool = False,
    double_enter: bool = False,
    allow_any: bool = False,
) -> PromptType[str]:
    r"""
    Parameters
    ----------
    hide
        Whether all characters should be replaced
        by asterisks when displaying.
    
    double_enter
        .. versionadded:: 1.0.0b3
        
        Reads enter as newline. When enter is hit
        twice in a row, it is interpreted as done.
        Trailing newlines will be removed.
    
    allow_any
        If set to ``False``, only alphanumeric,
        punctuation and spaces are allowed to type.
    
    Returns
    -------
    str
        The entered text.
    
    """
    formatter: Formatter = yield None # type: ignore
    display = Display()
    
    text = ""
    enter_count = 0
    
    while True:
        key = yield display(formatter.prompt(
            hide_string(text) if hide else text
        ))
        
        if key == Key.ENTER:
            enter_count += 1
            
            if double_enter and enter_count != 2:
                text += "\n"
            
            else:
                return (
                    text,
                    display.clear() + formatter.final(hide_string(text) if hide else text)
                )
        
        elif key == Key.BACKSPACE:
            if text:
                text = text[:-1]
            
            else:
                display.alert()
        
        elif key == Key.LEFT:
            display.alert()
        
        elif key == Key.RIGHT:
            display.alert()
        
        elif key in [Key.UP, Key.DOWN, Key.PAGE_UP, Key.PAGE_DOWN]:
            # PGUP and PGDN do not give feedback but
            # atleast it does not scroll
            display.alert()
        
        elif allow_any:
            if (
                key.isalnum()
                or key in string.punctuation
                or key in SPACE
            ):
                text += key
            
            else:
                display.alert()
        
        else:
            text += key
        
        if key != Key.ENTER:
            enter_count = 0

def code(
    *,
    length: int,
    hide: bool = False,
    chars: Iterable[str] = string.ascii_letters + string.digits,
    char_missing: str = "_",
    require_enter: bool = False,
) -> PromptType[str]:
    """
    .. versionadded:: 1.0.0b2
    
    Parameters
    ----------
    length
        The exact length of the code.
    
    hide
        Whether all characters should be replaced
        by asterisks when displaying.
    
    chars
        Allowed characters.
    
    char_missing
        A character that signals a missing character.
        By default this is ``_`` but if ``chars``
        contains that, this parameter should be changed.
        Otherwise a warning will be raised.
    
    require_enter
        Whether the enter key must be pressed to enter
        or the code will be entered as soon as the last
        character is pressed.
    
    Returns
    -------
    str
        The entered code.
    """
    formatter: Formatter = yield None # type: ignore
    display = Display()
    
    if char_missing in chars:
        warnings.warn("`chars` contains `char_missing`", RuntimeWarning)
    
    code = ""
    
    while True:
        key = yield display(formatter.prompt(
            (hide_string(code) if hide else code).ljust(length, char_missing)
        ))
        
        if key == Key.ENTER and require_enter and len(code) == length:
            return (
                code,
                display.clear() + formatter.final(hide_string(code) if hide else code)
            )
        
        elif key == Key.BACKSPACE:
            if code:
                code = code[:-1]
            
            else:
                display.alert()
        
        elif key in [Key.UP, Key.DOWN, Key.PAGE_UP, Key.PAGE_DOWN]:
            # PGUP and PGDN do not give feedback but
            # atleast it does not scroll
            display.alert()
        
        elif key in chars and len(code) != length:
            code += key
            
            if not require_enter and len(code) == length:
                return (
                    code,
                    display.clear() + formatter.final(hide_string(code) if hide else code)
                )
        
        else:
            display.alert()

#def datetime(
#    t: DateimeTypeVar,
#    /, *,
#    minimum: Optional[DatetimeType] = None,
#    maximum: Optional[DatetimeType] = None,
#) -> PromptType[DateimeTypeVar]:
#    r"""
#    .. versionadded:: 1.0.0b3
#    
#    Prompt for datetime. This prompt takes leap years,
#    amount of days for each month into account and
#    therefore allows any datetime that exists.
#    
#    Parameters
#    ----------
#    t
#        A ``datetime.datetime``, ``datetime.dat`` or
#        ``datetime.time`` object representing the default
#        datetime and values that can be modified.
#    
#    minimum
#        The minimum datetime that can be used.
#    
#    maximum
#        The minimum datetime that can be used.
#    
#    Returns
#    -------
#    Return entered datetime. Type is the same as provides for ``t``.
#    """
#    formatter: Formatter = yield None # type: ignore
#    display = Display(navigation = {
#        "enter": SYM_ENTER,
#        "increase": SYM_ARROW_UP,
#        "decrease": SYM_ARROW_DOWN,
#        "left": SYM_ARROW_LEFT,
#        "right": SYM_ARROW_RIGHT,
#    })
#    
#    if isinstance(t, dtlib.date):
#        sections = t.timetuple()
#    
#    else:
#        sections = struct_time(
#            -1, -1, -1,
#            t.hour, t.minute, t.second,
#        )
#    
#    while True:
#        key = yield display(
#            formatter.datetime(sections)
#        )
#        
#        if key == Key.ENTER:
#            return (
#                t.__class__(i for i in sections if i != -1),
#                formatter.final(t)
#            )

def sort(
    *options: str,
    sort: bool = False,
) -> PromptType[list[str]]:
    r"""
    Parameters
    ----------
    options
        Options to choose from.
    
    sort
        Sort options by built-in ``sorted`` function.
    
    Returns
    -------
    list[str]
        Provides options, but resorted.
    """
    formatter: Formatter = yield None # type: ignore
    display = Display(navigation = {
        "enter": SYM_ENTER,
        "select/unselect": SYM_SPACE,
        "move up": SYM_ARROW_UP,
        "move down": SYM_ARROW_DOWN,
    })
    
    if not all(options):
        raise ValueError("option cannot be empty string")
    
    optionlist: list[str] = list(options)
    
    if sort:
        optionlist = sorted(optionlist)
    
    #else:
    #    optionlist = optionlist.copy()
    
    pointer = Pointer(optionlist)
    scroll = 0
    grab_mode = False
    
    while True:
        text = []
        for idx, option in enumerate(optionlist):
            if idx == pointer.point:
                if grab_mode:
                    text.append(formatter.grab(option))
                
                else:
                    text.append(formatter.select(formatter.option(option)))
            
            else:
                text.append(formatter.unselect(formatter.option(option)))
        
        key = yield display(
            *text,
            scroll = scroll
        )
        
        if key == Key.ENTER:
            opts = [i for i in optionlist]
            
            return (
                opts,
                display.clear() + formatter.final(opts)
            )
        
        elif key == Key.SPACE:
            grab_mode = not grab_mode
        
        elif key == Key.UP:
            if grab_mode:
                swap(optionlist, pointer.point, pointer.up())
            
            else:
                scroll = pointer.up()
        
        elif key == Key.DOWN:
            if grab_mode:
                swap(optionlist, pointer.point, pointer.down())
            
            else:
                scroll = pointer.down()
        
        else:
            display.alert()

def select(
    *options: str,
    multiple: bool = False,
    sort: bool = False,
    require: Union[Iterable[int], Callable[[int], bool], int, None] = None,
) -> PromptType[Union[list[str], str]]:
    r"""
    Parameters
    ----------
    options
        Options to choose from.
    
    multiple
        Whether only one or multple options can
        be selected.
    
    sort
        Sort options by built-in ``sorted`` function.
    
    require
        ``int`` or iterable of ``int``\s indicating the amount of
        options that can be selected. Setting this parameter
        requires enabling ``multiple``.
        This may also be a callable taking one argument
        (the amount of selected options) that returns either
        ``True`` to continue or ``False`` to signal, that the
        amount is invalid. This would be equal to specifying
        the `repeat_while` parameter in the main prompt function
        with the difference that it does not reset the selected
        options.
    
    Returns
    -------
    list[str]
        Selected options if ``multiple`` is enabled.
    
    str
        Selected option if ``multiple`` is disabled.
    """
    formatter: Formatter = yield None # type: ignore
    display = Display(navigation = {
        "enter": SYM_ENTER,
        **({"select/unselect": SYM_SPACE} if multiple else {}),
        "move up": SYM_ARROW_UP,
        "move down": SYM_ARROW_DOWN,
    })
    
    if require is not None and not multiple:
        raise ValueError("`require` is set but `mutiple` is not enabled")
    
    if not all(isinstance(i, str) and i for i in options):
        raise ValueError("option has to be non-empty string")
    
    if sort:
        options = tuple(sorted(options))
    
    pointer = Pointer(options)
    selected: list[int] = []
    scroll = 0
    
    while True:
        text: list[str] = []
        for idx, option in enumerate(options):
            apply: Callable[[Any], str] = lambda x: str(x)
            
            if idx in selected:
                apply = formatter.check
            
            elif multiple:
                apply = formatter.uncheck
            
            if idx == pointer.point:
                opt = formatter.select(option)
            
            else:
                opt = formatter.unselect(option)
            
            text.append(apply(opt))
        
        key = yield display(
            *text,
            scroll = scroll
        )
        
        if key == Key.ENTER:
            if multiple:
                chose = [options[i] for i in selected]
                
                if require is not None:
                    success = False
                    
                    if callable(require):
                        if require(len(chose)):
                            success = True
                    
                    elif isinstance(require, int):
                        success = len(chose) == require
                    
                    elif len(chose) in require:
                        success = True
                    
                    if not success:
                        display.alert()
                        continue
                
                return (
                    chose,
                    display.clear() + formatter.final(", ".join(chose))
                )
            
            return (
                pointer.get(),
                display.clear() + formatter.final(pointer.get())
            )
        
        elif key == Key.SPACE and multiple:
            if pointer.point in selected:
                selected.remove(pointer.point)
            
            else:
                selected.append(pointer.point)
        
        elif key == Key.UP:
            scroll = pointer.up()
        
        elif key == Key.DOWN:
            scroll = pointer.down()
        
        else:
            display.alert()

def amount(
    *,
    default: Optional[int] = None,
    factor: int = 1,
    maximum: Optional[int] = None,
    minimum: Optional[int] = None,
) -> PromptType[int]:
    r"""
    Parameters
    ----------
    default
        Integer to start at. Must be between ``maximum``
        and ``minimum`` in case they are defined. This
        can be any int-like value, that provides the
        ``__iadd__``, ``__isub__`` and ``__int__`` methods.
        Defaults to ``minimum`` if defined, otherwise
        ``0``.
    
    factor
        Integer indicating by how much the value should
        be increased/decreased.
    
    maximum
        Integer the value cannot exceed. When the value
        is not the maximum but the factor would make the
        value go above, the value stays the same. By default,
        there is no maximum value.
    
    minimum
        Same as ``maximum`` but with an integer the value
        cannot fall below.
    
    Returns
    -------
    int
        The adjusted value.
    """
    formatter: Formatter = yield None # type: ignore
    display = Display(navigation = {
        "enter": SYM_ENTER,
        "increase": [SYM_ARROW_UP, "+"],
        "decrease": [SYM_ARROW_DOWN, "-"],
    })
    
    if default is None:
        if minimum is not None:
            value = minimum
        
        else:
            value = 0
    
    else:
        value = default
    
    if minimum is not None and value < minimum:
        raise ValueError("value greater than minimum")
    
    if maximum is not None and value > maximum:
        raise ValueError("value less than maximum")
    
    while True:
        key = yield display(
            formatter.adjust_number(value)
        )
        
        if key == Key.ENTER:
            return (
                value,
                display.clear() + formatter.final(value)
            )
        
        elif key in [Key.UP, "+"]:
            value += factor
            if maximum is not None and value > maximum:
                value -= factor
                display.alert()
        
        elif key in [Key.DOWN, "-"]:
            value -= factor
            if minimum is not None and value < minimum:
                value += factor
                display.alert()
        
        else:
            display.alert()

def confirm(
    *,
    default: bool = True
) -> PromptType[bool]:
    r"""
    Parameters
    ----------
    default
        If the user does not type any value,
        this is going to be used.
    
    Returns
    -------
    bool
        The answer.
    """
    formatter: Formatter = yield None # type: ignore
    display = Display(navigation = {
        "enter": SYM_ENTER,
        "yes": "Y y",
        "no": "N n",
    })
    
    while True:
        key = yield display(
            formatter.confirm(default)
        )
        
        if key == Key.ENTER:
            return (
                bool(default),
                display.clear() + formatter.final("y" if default else "n")
            )
        
        elif key in "Yy":
            return (
                True,
                display.clear() + formatter.final("y")
            )
        
        elif key in "Nn":
            return (
                False,
                display.clear() + formatter.final("n")
            )
        
        else:
            display.alert()

def path(
    root: Union[Path, str, None] = None,
    *,
    allow_creation: bool = False,
    require_file: bool = False,
    multiple_files: bool = False,
) -> PromptType[Union[list[Path], Path]]:
    r"""
    .. versionadded:: 1.0.0b1
    
    Parameters
    ----------
    root
        Directory the user, where the user starts
        navigating. Defaults to current working
        directory.
    
    allow_creation
        Allows the creation of directories or files
        respectively. Note that only the directories
        that are required will be created and only after
        the user hits enter.
    
    require_file
        By default the user is prompted to select
        a directory. Be enabling this option, the
        a file is requires to be selected.
    
    multiple_files
        If ``require_file`` is enabled, this will
        allow selecting multiple files.
    
    Returns
    -------
    list[Path]
        List of path objects, when ``multiple_files``
        is enabled.
    
    Path
        The selected directory or file as a path
        object.
    """
    formatter: Formatter = yield None # type: ignore
    display = Display(navigation = {
        "enter": SYM_ENTER,
        "open directory": SYM_ARROW_RIGHT,
        "goto parent directory": SYM_ARROW_LEFT,
        "goto root directory": "r",
        **({"select/unselect": SYM_SPACE} if multiple_files else {}),
        **({"select current directoy": "."} if not require_file else {}),
        #**({"create directory": "n"} if allow_creation else {}),
    })
    
    root = Path(root or Path.cwd()).resolve()
    current_path = root
    if not current_path.exists():
        raise ValueError(f"{current_path} does not exist")
    
    selected: list[Path] = []
    scroll = 0
    
    # Because this is right at the start
    # it is okay to not catch permission
    # error.
    options = list(current_path.iterdir())
    
    pointer = Pointer(options)
    
    while True:
        tree = []
        for idx, d in enumerate(options):
            #d = directory.name
            
            apply = formatter.option
            
            if d in selected:
                apply = formatter.check
            
            elif multiple_files and d.is_file():
                apply = formatter.uncheck
            
            if idx == pointer.point:
                tree.append(apply(formatter.select(formatter.path(d))))
            
            else:
                tree.append(apply(formatter.unselect(formatter.path(d))))
        
        key = yield display(
            str(current_path) + "/\n",
            *tree,
            formatter.selected_files(selected) if multiple_files else "\n",
            scroll = scroll
        )
        
        if key == Key.ENTER:
            if multiple_files:
                return (
                    selected,
                    display.clear() + formatter.final(selected)
                )
            
            else:
                p = pointer.get()
                if p.is_file() == require_file:
                    return (
                        p,
                        display.clear() + formatter.final(p)
                    )
                
                display.alert()
        
        elif key == "." and not require_file:
            if not current_path.is_file():
                return(
                    current_path,
                    display.clear() + formatter.final(current_path)
                )
            
            display.alert()
        
        elif key == "r":
            current_path = root
            try:
                options = list(current_path.iterdir())
            except PermissionError:
                display.alert()
        
        elif key == Key.SPACE and multiple_files and options:
            p = pointer.get()
            
            if p.is_file():
                if p in selected:
                    selected.remove(p)
                
                else:
                    selected.append(p)
            
            else:
                display.alert()
        
        elif key == Key.RIGHT and options:
            p = pointer.get()
            
            if p.is_dir():
                before = current_path
                current_path /= p
                
                try:
                    options = list(current_path.iterdir())
                except PermissionError:
                    display.alert()
                    current_path = before
                    continue
                
                pointer = Pointer(options)
                scroll = 0
            
            else:
                display.alert()
        
        elif key == Key.UP and options:
            scroll = pointer.up()
        
        elif key == Key.DOWN and options:
            scroll = pointer.down()
        
        elif key == Key.LEFT:
            before = current_path
            current_path = current_path.parent
            
            try:
                options = list(current_path.iterdir())
            except PermissionError:
                display.alert()
                current_path = before
                continue
            
            pointer = Pointer(options)
            scroll = 0
        
        else:
            display.alert()
