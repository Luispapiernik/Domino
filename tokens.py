from utils import *
from baseObjects import Writable


def areClose(token1, token2):
    """
    """
    verticalDiference = token1.position[0] - token2.position[0]
    horizontalDiference = token1.position[1] - token2.position[1]

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
    if token1.position[1] == token2.position[1]:
        if token1.isVertical() and token2.isVertical():
            # token1 esta abajo
            if verticalDiference == 9:
                return -PROXIMITYCONFIGURACION_1
            # token2 esta abajo
            if verticalDiference == -9:
                return PROXIMITYCONFIGURACION_1

    # configuracion de cercania 2
    # +-----------++-----------+
    # |* * *|* * *||* * *|* * *|
    # |* * *1* * *||* * *2* * *|
    # |* * *|* * *||* * *|* * *|
    # +-----------++-----------+
    if token1.position[0] == token2.position[0]:
        if token1.isHorizontal() and token2.isHorizontal():
            # token1 esta a la derecha
            if horizontalDiference == 13:
                return -PROXIMITYCONFIGURACION_2
            # token2 esta a la derecha
            if horizontalDiference == -13:
                return PROXIMITYCONFIGURACION_2

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
        if horizontalDiference == 7:
            return -PROXIMITYCONFIGURACION_3
        # token 2 a la derecha
        if horizontalDiference == -7:
            return PROXIMITYCONFIGURACION_3

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
    if abs(verticalDiference) == 2:
        # token1 el de la derecha
        if horizontalDiference == 7:
            return -PROXIMITYCONFIGURACION_4
        # token2 a la derecha
        if horizontalDiference == -7:
            return PROXIMITYCONFIGURACION_4

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
    if abs(verticalDiference) == 4:
        # token1 a la derecha
        if horizontalDiference == 7:
            return -PROXIMITYCONFIGURACION_5
        # token2 a la derecha
        if horizontalDiference == -7:
            return PROXIMITYCONFIGURACION_5

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
        if horizontalDiference == 13:
            return -PROXIMITYCONFIGURACION_6
        if horizontalDiference == -13:
            return PROXIMITYCONFIGURACION_6

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
    if abs(verticalDiference) == 2:
        # token1 a la derecha
        if horizontalDiference == 13:
            return -PROXIMITYCONFIGURACION_7
        # token2 a la derecha
        if horizontalDiference == -13:
            return PROXIMITYCONFIGURACION_7

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
    if abs(verticalDiference) == 4:
        # token1 a la derecha
        if horizontalDiference == 13:
            return -PROXIMITYCONFIGURACION_8
        # token2 a la derecha
        if horizontalDiference == -13:
            return PROXIMITYCONFIGURACION_8

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
        if verticalDiference == 5:
            return -PROXIMITYCONFIGURACION_9
        # token1 abajo
        if verticalDiference == -5:
            return PROXIMITYCONFIGURACION_9

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
    if abs(horizontalDiference) == 3:
        # token1 abajo
        if verticalDiference == 5:
            return -PROXIMITYCONFIGURACION_10
        # token2 abajo
        if verticalDiference == -5:
            return PROXIMITYCONFIGURACION_10

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
    if abs(horizontalDiference) == 6:
        # token1 abajo
        if verticalDiference == 5:
            return -PROXIMITYCONFIGURACION_11
        # token2 abajo
        if verticalDiference == -5:
            return PROXIMITYCONFIGURACION_11

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
        if verticalDiference == 9:
            return -PROXIMITYCONFIGURACION_12
        # token2 abajo
        if verticalDiference == -9:
            return PROXIMITYCONFIGURACION_12

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
    if abs(horizontalDiference) == 3:
        # token1 abajo
        if verticalDiference == 9:
            return -PROXIMITYCONFIGURACION_13
        # token2 abajo
        if verticalDiference == -9:
            return PROXIMITYCONFIGURACION_13

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
    if abs(horizontalDiference) == 6:
        # token1 abajo
        if verticalDiference == 9:
            return -PROXIMITYCONFIGURACION_14
        # token2 abajo
        if verticalDiference == -9:
            return PROXIMITYCONFIGURACION_14

    return False


