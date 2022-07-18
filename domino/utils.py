# representacion grafica de las fichas
# +-----+
# |* * *|
# |* * *|
# |* * *|
# |-----|
# |* * *|
# |* * *|
# |* * *|
# +-----+

# +-----------+
# |* * *|* * *|
# |* * *|* * *|
# |* * *|* * *|
# +-----------+

# estas constantes definen la logica del juego
# posibles orientaciones para las fichas
VERTICAL = 0
HORIZONTAL = 1

# necesarios para la construccion del string que representa a las fichas
TOKENS_PARTS = [{}, {}]
TOKENS_PARTS[VERTICAL]["head"] = "+-----+"
TOKENS_PARTS[VERTICAL]["middle"] = "|-----|"
TOKENS_PARTS[VERTICAL][0] = ["|     |", "|     |", "|     |"]
TOKENS_PARTS[VERTICAL][1] = ["|     |", "|  *  |", "|     |"]
TOKENS_PARTS[VERTICAL][2] = ["|*    |", "|     |", "|    *|"]
TOKENS_PARTS[VERTICAL][3] = ["|*    |", "|  *  |", "|    *|"]
TOKENS_PARTS[VERTICAL][4] = ["|*   *|", "|     |", "|*   *|"]
TOKENS_PARTS[VERTICAL][5] = ["|*   *|", "|  *  |", "|*   *|"]
TOKENS_PARTS[VERTICAL][6] = ["|*   *|", "|*   *|", "|*   *|"]
TOKENS_PARTS[VERTICAL][7] = ["|*   *|", "|* * *|", "|*   *|"]
TOKENS_PARTS[VERTICAL][8] = ["|* * *|", "|*   *|", "|* * *|"]
TOKENS_PARTS[VERTICAL][9] = ["|* * *|", "|* * *|", "|* * *|"]

TOKENS_PARTS[HORIZONTAL]["head"] = "+|||+"
TOKENS_PARTS[HORIZONTAL]["middle"] = "-|||-"
TOKENS_PARTS[HORIZONTAL]["space"] = "-   -"
TOKENS_PARTS[HORIZONTAL][0] = ["-   -", "-   -", "-   -"]
TOKENS_PARTS[HORIZONTAL][1] = ["-   -", "- * -", "-   -"]
TOKENS_PARTS[HORIZONTAL][2] = ["-  *-", "-   -", "-*  -"]
TOKENS_PARTS[HORIZONTAL][3] = ["-  *-", "- * -", "-*  -"]
TOKENS_PARTS[HORIZONTAL][4] = ["-* *-", "-   -", "-* *-"]
TOKENS_PARTS[HORIZONTAL][5] = ["-* *-", "- * -", "-* *-"]
TOKENS_PARTS[HORIZONTAL][6] = ["-* *-", "-* *-", "-* *-"]
TOKENS_PARTS[HORIZONTAL][7] = ["-* *-", "-***-", "-* *-"]
TOKENS_PARTS[HORIZONTAL][8] = ["-***-", "-* *-", "-***-"]
TOKENS_PARTS[HORIZONTAL][9] = ["-***-", "-***-", "-***-"]

# estas constantes definen las posiibles configuraciones de cercania entre 2
# fichas
# +-----+
# |* * *|
# |* * *|
# |* * *|
# |--1--|
# |* * *|
# |* * *|
# |* * *|
# +-----+
# +-----+
# |* * *|
# |* * *|
# |* * *|
# |--2--|
# |* * *|
# |* * *|
# |* * *|
# +-----+
PROXIMITYCONFIGURACION_1 = 1

# +-----------++-----------+
# |* * *|* * *||* * *|* * *|
# |* * *1* * *||* * *2* * *|
# |* * *|* * *||* * *|* * *|
# +-----------++-----------+
PROXIMITYCONFIGURACION_2 = 2

# +-----++-----------+
# |* * *||* * *|* * *|
# |* * *||* * *2* * *|
# |* * *||* * *|* * *|
# |--1--|+-----------+
# |* * *|
# |* * *|
# |* * *|
# +-----+
PROXIMITYCONFIGURACION_3 = 3

# +-----+
# |* * *|
# |* * *|+-----------+
# |* * *||* * *|* * *|
# |--1--||* * *2* * *|
# |* * *||* * *|* * *|
# |* * *|+-----------+
# |* * *|
# +-----+
PROXIMITYCONFIGURACION_4 = 4

# +-----+
# |* * *|
# |* * *|
# |* * *|
# |--1--|+-----------+
# |* * *||* * *|* * *|
# |* * *||* * *2* * *|
# |* * *||* * *|* * *|
# +-----++-----------+
PROXIMITYCONFIGURACION_5 = 5

