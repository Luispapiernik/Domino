from __future__ import division

import curses as c

from utils import *
from baseObjects import BaseContainer
from tokens import LightToken, getFreeSide


class Board(BaseContainer):
    def __init__(self, window, verticalScrollable=True,
                 horizontalScrollable=True):

        super(Board, self).__init__(window)

        self.verticalScrollable = verticalScrollable
        self.horizontalScrollable = horizontalScrollable

    def inputHandler(self, char):
        # manejando scrolling
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
    def __init__(self, maxHeight, maxWidth):
        window = c.newwin(maxHeight - 13, maxWidth - 30, 1, 1)

        super(Table, self).__init__(window)

        self.isLocatingToken = False
        self.linter = -1

        self.right = None
        self.left = None

    def getTokens(self):
        tokens = []

        for token, _ in self.elements:
            tokens.append(LightToken(token.numerator, token.denominator))

        tokens.append

        return tokens

    def isValidPosition(self):
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

        if char == 10:  # ENTER
            if self.isLocatingToken:
                if self.isValidPosition():
                    self.isLocatingToken = False
                    return True

        elif char == 116:
            self.elements[self.linter][0].rotate()
        else:
            pass

        if self.isLocatingToken:
            if char == 259:  # UP
                self.elements[self.linter][0].position[0] += 1
            if char == 258:  # DOWN
                self.elements[self.linter][0].position[0] -= 1
            if char == 260:  # RIGHT
                self.elements[self.linter][0].position[1] += 1
            if char == 261:  # LEFT
                self.elements[self.linter][0].position[1] -= 1

            # i j k l - 105 106 107 108
            if char == 119:  # w
                self.elements[self.linter][0].position[0] -= 1
            if char == 115:  # s
                self.elements[self.linter][0].position[0] += 1
            if char == 97:  # a
                self.elements[self.linter][0].position[1] -= 1
            if char == 100:  # d
                self.elements[self.linter][0].position[1] += 1

        return False

    def locateToken(self, token):
        # se posiciona la ficha en la mitad de la pantalla
        token.position[0] = self.height // 2 - 7 - self.zeroPosition[0]
        token.position[1] = self.width // 2 - 13 - self.zeroPosition[1]

        self.addElements(token, False)

        self.isLocatingToken = True
        self.linter += 1

    def locateComputerToken(self, token):
        self.addElements(token, False)
        self.linter += 1

        if token.areConcatenable(self.right):
            tempToken = self.right
        else:
            tempToken = self.left

        # se asigna la misma posicion a los tokens
        token.position = tempToken.position[:]

        # se orientan las fichas en la misma direccion
        if token.orientation != tempToken.orientation:
            token.rotate()

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
        isValid = False

        if self.right is None and self.left is None:
            isValid = True

        if self.right is not None:
            isValid = isValid or self.right.areConcatenable(lightToken)

        if self.left is not None:
            isValid = isValid or self.left.areConcatenable(lightToken)

        return isValid


class PlayerTable(Board):
    def __init__(self, maxHeight, maxWidth):
        window = c.newwin(11, maxWidth - 30, maxHeight - 12, 1)

        super(PlayerTable, self).__init__(window, verticalScrollable=False)

    def inputHandler(self, char):
        super(PlayerTable, self).inputHandler(char)

        if char == 97:  # a
            self.linter -= 1
        elif char == 100:  # d
            self.linter += 1
        elif char == 10:  # ENTER
            return self.elements[self.linter][0]
        else:
            pass

        self.linter %= self.linterableObjects
