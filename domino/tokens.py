from typing import Dict, List, Tuple, Union

from domino.schemas import ProximitiesConfigurations, TokenOrientations, TokenParts
from domino.writable import Writable

# graphic representation of the tokens
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

# necesarios para la construccion del string que representa a las fichas
TOKENS_PARTS: List[Dict[Union[str, int], Union[str, List[str]]]] = [{}, {}]
TOKENS_PARTS[TokenOrientations.VERTICAL]["head"] = "+-----+"
TOKENS_PARTS[TokenOrientations.VERTICAL]["middle"] = "|-----|"
TOKENS_PARTS[TokenOrientations.VERTICAL][0] = ["|     |", "|     |", "|     |"]
TOKENS_PARTS[TokenOrientations.VERTICAL][1] = ["|     |", "|  *  |", "|     |"]
TOKENS_PARTS[TokenOrientations.VERTICAL][2] = ["|*    |", "|     |", "|    *|"]
TOKENS_PARTS[TokenOrientations.VERTICAL][3] = ["|*    |", "|  *  |", "|    *|"]
TOKENS_PARTS[TokenOrientations.VERTICAL][4] = ["|*   *|", "|     |", "|*   *|"]
TOKENS_PARTS[TokenOrientations.VERTICAL][5] = ["|*   *|", "|  *  |", "|*   *|"]
TOKENS_PARTS[TokenOrientations.VERTICAL][6] = ["|*   *|", "|*   *|", "|*   *|"]
TOKENS_PARTS[TokenOrientations.VERTICAL][7] = ["|*   *|", "|* * *|", "|*   *|"]
TOKENS_PARTS[TokenOrientations.VERTICAL][8] = ["|* * *|", "|*   *|", "|* * *|"]
TOKENS_PARTS[TokenOrientations.VERTICAL][9] = ["|* * *|", "|* * *|", "|* * *|"]

TOKENS_PARTS[TokenOrientations.HORIZONTAL]["head"] = "+|||+"
TOKENS_PARTS[TokenOrientations.HORIZONTAL]["middle"] = "-|||-"
TOKENS_PARTS[TokenOrientations.HORIZONTAL]["space"] = "-   -"
TOKENS_PARTS[TokenOrientations.HORIZONTAL][0] = ["-   -", "-   -", "-   -"]
TOKENS_PARTS[TokenOrientations.HORIZONTAL][1] = ["-   -", "- * -", "-   -"]
TOKENS_PARTS[TokenOrientations.HORIZONTAL][2] = ["-  *-", "-   -", "-*  -"]
TOKENS_PARTS[TokenOrientations.HORIZONTAL][3] = ["-  *-", "- * -", "-*  -"]
TOKENS_PARTS[TokenOrientations.HORIZONTAL][4] = ["-* *-", "-   -", "-* *-"]
TOKENS_PARTS[TokenOrientations.HORIZONTAL][5] = ["-* *-", "- * -", "-* *-"]
TOKENS_PARTS[TokenOrientations.HORIZONTAL][6] = ["-* *-", "-* *-", "-* *-"]
TOKENS_PARTS[TokenOrientations.HORIZONTAL][7] = ["-* *-", "-***-", "-* *-"]
TOKENS_PARTS[TokenOrientations.HORIZONTAL][8] = ["-***-", "-* *-", "-***-"]
TOKENS_PARTS[TokenOrientations.HORIZONTAL][9] = ["-***-", "-***-", "-***-"]


