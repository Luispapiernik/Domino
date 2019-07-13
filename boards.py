#! -*- coding: utf-8 -*-

from __future__ import division

import curses as c

from utils import *
from baseObjects import BaseContainer
from tokens import LightToken, getFreeSide


class Board(BaseContainer):
    """
    Esta clase representa un panel en donde se pueden ubicar fichas

    Parametros
    ----------
    window(Window): tablero en donde se dibujaran las fichas
    verticalScrollable(bool): Booleano que indica si las fichas se pueden mover
        en direccion vertical
    horizontalScrollable(bool): Booleano que indica si las fichas se pueden
        mover en direccion horizontal
    """
    def __init__(self, window, verticalScrollable=True,
                 horizontalScrollable=True):

        super(Board, self).__init__(window)

        self.verticalScrollable = verticalScrollable
        self.horizontalScrollable = horizontalScrollable

    def inputHandler(self, char):
        # el scrolling de las fichas se maneja con la variable zeroPosition que
        # es el corrimiento que se debe agregar a su posicion en el momento de
        # dibujarlas

        # manejando scrolling de las fichas
        if self.verticalScrollable:
            if char == 259:  # UP
                self.zeroPosition[0] -= 1
            if char == 258:  # DOWN
                self.zeroPosition[0] += 1
        if self.horizontalScrollable:
            if char == 260:  # RIGHT
                self.zeroPosition[1] -= 1
            if char == 261:  # LEFT
                self.zeroPosition[1] += 1
        if char == 114:  # r
            self.elements[self.linter][0].reflect()