def getFreeSide(token1, token2):
    """Esta funcion retorna el lado libre de token1 una vez se ha conectado
       con token2
    """
    are_close = areClose(token1, token2)

    if are_close == PROXIMITYCONFIGURACION_1:
        return NUMERATOR
    elif are_close == -PROXIMITYCONFIGURACION_1:
        return DENOMINATOR
    elif are_close == PROXIMITYCONFIGURACION_2:
        return NUMERATOR
    elif are_close == -PROXIMITYCONFIGURACION_2:
        return DENOMINATOR
    elif are_close == PROXIMITYCONFIGURACION_3:
        return DENOMINATOR
    elif are_close == -PROXIMITYCONFIGURACION_3:
        return DENOMINATOR
    elif are_close == PROXIMITYCONFIGURACION_4:
        return BOTH
    elif are_close == -PROXIMITYCONFIGURACION_4:
        return DENOMINATOR
    elif are_close == PROXIMITYCONFIGURACION_5:
        return NUMERATOR
    elif are_close == -PROXIMITYCONFIGURACION_5:
        return DENOMINATOR
    elif are_close == PROXIMITYCONFIGURACION_6:
        return NUMERATOR
    elif are_close == -PROXIMITYCONFIGURACION_6:
        return DENOMINATOR
    elif are_close == PROXIMITYCONFIGURACION_7:
        return NUMERATOR
    elif are_close == -PROXIMITYCONFIGURACION_7:
        return BOTH
    elif are_close == PROXIMITYCONFIGURACION_8:
        return NUMERATOR
    elif are_close == -PROXIMITYCONFIGURACION_8:
        return NUMERATOR
    elif are_close == PROXIMITYCONFIGURACION_9:
        return DENOMINATOR
    elif are_close == -PROXIMITYCONFIGURACION_9:
        return DENOMINATOR
    elif are_close == PROXIMITYCONFIGURACION_10:
        return BOTH
    elif are_close == -PROXIMITYCONFIGURACION_10:
        return DENOMINATOR
    elif are_close == PROXIMITYCONFIGURACION_11:
        return NUMERATOR
    elif are_close == -PROXIMITYCONFIGURACION_11:
        return DENOMINATOR
    elif are_close == PROXIMITYCONFIGURACION_12:
        return NUMERATOR
    elif are_close == -PROXIMITYCONFIGURACION_12:
        return DENOMINATOR
    elif are_close == PROXIMITYCONFIGURACION_13:
        return NUMERATOR
    elif are_close == -PROXIMITYCONFIGURACION_13:
        return BOTH
    elif are_close == PROXIMITYCONFIGURACION_14:
        return NUMERATOR
    elif are_close == -PROXIMITYCONFIGURACION_14:
        return NUMERATOR
    else:
        return False


def _areCompatible(token1, token2):
    """
    """
    are_close = areClose(token1, token2)

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
    if are_close == PROXIMITYCONFIGURACION_1:
        # token1 esta arriba
        return token1.denominator == token2.numerator
    elif are_close == -PROXIMITYCONFIGURACION_1:
        # token1 esta abajo
        return token1.numerator == token2.denominator

    # +-----------++-----------+
    # |* * *|* * *||* * *|* * *|
    # |* * *1* * *||* * *2* * *|
    # |* * *|* * *||* * *|* * *|
    # +-----------++-----------+
    elif are_close == PROXIMITYCONFIGURACION_2:
        # token1 esta a la izquierda
        return token1.denominator == token2.denominator
    elif are_close == -PROXIMITYCONFIGURACION_2:
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
    elif are_close == PROXIMITYCONFIGURACION_3:
        # token1 esta a la izquierda
        return token1.numerator == token2.numerator
    elif are_close == -PROXIMITYCONFIGURACION_3:
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
    elif are_close == PROXIMITYCONFIGURACION_4:
        # token1 esta a la izquierda
        return token1.numerator == token1.denominator == token2.numerator
    elif are_close == -PROXIMITYCONFIGURACION_4:
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
    elif are_close == PROXIMITYCONFIGURACION_5:
        # token1 esta a la izquierda
        return token1.denominator == token2.numerator
    elif are_close == -PROXIMITYCONFIGURACION_5:
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
    elif are_close == PROXIMITYCONFIGURACION_6:
        # token1 esta a la izquierda
        return token1.denominator == token2.numerator
    elif are_close == -PROXIMITYCONFIGURACION_6:
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
    elif are_close == PROXIMITYCONFIGURACION_7:
        # token1 esta a la izquierda
        return token1.denominator == token2.numerator == token2.denominator
    elif are_close == -PROXIMITYCONFIGURACION_7:
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
    elif are_close == PROXIMITYCONFIGURACION_8:
        # token1 esta a la izquierda
        return token1.denominator == token2.denominator
    elif are_close == -PROXIMITYCONFIGURACION_8:
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
    elif are_close == PROXIMITYCONFIGURACION_9:
        # token1 esta arriba
        return token1.numerator == token2.numerator
    elif are_close == -PROXIMITYCONFIGURACION_9:
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
    elif are_close == PROXIMITYCONFIGURACION_10:
        # token1 esta arriba
        return token1.numerator == token1.denominator == token2.denominator
    elif are_close == -PROXIMITYCONFIGURACION_10:
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
    elif are_close == PROXIMITYCONFIGURACION_11:
        # token1 esta arriba
        return token1.denominator == token2.numerator
    elif are_close == -PROXIMITYCONFIGURACION_11:
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
    elif are_close == PROXIMITYCONFIGURACION_12:
        # token1 esta arriba
        return token1.denominator == token2.numerator
    elif are_close == -PROXIMITYCONFIGURACION_12:
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
    elif are_close == PROXIMITYCONFIGURACION_13:
        # token1 esta arriba
        return token1.denominator == token2.numerator == token2.denominator
    elif are_close == -PROXIMITYCONFIGURACION_13:
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
    elif are_close == PROXIMITYCONFIGURACION_14:
        # token1 esta arriba
        return token1.denominator == token2.denominator
    elif are_close == -PROXIMITYCONFIGURACION_14:
        # token1 esta abajo
        return token1.denominator == token2.denominator
    else:
        return False


