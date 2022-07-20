import curses
from optparse import Option
from typing import Optional

from domino.board import Board
from domino.schemas import Key
from domino.writable import Writable


class PlayerTable(Board):
    """
    This class represents the board where the user tokens are placed.

    Parameters
    ----------
    max_height, max_width: int
        Dimensions of the entire screen.
    """

    def __init__(self, max_height: int, max_width: int) -> None:
        window = curses.newwin(11, max_width - 30, max_height - 12, 1)

        super().__init__(window, vertical_scrollable=False)

    def input_handler(self, char: Key) -> Optional[Writable]:
        super().input_handler(char)

        # When the Key "a" is pressed
        if char == 97:
            self.linter -= 1
        # When the Key "d" is pressed
        elif char == 100:
            self.linter += 1
        # When the Key "ENTER" is pressed
        elif char == 10:
            # cuando se presiona ENTER el jugador hace la jugada, retornando la
            # ficha que esta resaltada
            return self.elements[self.linter][0]
        else:
            pass

        self.linter %= self.linterable_objects
        return None
