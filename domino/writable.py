import curses
from typing import List, Optional, Union

from domino.schemas import Position


class Writable:
    """
    This class represent something that can be draw on screen, basically text.

    Parameters
    ----------
    text: str, List[str]
        Contains the string that will be drawed. For multiline text a list of strings
        must be provided.
    position: Position
        Position of the text on the screen.
    """

    # TODO: Add a parameter for color.
    def __init__(self, text: Union[str, List[str]], position: Position) -> None:
        # multiline text correspond to a list of strings
        self.text = [text] if isinstance(text, str) else text
        # The first component represent rows and the second columns.
        self.position = position

    def write(
        self,
        window: curses.window,
        offset: Position,
        color_linter: Optional[int] = None,
    ) -> None:
        """
        This method writes text on a given window.

        Parameters
        ----------
        window: curses.window
            Window where the text will be drawed.
        offset: Position
            Offset to apply to the position of the text.
        color_linter: Optional[int]
            Color to apply to the drawed text.
        """
        if color_linter is not None:
            window.attron(curses.color_pair(color_linter))

        height, width = window.getmaxyx()
        for x in range(len(self.text[0])):
            for y in range(len(self.text)):
                column = self.position[1] + x + offset[1]
                row = self.position[0] + y + offset[0]

                # Only what is inside the window gets drawed.
                if 0 < row < height - 1 and 0 < column < width - 1:
                    window.addch(row, column, self.text[y][x])

        if color_linter is not None:
            # When a color was applied, must be deactivated.
            window.attroff(curses.color_pair(color_linter))
