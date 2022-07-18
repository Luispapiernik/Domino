import curses

from domino.board import Board
from domino.schemas import Key
from domino.writable import Writable


class PlayerTable(Board):
    """
    Esta clase representa el tablero en donde se ubicaran las fichas del
    jugador

    Parametros
    ----------
    max_height(int): altura de la ventana
    max_width(int): ancho de la ventana
    """

    def __init__(self, max_height: int, max_width: int):
        window = curses.newwin(11, max_width - 30, max_height - 12, 1)

        super().__init__(window, vertical_scrollable=False)

    def input_handler(self, char: Key) -> Writable:
        # el metodo input_handler se encarga de manejar el scrolling de la ficha
        super().input_handler(char)

        # manejo del resaltado de las fichas
        if char == 97:  # a
            self.linter -= 1
        elif char == 100:  # d
            self.linter += 1
        elif char == 10:  # ENTER
            # cuando se presiona ENTER el jugador hace la jugada, retornando la
            # ficha que esta resaltada
            return self.elements[self.linter][0]
        else:
            pass

        self.linter %= self.linterable_objects
