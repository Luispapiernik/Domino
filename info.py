import curses as c

from utils import *
from baseObjects import Writable, BaseContainer


class GameInfo(BaseContainer):
    def __init__(self, maxHeight, maxWidth):
        window = c.newwin(maxHeight - 2, 28, 1, maxWidth - 29)

        super(GameInfo, self).__init__(window)

        self.addElements(Writable(['PLAYER'], [1, getCenterColumn('PLAYER', self.height) - 2]), False)
        self.addElements(Writable(['-' * 28], [2, 1]))

        self.addElements(Writable(['COMPUTER'], [getCenterRow(self.height), getCenterColumn('COMPUTER', self.height) - 2]))
        self.addElements(Writable(['-' * 28], [getCenterRow(self.height) + 1, 1]))

    def updateInfo(self, info, player=PLAYER):
        if player == PLAYER:
            for i in range(len(info)):
                self.addElements(Writable([info[i]], [4 + i, 1]))

        if player == COMPUTER:
            for i in range(len(info)):
                self.addElements(Writable([info[i]], [getCenterRow(self.height) + 3 + i, 1]))
