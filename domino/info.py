import curses as c

from domino.baseObjects import BaseContainer, Writable
from domino.utils import *


class GameInfo(BaseContainer):
    """
    Esta clase se encarga de mostrar la informacion de cada usuario en pantalla
    """

    def __init__(self, maxHeight, maxWidth):
        window = c.newwin(maxHeight - 2, 28, 1, maxWidth - 29)

        super().__init__(window)

        position = [1, getCenterColumn("PLAYER", self.height) - 2]
        self.addElements(Writable(["PLAYER"], position), False)

        self.addElements(Writable(["-" * 28], [2, 1]))

        position = [
            getCenterRow(self.height),
            getCenterColumn("COMPUTER", self.height) - 2,
        ]
        self.addElements(Writable(["COMPUTER"], position))

        position = [getCenterRow(self.height) + 1, 1]
        self.addElements(Writable(["-" * 28], position))

    def initInfo(self, playerInfo, computerInfo):
        """
        Este metodo inicializa la informacion de cada jugador
        """
        for i in range(len(playerInfo)):
            position = [4 + i, 1]
            self.addElements(Writable([playerInfo[i]], position))

        for i in range(len(computerInfo)):
            position = [getCenterRow(self.height) + 3 + i, 1]
            self.addElements(Writable([computerInfo[i]], position))

    def updateInfo(self, info, player=PLAYER):
        """
        Este metodo actualiza la informacion de cada jugador
        """
        if player == PLAYER:
            for i in range(len(info)):
                self.elements[i + 4][0].text = [info[i]]

        if player == COMPUTER:
            for i in range(len(info)):
                self.elements[i + 7][0].text = [info[i]]
