import curses
from typing import Optional, Tuple

from domino.schemas import Events, Key
from domino.writable import Writable


class BaseContainer:
    """
    This class represent a panel, that is, a container for writable objects.

    Parametros
    ----------
    window: curses.window
        Windows where the container's elements will be drawed.
    """

    def __init__(self, window: curses.window) -> None:
        self.window = window
        self.height, self.width = self.window.getmaxyx()

        # Offset that will be applied to all element in the container
        self.zero_position = [0, 0]

        # In every item, the second component indicates if the writable element
        # must be highlighted or not.
        self.elements: Tuple[Writable, bool] = []

        # index of the element to highligh
        self.linter = 0  # indice del elemento a resaltar
        # Number of highlightable elements.
        self.linterable_objects = 0

    def add_elements(self, element: Writable, linterable: bool = True) -> None:
        """
        This element add one element to the container.

        Parameters
        ----------
        element: Writable
            Element that will be added.
        linterable: bool
            If the element is highlightable or not.
        """
        self.elements.append((element, linterable))
        if linterable:
            self.linterable_objects += 1

    def input_handler(self, char: Key) -> Events:
        """
        This method defined how the container reacts to user inputs.
        """
        pass

    def write(self, border_color: Optional[int] = None) -> None:
        """
        This method draws the container and all his elements on screen.

        Parameters
        ----------
        border_color: Optional[int]
            Color to apply to the drawed border of the container.
        """
        # First the all drawed string must be erased.
        self.window.erase()

        # In order to apply a color to the border of the panel.
        if border_color is not None:
            self.window.attron(curses.color_pair(border_color))

        # The border of the container is painted.
        self.window.box()

        # Deactivated the color if was activated before.
        if border_color is not None:
            self.window.attroff(curses.color_pair(border_color))

        # Contains the color for the highlightable element.
        color_linter = None
        for i in range(len(self.elements)):
            element, linterable = self.elements[i]

            if i == self.linter and linterable:
                color_linter = 1

            element.write(self.window, self.zero_position, color_linter)

            # Only a single element get highlighted.
            color_linter = None

        # Load changes on screen.
        self.window.refresh()
