from __future__ import annotations

import signal
import sys
from typing import (
    Any,
    Callable,
    Optional,
)

from readchar import readkey, key as Key

from .formatters import Formatter, ColoredFormatter
from .prompts import T, PromptType
from .utils import set_stream, _file


#T = TypeVar("T")


def prompt(
    message: str,
    kind: PromptType[T],
    *,
    cleanup: Optional[Callable[[], None]] = None,
    formatter: Optional[Formatter] = None,
) -> T:
    r"""
    Prompts can be interrupted by pressing
    Ctrl-C (which will trigged `cleanup`) or
    Ctrl-\.
    
    Parameters
    ----------
    message
        The message/question to display.
    
    kind
        The kind of prompt to use. Select one
        from the :mod:`prompts` module or
        `a custom defined one`.
    
    cleanup
        A callable that will be called when the
        user hits Ctrl-C during a prompt. After
        that, the programm will be terminated.
    
    formatter
        A :class:`Formatter` that formats the prompt.
        Defaults to :class:`formatters.ColoredFormatter`.
    
    Returns
    -------
    The prompt's return value.
    """
    if formatter is None:
        formatter = ColoredFormatter()
    
    _file.write(formatter.ask(message))
    _file.flush()
    
    next(kind)
    text = kind.send(formatter) # type: ignore
    
    try:
        while True:
            _file.write(text)
            _file.flush()
            
            key = readkey()
            
            if key == Key.CTRL_C:
                if cleanup is not None:
                    cleanup()
                
                sys.exit(signal.SIGINT)
            
            text = kind.send(key)
    
    except StopIteration as result:
        if result is None:
            raise RuntimeError(f"{kind.__name__!r} never returned anything")
        
        res, post = result.value
        
        if post is not None:
            _file.write(post + "\n")
            _file.flush()
        
        return res
