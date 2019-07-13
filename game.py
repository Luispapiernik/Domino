from random import randint, choice
import curses as c

from utils import *
from baseObjects import *

from tokens import Token
from boards import Table, PlayerTable
from info import GameInfo

from players import Human, Computer


class Game(BaseContainer):
    """
    Esta clase representa al juego
    """
    def __init__(self, height, width, tokens_per_player=9, max_number=9):
        window = c.newwin(height, width, 0, 0)

        super(Game, self).__init__(window)

        self.table = Table(height, width)
        self.playerTable = PlayerTable(height, width)
        self.info = GameInfo(height, width)

        # se agregan los tableros
        self.addElements(self.table)
        self.addElements(self.playerTable)
        self.addElements(self.info, False)

        # se crean las fichas del juego
        self.tokens = [Token(i, j) for i in range(max_number + 1)
                       for j in range(i, max_number + 1)]

        if self.getFirst() == PLAYER:
            self.player = Human(self.getPlayerTokens(tokens_per_player))
            self.computer = Computer(self.getPlayerTokens(tokens_per_player))
            self.turn = PLAYER
        else:
            self.computer = Computer(self.getPlayerTokens(tokens_per_player))
            self.player = Human(self.getPlayerTokens(tokens_per_player))
            self.turn = COMPUTER

        self.turn = PLAYER

        for element in self.player.tokens:
            self.playerTable.addElements(element)

    def getFirst(self):
        """
        Esta funcion decide quien va primero
        """
        return choice([PLAYER, COMPUTER])

    def getPlayerTokens(self, tokenNumber):
        tokens = []

        while len(tokens) < tokenNumber:
            tokens.append(self.tokens.pop(randint(0, len(self.tokens) - 1)))
            tokens[-1].position = [1, 1 + 8 * (len(tokens) - 1)]

        return tokens

    @applyEvent(113, COVER)
    def inputHandler(self, char):
        if char == 9:  # TAB
            if not self.table.isLocatingToken:
                self.linter += 1
        if char == 112:  # p
            self.player.skippedTurns += 1
            self.turn = COMPUTER
        else:
            pass

        self.linter %= self.linterableObjects

        # se maneja el turno del jugador
        if self.turn == PLAYER:
            if self.linter == 1:  # ventana con las fichas del jugador
                token = self.playerTable.inputHandler(char)

                if (token is not None) and self.table.isValidToken(token):
                    token = self.player.getToken(token.numerator,
                                                 token.denominator)

                    self.playerTable.elements.remove((token, True))
                    self.playerTable.linterableObjects -= 1

                    self.linter = 0
                    self.table.locateToken(token)
            else:
                nextTurn = self.table.inputHandler(char)

                if nextTurn:
                    self.turn = COMPUTER
                    pass

        # turno de la maquina
        else:
            token = self.computer.makeMove(self.table.getTokens(),
                                           self.table.right,
                                           self.table.left)

            if (token is not None) and self.table.isValidToken(token):
                token = self.computer.getToken(token.numerator,
                                               token.denominator)

                self.table.locateComputerToken(token)

            self.turn = PLAYER

        self.info.updateInfo(self.player.getInfo(), player=PLAYER)
        self.info.updateInfo(self.computer.getInfo(), player=COMPUTER)

        return NONE

    def write(self):
        colorLinter = None
        for i in range(len(self.elements)):

            element, _ = self.elements[i]

            if i == self.linter:
                colorLinter = 2

            element.write(colorLinter)

            colorLinter = None