class LightToken(object):
    def __init__(self, numerator, denominator, pos=[0, 0],
                 orientation=VERTICAL):
        self.numerator = numerator
        self.denominator = denominator

        self.position = pos
        self.orientation = orientation

    def __repr__(self):
        return str([(self.numerator, self.denominator), self.position])

    def isVertical(self):
        return self.orientation == VERTICAL

    def isHorizontal(self):
        return self.orientation == HORIZONTAL

    def areConcatenable(self, token):
        """
        Este metodo retorna True si dos fichas pueden ser compatibles
        """
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

    def areCompatible(self, token):
        """
        Este metodo chequea si la ficha es compatible con alguna otra, son
        fichas compatibles si se pueden poner un despues de la otra siquiendo
        las reglas del domino
        """
        return _areCompatible(self, token)


class Token(LightToken, Writable):
    def __init__(self, *args, **kwargs):

        LightToken.__init__(self, *args, **kwargs)

        string = self.getString()

        Writable.__init__(self, string, self.position)

    def getString(self):
        """
        Este metodo obtiene la representacion en string de la ficha
        """
        string = []

        if self.orientation == VERTICAL:
            string.append(TOKENS_PARTS[VERTICAL]['head'])
            string.extend(TOKENS_PARTS[VERTICAL][self.numerator])
            string.append(TOKENS_PARTS[VERTICAL]['middle'])
            string.extend(TOKENS_PARTS[VERTICAL][self.denominator])
            string.append(TOKENS_PARTS[VERTICAL]['head'])
        else:
            for i in range(5):
                s = TOKENS_PARTS[HORIZONTAL]['head'][i]

                s += TOKENS_PARTS[HORIZONTAL][self.numerator][0][i]
                s += TOKENS_PARTS[HORIZONTAL]['space'][i]
                s += TOKENS_PARTS[HORIZONTAL][self.numerator][1][i]
                s += TOKENS_PARTS[HORIZONTAL]['space'][i]
                s += TOKENS_PARTS[HORIZONTAL][self.numerator][2][i]

                s += TOKENS_PARTS[HORIZONTAL]['middle'][i]

                s += TOKENS_PARTS[HORIZONTAL][self.denominator][0][i]
                s += TOKENS_PARTS[HORIZONTAL]['space'][i]
                s += TOKENS_PARTS[HORIZONTAL][self.denominator][1][i]
                s += TOKENS_PARTS[HORIZONTAL]['space'][i]
                s += TOKENS_PARTS[HORIZONTAL][self.denominator][2][i]

                s += TOKENS_PARTS[HORIZONTAL]['head'][i]

                string.append(s)

        return string

    def reflect(self):
        """
        Este metodo invierte la ficha
        """
        self.numerator, self.denominator = self.denominator, self.numerator
        self.text = self.getString()

    def rotate(self):
        """
        Este metodo cambia la orientacion de la ficha
        """
        if self.orientation == VERTICAL:
            self.orientation = HORIZONTAL
        else:
            self.orientation = VERTICAL

        self.text = self.getString()