def are_close(
    token1: Union["LightToken", "Token"], token2: Union["LightToken", "Token"]
) -> bool:
    """
    Esta funcion retorna la configuracion de conexion que hay entre 2 fichas.

    Parametros
    ----------
    token1: Union[LightToken, Token]
        Ficha uno.
    token2: Union[LightToken, Token]
        Ficha dos.

    Returns
    -------
    int | False: entero entre 1 y 14 que representa que tipo de conexion tienen
        las fichas, se retorna False si no estan conectadas
    """

    # para detectar que 2 fichas estan conectadas de forma validad, se hace uso
    # de la separacion entre sus esquinas superior izquierda.
    # la componente cero de position indica posicion en el eje y(filas), la
    # componente 1 indica posicion en el eje x(columnas)

    vertical_diference = token1.position[0] - token2.position[0]
    horizontal_diference = token1.position[1] - token2.position[1]

    # configuracion de cercania 1
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
    # si las fichas estan en la misma columna
    if token1.position[1] == token2.position[1]:
        # si ambas fichas estan orientadas de forma vertical
        if token1.is_vertical() and token2.is_vertical():
            # token1 esta abajo
            if vertical_diference == 9:
                return -ProximitiesConfigurations.PROXIMITYCONFIGURATION_1
            # token2 esta abajo
            if vertical_diference == -9:
                return ProximitiesConfigurations.PROXIMITYCONFIGURATION_1

    # configuracion de cercania 2
    # +-----------++-----------+
    # |* * *|* * *||* * *|* * *|
    # |* * *1* * *||* * *2* * *|
    # |* * *|* * *||* * *|* * *|
    # +-----------++-----------+
    # si ambas fichas estan en la misma fila
    if token1.position[0] == token2.position[0]:
        # si ambas fichas estan orientadas de forma horizontal
        if token1.is_horizontal() and token2.is_horizontal():
            # token1 esta a la derecha
            if horizontal_diference == 13:
                return -ProximitiesConfigurations.PROXIMITYCONFIGURATION_2
            # token2 esta a la derecha
            if horizontal_diference == -13:
                return ProximitiesConfigurations.PROXIMITYCONFIGURATION_2

    # configuracion de cercania 3
    # +-----++-----------+
    # |* * *||* * *|* * *|
    # |* * *||* * *2* * *|
    # |* * *||* * *|* * *|
    # |--1--|+-----------+
    # |* * *|
    # |* * *|
    # |* * *|
    # +-----+
    if token1.position[0] == token2.position[0]:
        # token 1 es el de la derecha
        if horizontal_diference == 7:
            return -ProximitiesConfigurations.PROXIMITYCONFIGURATION_3
        # token 2 a la derecha
        if horizontal_diference == -7:
            return ProximitiesConfigurations.PROXIMITYCONFIGURATION_3

    # configuracion de cercania 4
    # +-----+
    # |* * *|
    # |* * *|+-----------+
    # |* * *||* * *|* * *|
    # |--1--||* * *2* * *|
    # |* * *||* * *|* * *|
    # |* * *|+-----------+
    # |* * *|
    # +-----+
    if abs(vertical_diference) == 2:
        # token1 el de la derecha
        if horizontal_diference == 7:
            return -ProximitiesConfigurations.PROXIMITYCONFIGURATION_4
        # token2 a la derecha
        if horizontal_diference == -7:
            return ProximitiesConfigurations.PROXIMITYCONFIGURATION_4

    # configuracion de cercania 5
    # +-----+
    # |* * *|
    # |* * *|
    # |* * *|
    # |--1--|+-----------+
    # |* * *||* * *|* * *|
    # |* * *||* * *2* * *|
    # |* * *||* * *|* * *|
    # +-----++-----------+
    if abs(vertical_diference) == 4:
        # token1 a la derecha
        if horizontal_diference == 7:
            return -ProximitiesConfigurations.PROXIMITYCONFIGURATION_5
        # token2 a la derecha
        if horizontal_diference == -7:
            return ProximitiesConfigurations.PROXIMITYCONFIGURATION_5

    # configuracion de cercania 6
    # +-----------++-----+
    # |* * *|* * *||* * *|
    # |* * *1* * *||* * *|
    # |* * *|* * *||* * *|
    # +-----------+|--2--|
    #              |* * *|
    #              |* * *|
    #              |* * *|
    #              +-----+
    if token1.position[0] == token2.position[0]:
        # token1 a la derecha
        if horizontal_diference == 13:
            return -ProximitiesConfigurations.PROXIMITYCONFIGURATION_6
        if horizontal_diference == -13:
            return ProximitiesConfigurations.PROXIMITYCONFIGURATION_6

    # configuracion de cercania 7
    #              +-----+
    #              |* * *|
    # +-----------+|* * *|
    # |* * *|* * *||* * *|
    # |* * *1* * *||--2--|
    # |* * *|* * *||* * *|
    # +-----------+|* * *|
    #              |* * *|
    #              +-----+
    if abs(vertical_diference) == 2:
        # token1 a la derecha
        if horizontal_diference == 13:
            return -ProximitiesConfigurations.PROXIMITYCONFIGURATION_7
        # token2 a la derecha
        if horizontal_diference == -13:
            return ProximitiesConfigurations.PROXIMITYCONFIGURATION_7

    # configuracion de cercania 8
    #              +-----+
    #              |* * *|
    #              |* * *|
    #              |* * *|
    # +-----------+|--2--|
    # |* * *|* * *||* * *|
    # |* * *1* * *||* * *|
    # |* * *|* * *||* * *|
    # +-----------++-----+
    if abs(vertical_diference) == 4:
        # token1 a la derecha
        if horizontal_diference == 13:
            return -ProximitiesConfigurations.PROXIMITYCONFIGURATION_8
        # token2 a la derecha
        if horizontal_diference == -13:
            return ProximitiesConfigurations.PROXIMITYCONFIGURATION_8

    # configuracion de cercania 9
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
    if token1.position[1] == token2.position[1]:
        # token1 abajo
        if vertical_diference == 5:
            return -ProximitiesConfigurations.PROXIMITYCONFIGURATION_9
        # token1 abajo
        if vertical_diference == -5:
            return ProximitiesConfigurations.PROXIMITYCONFIGURATION_9

    # configuracion de cercania 10
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
    if abs(horizontal_diference) == 3:
        # token1 abajo
        if vertical_diference == 5:
            return -ProximitiesConfigurations.PROXIMITYCONFIGURATION_10
        # token2 abajo
        if vertical_diference == -5:
            return ProximitiesConfigurations.PROXIMITYCONFIGURATION_10

    # configuracion de cercania 11
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
    if abs(horizontal_diference) == 6:
        # token1 abajo
        if vertical_diference == 5:
            return -ProximitiesConfigurations.PROXIMITYCONFIGURATION_11
        # token2 abajo
        if vertical_diference == -5:
            return ProximitiesConfigurations.PROXIMITYCONFIGURATION_11

    # configuracion de cercania 12
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
    if token1.position[1] == token2.position[1]:
        # token1 abajo
        if vertical_diference == 9:
            return -ProximitiesConfigurations.PROXIMITYCONFIGURATION_12
        # token2 abajo
        if vertical_diference == -9:
            return ProximitiesConfigurations.PROXIMITYCONFIGURATION_12

    # configuracion de cercania 13
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
    if abs(horizontal_diference) == 3:
        # token1 abajo
        if vertical_diference == 9:
            return -ProximitiesConfigurations.PROXIMITYCONFIGURATION_13
        # token2 abajo
        if vertical_diference == -9:
            return ProximitiesConfigurations.PROXIMITYCONFIGURATION_13

    # configuracion de cercania 14
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
    if abs(horizontal_diference) == 6:
        # token1 abajo
        if vertical_diference == 9:
            return -ProximitiesConfigurations.PROXIMITYCONFIGURATION_14
        # token2 abajo
        if vertical_diference == -9:
            return ProximitiesConfigurations.PROXIMITYCONFIGURATION_14

    return False