# +-----------++-----+
# |* * *|* * *||* * *|
# |* * *1* * *||* * *|
# |* * *|* * *||* * *|
# +-----------+|--2--|
#              |* * *|
#              |* * *|
#              |* * *|
#              +-----+
PROXIMITYCONFIGURACION_6 = 6

#              +-----+
#              |* * *|
# +-----------+|* * *|
# |* * *|* * *||* * *|
# |* * *1* * *||--2--|
# |* * *|* * *||* * *|
# +-----------+|* * *|
#              |* * *|
#              +-----+
PROXIMITYCONFIGURACION_7 = 7

#              +-----+
#              |* * *|
#              |* * *|
#              |* * *|
# +-----------+|--2--|
# |* * *|* * *||* * *|
# |* * *1* * *||* * *|
# |* * *|* * *||* * *|
# +-----------++-----+
PROXIMITYCONFIGURACION_8 = 8

# +-----------+
# |* * *|* * *|
# |* * *1* * *|
# |* * *|* * *|
# +-----------+
# +-----+
# |* * *|
# |* * *|
# |* * *|
# |--2--|
# |* * *|
# |* * *|
# |* * *|
# +-----+
PROXIMITYCONFIGURACION_9 = 9

# +-----------+
# |* * *|* * *|
# |* * *1* * *|
# |* * *|* * *|
# +-----------+
#    +-----+
#    |* * *|
#    |* * *|
#    |* * *|
#    |--2--|
#    |* * *|
#    |* * *|
#    |* * *|
#    +-----+
PROXIMITYCONFIGURACION_10 = 10

# +-----------+
# |* * *|* * *|
# |* * *1* * *|
# |* * *|* * *|
# +-----------+
#       +-----+
#       |* * *|
#       |* * *|
#       |* * *|
#       |--2--|
#       |* * *|
#       |* * *|
#       |* * *|
#       +-----+
PROXIMITYCONFIGURACION_11 = 11

# +-----+
# |* * *|
# |* * *|
# |* * *|
# |--1--|
# |* * *|
# |* * *|
# |* * *|
# +-----+
# +-----------+
# |* * *|* * *|
# |* * *2* * *|
# |* * *|* * *|
# +-----------+
PROXIMITYCONFIGURACION_12 = 12

#    +-----+
#    |* * *|
#    |* * *|
#    |* * *|
#    |--1--|
#    |* * *|
#    |* * *|
#    |* * *|
#    +-----+
# +-----------+
# |* * *|* * *|
# |* * *2* * *|
# |* * *|* * *|
# +-----------+
PROXIMITYCONFIGURACION_13 = 13

#       +-----+
#       |* * *|
#       |* * *|
#       |* * *|
#       |--1--|
#       |* * *|
#       |* * *|
#       |* * *|
#       +-----+
# +-----------+
# |* * *|* * *|
# |* * *2* * *|
# |* * *|* * *|
# +-----------+
PROXIMITYCONFIGURACION_14 = 14

# especifica que parte tiene libre una ficha para realizar conexiones
NUMERATOR = 0
DENOMINATOR = 1
BOTH = 2

# identificador para los jugadores
PLAYER = 0
COMPUTER = 1

# ============================================================================
# estas constantes definen como lucira el juego visualmente
# color para la seleccion de un elemento de alguna ventana(ficha, opciones)
COLOR_SELECTED_ELEMENT = 1
# color para el tablero activo(tablero de fichas o tablero de jugador)
COLOR_SELECTED_PANEL = 2

# ============================================================================
# estas constantes definen la logica del programa
# eventos que especifican a que pagina del programa se debe ir
NONE = 0
COVER = 1
PLAY = 2
OPTIONS = 3
HELP = 4
CREDITS = 5
QUIT = 6


def get_center_column(text, max_width):
    """
    Esta funcion retorna la posicion de la columna en que se debe poner un
    texto en una ventana para que quede centrado

    Parametros
    ----------
    text(str): Texto que sera centrado
    max_width(int): Ancho de la ventana en la que se escribira el texto
    """
    middle_tex = len(text) // 2
    return max_width // 2 - middle_tex


def get_center_row(max_height):
    """
    Esta funcion retorna la posicion de la fila en que se debe poner un
    texto en una ventana para que quede centrado

    Parametros
    ----------
    max_height(int): Alto de la ventana en la que se escribira el texto
    """
    return (max_height - 2) // 2


def apply_event(character, event):
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
