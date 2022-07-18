from typing import Callable

from domino.schemas import Events, Key


def get_center_column(text: str, max_width: int):
    """
    Esta funcion retorna la posicion de la columna en que se debe poner un
    texto en una ventana para que quede centrado.

    Parametros
    ----------
    text: str
        Texto que sera centrado.
    max_width: int
        Ancho de la ventana en la que se escribira el texto.
    """
    middle_tex = len(text) // 2
    return max_width // 2 - middle_tex


def get_center_row(max_height: int):
    """
    Esta funcion retorna la posicion de la fila en que se debe poner un
    texto en una ventana para que quede centrado.

    Parametros
    ----------
    max_height: int
        Alto de la ventana en la que se escribira el texto.
    """
    return (max_height - 2) // 2


def apply_event(character: Key, event: Events) -> Callable:
    """
    Esta funcion es un constructor de decoradores que se usara para agregar de
    forma automatica el manejo de algunos eventos a las ventanas

    Parametros
    ----------
    character(int): Entero que representa la tecla que ha sido presionada
    event(int): Entero que representa el evento que genera la tecla presionada
        puede ser COVER, PLAY, OPTIONS,...
    """

    def decorator(function):
        def wrapper(self, char):
            if character == char:
                return event
            else:
                return function(self, char)

        return wrapper

    return decorator