def getFreeSide(
    token1: Union["LightToken", "Token"], token2: Union["LightToken", "Token"]
) -> Union[int, bool]:
    """
    Esta funcion retorna que lado queda libre una vez se han conectado 2 fichas.

    Parametros
    ----------
    token1: Union[LightToken, Token]
        Ficha uno, el lado libre que se retorna corresponde a esta ficha.
    token2: Union[LightToken, Token]
        Ficha 2, es la ficha que se conecta a la ficha uno.

    Return
    ------
    outs: Union[int, False]
        Entero que representa que lado quedo libre, puede ser TokenParts.NUMERATOR,
        TokenParts.DENOMINATOR o TokenParts.BOTH y se retorna False si no estan conectadas
    """
    # se obtiene que tipo de conexion tienen las fichas
    are_close = are_close(token1, token2)

    if are_close == ProximitiesConfigurations.PROXIMITYCONFIGURATION_1:
        return TokenParts.NUMERATOR
    elif are_close == -ProximitiesConfigurations.PROXIMITYCONFIGURATION_1:
        return TokenParts.DENOMINATOR
    elif are_close == ProximitiesConfigurations.PROXIMITYCONFIGURATION_2:
        return TokenParts.NUMERATOR
    elif are_close == -ProximitiesConfigurations.PROXIMITYCONFIGURATION_2:
        return TokenParts.DENOMINATOR
    elif are_close == ProximitiesConfigurations.PROXIMITYCONFIGURATION_3:
        return TokenParts.DENOMINATOR
    elif are_close == -ProximitiesConfigurations.PROXIMITYCONFIGURATION_3:
        return TokenParts.DENOMINATOR
    elif are_close == ProximitiesConfigurations.PROXIMITYCONFIGURATION_4:
        return TokenParts.BOTH
    elif are_close == -ProximitiesConfigurations.PROXIMITYCONFIGURATION_4:
        return TokenParts.DENOMINATOR
    elif are_close == ProximitiesConfigurations.PROXIMITYCONFIGURATION_5:
        return TokenParts.NUMERATOR
    elif are_close == -ProximitiesConfigurations.PROXIMITYCONFIGURATION_5:
        return TokenParts.DENOMINATOR
    elif are_close == ProximitiesConfigurations.PROXIMITYCONFIGURATION_6:
        return TokenParts.NUMERATOR
    elif are_close == -ProximitiesConfigurations.PROXIMITYCONFIGURATION_6:
        return TokenParts.DENOMINATOR
    elif are_close == ProximitiesConfigurations.PROXIMITYCONFIGURATION_7:
        return TokenParts.NUMERATOR
    elif are_close == -ProximitiesConfigurations.PROXIMITYCONFIGURATION_7:
        return TokenParts.BOTH
    elif are_close == ProximitiesConfigurations.PROXIMITYCONFIGURATION_8:
        return TokenParts.NUMERATOR
    elif are_close == -ProximitiesConfigurations.PROXIMITYCONFIGURATION_8:
        return TokenParts.NUMERATOR
    elif are_close == ProximitiesConfigurations.PROXIMITYCONFIGURATION_9:
        return TokenParts.DENOMINATOR
    elif are_close == -ProximitiesConfigurations.PROXIMITYCONFIGURATION_9:
        return TokenParts.DENOMINATOR
    elif are_close == ProximitiesConfigurations.PROXIMITYCONFIGURATION_10:
        return TokenParts.BOTH
    elif are_close == -ProximitiesConfigurations.PROXIMITYCONFIGURATION_10:
        return TokenParts.DENOMINATOR
    elif are_close == ProximitiesConfigurations.PROXIMITYCONFIGURATION_11:
        return TokenParts.NUMERATOR
    elif are_close == -ProximitiesConfigurations.PROXIMITYCONFIGURATION_11:
        return TokenParts.DENOMINATOR
    elif are_close == ProximitiesConfigurations.PROXIMITYCONFIGURATION_12:
        return TokenParts.NUMERATOR
    elif are_close == -ProximitiesConfigurations.PROXIMITYCONFIGURATION_12:
        return TokenParts.DENOMINATOR
    elif are_close == ProximitiesConfigurations.PROXIMITYCONFIGURATION_13:
        return TokenParts.NUMERATOR
    elif are_close == -ProximitiesConfigurations.PROXIMITYCONFIGURATION_13:
        return TokenParts.TokenParts.BOTH
    elif are_close == ProximitiesConfigurations.PROXIMITYCONFIGURATION_14:
        return TokenParts.NUMERATOR
    elif are_close == -ProximitiesConfigurations.PROXIMITYCONFIGURATION_14:
        return TokenParts.NUMERATOR
    else:
        return False


