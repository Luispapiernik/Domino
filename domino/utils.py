from typing import Callable

from domino.schemas import Events, Key


def get_center_column(text: str, max_width: int):
    """
    This function returns the position of the column in which the text must be
    write in order to be column centered.

    Parameters
    ----------
    text: str
        Text that will be centered.
    max_width: int
        Width of the window in which the text will be writted.
    """
    middle_tex = len(text) // 2
    return max_width // 2 - middle_tex


def get_center_row(max_height: int):
    """
    This function returns the position of the row in which the text must be
    write in order to be row centered.

    Parameters
    ----------
    max_height: int
        Height of the window in which the text will be writed.
    """
    return (max_height - 2) // 2


def apply_event(character: Key, event: Events) -> Callable:
    """
    This function is a constructor of decorators that will be used to add
    automatically event managers to the windows.

    Parameters
    ----------
    character: int
        Integer that represents the Key that has been pressed.
    event: int
        Integer that represents the event that generates when the key is pressed.
    """

    def decorator(function):
        def wrapper(self, char: Key) -> Events:
            if character == char:
                return event
            else:
                return function(self, char)

        return wrapper

    return decorator
