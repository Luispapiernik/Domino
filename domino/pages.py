import curses

from domino.container import BaseContainer
from domino.schemas import Events, Key
from domino.utils import apply_event, get_center_column, get_center_row
from domino.writable import Writable


class PageNotImplemented(BaseContainer):
    """
    This class represent some window that is not implemented.
    """

    def __init__(self, height: int, width: int) -> None:
        window = curses.newwin(height, width, 0, 0)

        super().__init__(window)

        center_position_x = get_center_row(height)

        self.add_elements(
            Writable(
                "Not implemented",
                (center_position_x, get_center_column("Not implemented", width)),
            )
        )

    # When the ENTER key is pressed.
    @apply_event(10, Events.COVER)
    def input_handler(self, _: Key) -> Events:
        pass


class Cover(BaseContainer):
    """
    This class represent the first application window, in this the differents
    options (Play, Options, Help, ...) are displayed.

    Parameters
    ----------
    max_height: int
        Window height.
    max_width: int
        Window width.
    """

    def __init__(self, max_height: int, max_width: int) -> None:
        window = curses.newwin(max_height, max_width, 0, 0)
        super().__init__(window)

        # para dibujar los elementos de forma centrada se obtiene la fila que
        # esta en el centro
        center_position_x = get_center_row(max_height)

        # se agregan los elementos
        self.add_elements(
            Writable(
                "Jugar", (center_position_x, get_center_column("Jugar", max_width))
            )
        )

        self.add_elements(
            Writable(
                "Opciones",
                (center_position_x + 1, get_center_column("Opciones", max_width)),
            )
        )

        self.add_elements(
            Writable(
                "Ayuda", (center_position_x + 2, get_center_column("Ayuda", max_width))
            )
        )

        self.add_elements(
            Writable(
                "Credito",
                (center_position_x + 3, get_center_column("Credito", max_width)),
            )
        )

    # When the dimension of the window is changed.
    @apply_event(curses.KEY_RESIZE, Events.QUIT)
    # When the key Q is pressed.
    @apply_event(113, Events.QUIT)
    def input_handler(self, char: Key) -> Events:
        # self.linter esta apuntando al elmento que es resaltado, si se aumenta
        # o disminuye este valor en uno el objeto resaltado cambia, si se
        # preciona la tecla enter en uno de los elementos se pasa a la ventana
        # correspondiente
        if char == 259:  # UP
            self.linter -= 1
        if char == 258:  # DOWN
            self.linter += 1

        # self.linter no debe estar por fuera de [0, 3], si esta por fuera con
        # operacion modulo se vuelve a poner en el conjunto [0, 3]
        self.linter %= self.linterable_objects

        if char == 10:  # ENTER
            if self.linter == 0:
                return Events.PLAY
            elif self.linter == 1:
                return Events.OPTIONS
            elif self.linter == 2:
                return Events.HELP
            elif self.linter == 3:
                return Events.CREDITS
            else:
                return Events.NONE
        else:
            pass


class Options(PageNotImplemented):
    pass


class Help(PageNotImplemented):
    pass


class Credits(PageNotImplemented):
    pass