def _are_compatible(
    token1: Union["LightToken", "Token"], token2: Union["LightToken", "Token"]
) -> bool:
    """
    Esta funcion retorna True cuando 2 fichas estan bien conectadas segun las
    regla del domino y False en caso contrario.

    Parametros
    ----------
    token1: Union[LightToken, Token]
        Ficha uno.
    token2: Union[LightToken, Token]
        Ficha dos.
    """

    # 2 fichas estan bien conectadas si ademas de estar conectadas, los valores
    # de los numeradores o denominadores coinciden en el punto de conexion

    # se obtiene el tipo de conexion que tienen las fichas
    are_close = are_close(token1, token2)

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
    if are_close == ProximitiesConfigurations.PROXIMITYCONFIGURATION_1:
        # token1 esta arriba
        return token1.denominator == token2.numerator
    elif are_close == -ProximitiesConfigurations.PROXIMITYCONFIGURATION_1:
        # token1 esta abajo
        return token1.numerator == token2.denominator

    # +-----------++-----------+
    # |* * *|* * *||* * *|* * *|
    # |* * *1* * *||* * *2* * *|
    # |* * *|* * *||* * *|* * *|
    # +-----------++-----------+
    elif are_close == ProximitiesConfigurations.PROXIMITYCONFIGURATION_2:
        # token1 esta a la izquierda
        return token1.denominator == token2.denominator
    elif are_close == -ProximitiesConfigurations.PROXIMITYCONFIGURATION_2:
        # token1 esta a la derecha
        return token1.numerator == token2.denominator

    # +-----++-----------+
    # |* * *||* * *|* * *|
    # |* * *||* * *2* * *|
    # |* * *||* * *|* * *|
    # |--1--|+-----------+
    # |* * *|
    # |* * *|
    # |* * *|
    # +-----+
    elif are_close == ProximitiesConfigurations.PROXIMITYCONFIGURATION_3:
        # token1 esta a la izquierda
        return token1.numerator == token2.numerator
    elif are_close == -ProximitiesConfigurations.PROXIMITYCONFIGURATION_3:
        # token1 esta a la derecha
        return token1.numerator == token2.numerator

    # +-----+
    # |* * *|
    # |* * *|+-----------+
    # |* * *||* * *|* * *|
    # |--1--||* * *2* * *|
    # |* * *||* * *|* * *|
    # |* * *|+-----------+
    # |* * *|
    # +-----+
    elif are_close == ProximitiesConfigurations.PROXIMITYCONFIGURATION_4:
        # token1 esta a la izquierda
        return token1.numerator == token1.denominator == token2.numerator
    elif are_close == -ProximitiesConfigurations.PROXIMITYCONFIGURATION_4:
        # token1 esta a la derecha
        return token1.numerator == token2.numerator == token2.denominator

    # +-----+
    # |* * *|
    # |* * *|
    # |* * *|
    # |--1--|+-----------+
    # |* * *||* * *|* * *|
    # |* * *||* * *2* * *|
    # |* * *||* * *|* * *|
    # +-----++-----------+
    elif are_close == ProximitiesConfigurations.PROXIMITYCONFIGURATION_5:
        # token1 esta a la izquierda
        return token1.denominator == token2.numerator
    elif are_close == -ProximitiesConfigurations.PROXIMITYCONFIGURATION_5:
        # token1 esta a la derecha
        return token1.numerator == token2.denominator

    # +-----------++-----+
    # |* * *|* * *||* * *|
    # |* * *1* * *||* * *|
    # |* * *|* * *||* * *|
    # +-----------+|--2--|
    #              |* * *|
    #              |* * *|
    #              |* * *|
    #              +-----+
    elif are_close == ProximitiesConfigurations.PROXIMITYCONFIGURATION_6:
        # token1 esta a la izquierda
        return token1.denominator == token2.numerator
    elif are_close == -ProximitiesConfigurations.PROXIMITYCONFIGURATION_6:
        # token1 esta a la derecha
        return token1.numerator == token2.denominator

    #              +-----+
    #              |* * *|
    # +-----------+|* * *|
    # |* * *|* * *||* * *|
    # |* * *1* * *||--2--|
    # |* * *|* * *||* * *|
    # +-----------+|* * *|
    #              |* * *|
    #              +-----+
    elif are_close == ProximitiesConfigurations.PROXIMITYCONFIGURATION_7:
        # token1 esta a la izquierda
        return token1.denominator == token2.numerator == token2.denominator
    elif are_close == -ProximitiesConfigurations.PROXIMITYCONFIGURATION_7:
        # token1 esta a la derecha
        return token1.numerator == token1.denominator == token2.denominator

    #              +-----+
    #              |* * *|
    #              |* * *|
    #              |* * *|
    # +-----------+|--2--|
    # |* * *|* * *||* * *|
    # |* * *1* * *||* * *|
    # |* * *|* * *||* * *|
    # +-----------++-----+
    elif are_close == ProximitiesConfigurations.PROXIMITYCONFIGURATION_8:
        # token1 esta a la izquierda
        return token1.denominator == token2.denominator
    elif are_close == -ProximitiesConfigurations.PROXIMITYCONFIGURATION_8:
        # token1 esta a la derecha
        return token1.denominator == token2.denominator

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
    elif are_close == ProximitiesConfigurations.PROXIMITYCONFIGURATION_9:
        # token1 esta arriba
        return token1.numerator == token2.numerator
    elif are_close == -ProximitiesConfigurations.PROXIMITYCONFIGURATION_9:
        # token1 esta abajo
        return token1.numerator == token2.numerator

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
    elif are_close == ProximitiesConfigurations.PROXIMITYCONFIGURATION_10:
        # token1 esta arriba
        return token1.numerator == token1.denominator == token2.denominator
    elif are_close == -ProximitiesConfigurations.PROXIMITYCONFIGURATION_10:
        # token1 esta abajo
        return token1.numerator == token2.numerator == token2.denominator

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
    elif are_close == ProximitiesConfigurations.PROXIMITYCONFIGURATION_11:
        # token1 esta arriba
        return token1.denominator == token2.numerator
    elif are_close == -ProximitiesConfigurations.PROXIMITYCONFIGURATION_11:
        # token1 esta abajo
        return token1.numerator == token2.denominator

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
    elif are_close == ProximitiesConfigurations.PROXIMITYCONFIGURATION_12:
        # token1 esta arriba
        return token1.denominator == token2.numerator
    elif are_close == -ProximitiesConfigurations.PROXIMITYCONFIGURATION_12:
        # token1 esta abajo
        return token1.numerator == token2.denominator

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
    elif are_close == ProximitiesConfigurations.PROXIMITYCONFIGURATION_13:
        # token1 esta arriba
        return token1.denominator == token2.numerator == token2.denominator
    elif are_close == -ProximitiesConfigurations.PROXIMITYCONFIGURATION_13:
        # token1 esta abajo
        return token1.numerator == token1.denominator == token2.denominator

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
    elif are_close == ProximitiesConfigurations.PROXIMITYCONFIGURATION_14:
        # token1 esta arriba
        return token1.denominator == token2.denominator
    elif are_close == -ProximitiesConfigurations.PROXIMITYCONFIGURATION_14:
        # token1 esta abajo
        return token1.denominator == token2.denominator
    else:
        return False


