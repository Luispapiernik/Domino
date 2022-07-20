import curses

from domino.container import BaseContainer
from domino.schemas import Key


class Board(BaseContainer):
    """
    This class represents a container where a token can be placed.

    Parameters
    ----------
    window: curses.window
        Window where the tokens will be drawed.
    vertical_scrollable: bool
        This indicated if the window can be vertical scrollable.
    horizontal_scrollable: bool
        This indicated if the window can be horizontal scrollable.
    """

    def __init__(
        self,
        window: curses.window,
        vertical_scrollable: bool = True,
        horizontal_scrollable: bool = True,
    ) -> None:
        super().__init__(window)

        self.vertical_scrollable = vertical_scrollable
        self.horizontal_scrollable = horizontal_scrollable

    def input_handler(self, char: Key) -> None:
        # The scrolling works by changing the offset that will be applied to the
        # positions of the tokens when drawed.
        if self.vertical_scrollable:
            if char == 259:  # UP
                self.zero_position[0] -= 1
            if char == 258:  # DOWN
                self.zero_position[0] += 1
        if self.horizontal_scrollable:
            if char == 260:  # RIGHT
                self.zero_position[1] -= 1
            if char == 261:  # LEFT
                self.zero_position[1] += 1
        if char == 114:  # r
            self.elements[self.linter][0].reflect()