class Table(Board):
    """
    Esta clase representa el panel en donde iran las fichas jugadas
    """
    def __init__(self, maxHeight, maxWidth):
        window = c.newwin(maxHeight - 13, maxWidth - 30, 1, 1)

        super(Table, self).__init__(window)

        # esta variable especifica si el jugador esta posicionando una ficha
        self.isLocatingToken = False
        self.linter = -1

        # estas variables indican las ultimas fichas jugadas en los extremos
        # del domino, right para un extremo y left para el extremo contrario
        # considere el siquiente caso [2 | 3][3 | 6][6 | 0][0 | 4] asi por
        # ejemplo right podria se [2 | 3] en tal caso left seria [0 | 4] pero
        # podria suceder que right sea [0 | 4] por tanto left seria  [2 | 3]
        # o en el siguiente caso [5 | 3] right y left toman el mismo valor,
        # esto es, [5 | 3]. Se inicializa su valor con None porque al principio
        # no hay fichas ubicadas en el tablero
        self.right = None
        self.left = None

    def getTokens(self):
        """
        Este metodo retorna todas las fichas que han sido jugadas, es decir,
        las que estan en el tablero
        """
        tokens = []

        # se itera sobre los elementos
        for token, _ in self.elements:
            tokens.append(LightToken(token.numerator, token.denominator))

        return tokens

    def isValidPosition(self):
        """
        Este metodo chequea si el jugador ha posicionado de forma correcta una
        ficha
        """
        # no se documenta porque debe ser escrito de forma mas elegante
        token = self.elements[self.linter][0]

        if self.right is None and self.left is None:
            self.right = LightToken(token.numerator, token.denominator)
            self.left = LightToken(token.numerator, token.denominator)

            self.right.orientation = token.orientation
            self.left.orientation = token.orientation

            self.right.position = token.position[:]
            self.left.position = token.position[:]

            return True

        if (self.right is not None) and self.right.areCompatible(token):
            tempToken, other = self.right, self.left
        elif (self.left is not None) and self.left.areCompatible(token):
            tempToken, other = self.left, self.right
        else:
            return False

        freeSide = getFreeSide(token, tempToken)

        tempToken.position = token.position[:]
        tempToken.orientation = token.orientation

        if token.numerator == token.denominator:
            tempToken.numerator = token.numerator
            tempToken.denominator = token.denominator
        elif freeSide == NUMERATOR:
            tempToken.numerator = token.numerator
            tempToken.denominator = -1
        elif freeSide == DENOMINATOR:
            tempToken.numerator = -1
            tempToken.denominator = token.denominator
        else:
            pass

        if len(self.elements) == 2:
            freeSide = getFreeSide(other, token)

            if other.numerator == other.denominator:
                pass
            elif freeSide == NUMERATOR:
                other.denominator = -1
            elif freeSide == DENOMINATOR:
                other.numerator = -1
            else:
                pass

        return True

    def inputHandler(self, char):
        super(Table, self).inputHandler(char)

        # si se presiona ENTER el jugador ha terminado de posicionar una ficha
        if char == 10:  # ENTER
            # en el caso que este posicionando una ficha
            if self.isLocatingToken:
                # se revisa si la posicion es valida
                if self.isValidPosition():
                    # se ha terminado el proceso de posicionamiento
                    self.isLocatingToken = False
                    # se debe cambiar de turno
                    return True
        elif char == 116:  # t
            # cuando se presiona la tecla t mientras se esta en el proceso de
            # seleccion de posicion para una ficha, esta ficha debe ser rotada
            if self.isLocatingToken:
                self.elements[self.linter][0].rotate()
        else:
            pass

        # se maneja el movimiento de las fichas mientras se esta seleccionando
        # posicion para una ficha
        if self.isLocatingToken:
            # para mover las fichas que estan ya posicionadas en el tablero
            if char == 259:  # UP
                self.elements[self.linter][0].position[0] += 1
            if char == 258:  # DOWN
                self.elements[self.linter][0].position[0] -= 1
            if char == 260:  # RIGHT
                self.elements[self.linter][0].position[1] += 1
            if char == 261:  # LEFT
                self.elements[self.linter][0].position[1] -= 1

            # i j k l - 105 106 107 108
            # para mover la ficha que se esta posicionando
            if char == 119:  # w
                self.elements[self.linter][0].position[0] -= 1
            if char == 115:  # s
                self.elements[self.linter][0].position[0] += 1
            if char == 97:  # a
                self.elements[self.linter][0].position[1] -= 1
            if char == 100:  # d
                self.elements[self.linter][0].position[1] += 1

        # no se cambia de turno
        return False

    def locateToken(self, token):
        """
        Este metodo inicia el proceso de posicionamiento de una ficha del
        jugador en pantalla
        """
        # se posiciona la ficha en la mitad de la pantalla
        token.position[0] = self.height // 2 - 7 - self.zeroPosition[0]
        token.position[1] = self.width // 2 - 13 - self.zeroPosition[1]

        # se agrega la ficha a los elementos propios
        self.addElements(token, False)

        # ahora el jugador tiene que posicionar la ficha en el lugar correcto
        self.isLocatingToken = True
        # se acaba de agregar un elemento mas, por tanto este numero debe
        # aumentar en uno
        self.linter += 1

    def locateComputerToken(self, token):
        """
        Este metodo posiciona la ficha del computador en el tablero
        """
        # se agrega la ficha a los elementos propios
        self.addElements(token, False)
        # se acaba de agregar un elemento mas, por tanto este numero debe
        # aumentar en uno
        self.linter += 1

        # se revisa a que extremo se deberia agregar la ficha
        if token.areConcatenable(self.right):
            tempToken = self.right
        else:
            tempToken = self.left

        # se asigna la misma posicion a los tokens
        token.position = tempToken.position[:]

        # se orientan las fichas en la misma direccion
        if token.orientation != tempToken.orientation:
            token.rotate()

        # lo siguiente no se documenta porque debe ser implementado de forma
        # mas clara
        if token.numerator == tempToken.numerator:
            token.reflect()

            if token.orientation == VERTICAL:
                token.position[0] -= 9
            else:
                token.position[1] -= 13
        elif token.denominator == tempToken.numerator:
            if token.orientation == VERTICAL:
                token.position[0] -= 9
            else:
                token.position[1] -= 13
        elif token.numerator == tempToken.denominator:
            if token.orientation == VERTICAL:
                token.position[0] += 9
            else:
                token.position[1] += 13
        else:
            token.reflect()

            if token.orientation == VERTICAL:
                token.position[0] += 9
            else:
                token.position[1] += 13

    def isValidToken(self, lightToken):
        """
        Este metodo retorna True si un token puede ser posicionado en pantalla

        lightToken(LightToken| Token): token que sera posicionado
        """
        # un token es valido si se puede conectar a cualquiera de las 2 ramas
        # del domino

        # somos no optimistas y de entrada suponemos que el token no se puede
        # conectar
        isValid = False

        # si no hay fichas en el tablero, entones cualquier token puede ser
        # posicionado en pantalla
        if self.right is None and self.left is None:
            isValid = True

        # cuando self.right tiene un valor se debe chequear si es concatenable
        # con la ficha pasada
        if self.right is not None:
            isValid = isValid or self.right.areConcatenable(lightToken)

        # en el caso de que la ficha no sea concatenable con self.right, se
        # debe chequear con self.left
        if self.left is not None:
            isValid = isValid or self.left.areConcatenable(lightToken)

        return isValid


class PlayerTable(Board):
    """
    Esta clase representa el tablero en donde se ubicaran las fichas del
    jugador

    Parametros
    ----------
    maxHeight(int): altura de la ventana
    maxWidth(int): ancho de la ventana
    """
    def __init__(self, maxHeight, maxWidth):
        window = c.newwin(11, maxWidth - 30, maxHeight - 12, 1)

        super(PlayerTable, self).__init__(window, verticalScrollable=False)

    def inputHandler(self, char):
        # el metodo inputHandler se encarga de manejar el scrolling de la ficha
        super(PlayerTable, self).inputHandler(char)

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

        self.linter %= self.linterableObjects