class LightToken:
    """
    Esta clase representa una ficha de domino

    Parametros
    ----------
    numerator: int
        Entero que representa la parte superior o derecha de la fichas.
        denominator(int): Entero que representa la parte inferior o izquierda de la fichas
    pos: Tuple[int, int]
        Dupla de enteros que representa la posicion de la ficha, primera
        componente es posicion en fila y segunda componente es posicion en columna
    orientation: int
        Entero que representa la orientacion de la ficha, puede ser
        TokenOrientations.HORIZONTAL o TokenOrientations.VERTICAL
    """

    def __init__(
        self,
        numerator: int,
        denominator: int,
        pos: List[int] = [0, 0],
        orientation: TokenOrientations = TokenOrientations.VERTICAL,
    ) -> None:
        self.numerator = numerator
        self.denominator = denominator

        self.position = pos
        self.orientation = orientation

    def is_vertical(self) -> bool:
        """
        Este metodo retorna True si la ficha esta orientada de forma vertical,
        False en caso contrario
        """
        return self.orientation == TokenOrientations.VERTICAL

    def is_horizontal(self) -> bool:
        """
        Este metodo retorna True si la ficha esta orientada de forma
        horizontal, False en caso contrario
        """
        return self.orientation == TokenOrientations.HORIZONTAL

    def are_concatenable(self, token: Union["LightToken", "Token"]) -> bool:
        """
        Este metodo retorna True si dos fichas pueden ser compatibles, False
        en caso contrario
        """
        # dos fichas pueden ser compatibles si el valo de los denominadores o
        # numeradores coinciden
        if self.numerator == token.numerator:
            return True
        elif self.numerator == token.denominator:
            return True
        elif self.denominator == token.numerator:
            return True
        elif self.denominator == token.denominator:
            return True
        else:
            return False

    def are_compatible(self, token: Union["LightToken", "Token"]) -> bool:
        """
        Este metodo chequea si la ficha es compatible con alguna otra
        """
        # Dos fichas son compatibles si se pueden poner un despues de la otra
        # siquiendo las reglas del domino, es decir, estan bien conectadas
        return _are_compatible(self, token)


