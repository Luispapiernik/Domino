import curses

from domino.container import BaseContainer
from domino.schemas import Events, Key
from domino.utils import apply_event, get_center_column, get_center_row
from domino.writable import Writable


class PageNotImplemented(BaseContainer):
    """
    Esta clase reprensenta alguna ventana que no ha sido implementada
    """

    def __init__(self, height: int, width: int) -> None:
        window = curses.newwin(height, width, 0, 0)

        super().__init__(window)

        center_position_x = get_center_row(height)

        self.add_elements(
            Writable(
                "No implementado",
                (center_position_x, get_center_column("No implementado", width)),
            )
        )

    @apply_event(10, Events.COVER)  # ENTER
    def input_handler(self, _: Key) -> Events:
        pass


class Cover(BaseContainer):
    """
    Esta clase reprensenta la primera ventana del aplicacion, en ella estan las
    diferentes opciones que puede elejir un jugador: Jugar, Opciones,...

    Parametros
    ----------
    max_height: int
        Altura de la ventana.
    max_width: int
        Ancho de la ventana.
    """

    def __init__(self, max_height: int, max_width: int) -> None:
        # se crea la ventana en donde se dibujaran los elementos
        window = curses.newwin(max_height, max_width, 0, 0)

        # se llama al inicializador del padre
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

    @apply_event(
        curses.KEY_RESIZE, Events.QUIT
    )  # cuando se cambia dimension de la ventana
    @apply_event(113, Events.QUIT)  # q
    def input_handler(self, char: Key) -> Events:
        """
        Este metodo se encarga de manejar entrada del usuario, la clase Cover
        solo gestiona el cambio de ventana
        """
        # self.linter esta apuntando al elmento que es resaltado, si se aumenta
        # o disminuye este valor en uno el objeto resaltado cambia, si se
        # preciona la tecla enter en uno de los elementos se pasa a la ventana
        # correspondiente
        if char == 259:  # UP
            self.linter -= 1
        elif char == 258:  # DOWN
            self.linter += 1
        elif char == 10:  # ENTER
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

        # self.linter no debe estar por fuera de [0, 3], si esta por fuera con
        # operacion modulo se vuelve a poner en el conjunto [0, 3]
        self.linter %= self.linterable_objects


class Options(PageNotImplemented):
    pass


class Help(PageNotImplemented):
    pass


class Credits(PageNotImplemented):
    pass