class Token(LightToken, Writable):
    """
    Esta clase representa una ficha de domino que puede ser mostrada en
    pantalla

    Parametros
    ----------
    numerator(int): Entero que representa la parte superior o derecha de la
        fichas
    denominator(int): Entero que representa la parte inferior o izquierda de la
        fichas
    pos((int, int)): Dupla de enteros que representa la posicion de la ficha,
        primera componente es posicion en fila y segunda componente es posicion
        en columna
    orientation(int): Entero que representa la orientacion de la ficha, puede
        ser TokenOrientations.HORIZONTAL o TokenOrientations.VERTICAL
    """

    def __init__(self, *args, **kwargs) -> None:
        LightToken.__init__(self, *args, **kwargs)

        # se obtiene la representacion en string de la ficha
        string = self.getString()

        # se llama al inicializador de Writable para poder mostrar en pantalla
        Writable.__init__(self, string, self.position)

    def getString(self) -> List[str]:
        """
        Este metodo obtiene la representacion en string de la ficha
        """
        string: List[str] = []

        if self.orientation == TokenOrientations.VERTICAL:
            string.append(TOKENS_PARTS[TokenOrientations.VERTICAL]["head"])
            string.extend(TOKENS_PARTS[TokenOrientations.VERTICAL][self.numerator])
            string.append(TOKENS_PARTS[TokenOrientations.VERTICAL]["middle"])
            string.extend(TOKENS_PARTS[TokenOrientations.VERTICAL][self.denominator])
            string.append(TOKENS_PARTS[TokenOrientations.VERTICAL]["head"])
        else:
            for i in range(5):
                s = TOKENS_PARTS[TokenOrientations.HORIZONTAL]["head"][i]

                s += TOKENS_PARTS[TokenOrientations.HORIZONTAL][self.numerator][0][i]
                s += TOKENS_PARTS[TokenOrientations.HORIZONTAL]["space"][i]
                s += TOKENS_PARTS[TokenOrientations.HORIZONTAL][self.numerator][1][i]
                s += TOKENS_PARTS[TokenOrientations.HORIZONTAL]["space"][i]
                s += TOKENS_PARTS[TokenOrientations.HORIZONTAL][self.numerator][2][i]

                s += TOKENS_PARTS[TokenOrientations.HORIZONTAL]["middle"][i]

                s += TOKENS_PARTS[TokenOrientations.HORIZONTAL][self.denominator][0][i]
                s += TOKENS_PARTS[TokenOrientations.HORIZONTAL]["space"][i]
                s += TOKENS_PARTS[TokenOrientations.HORIZONTAL][self.denominator][1][i]
                s += TOKENS_PARTS[TokenOrientations.HORIZONTAL]["space"][i]
                s += TOKENS_PARTS[TokenOrientations.HORIZONTAL][self.denominator][2][i]

                s += TOKENS_PARTS[TokenOrientations.HORIZONTAL]["head"][i]

                string.append(s)

        return string

    def reflect(self) -> None:
        """
        Este metodo invierte la ficha.
        """
        self.numerator, self.denominator = self.denominator, self.numerator
        self.text = self.getString()

    def rotate(self) -> None:
        """
        Este metodo cambia la orientacion de la ficha.
        """
        if self.orientation == TokenOrientations.VERTICAL:
            self.orientation = TokenOrientations.HORIZONTAL
        else:
            self.orientation = TokenOrientations.VERTICAL

        self.text = self.getString()
