import curses as c

from domino.baseObjects import BaseContainer, Writable
from domino.utils import *


class GameInfo(BaseContainer):
    """
    Esta clase se encarga de mostrar la informacion de cada usuario en pantalla
    """

    def __init__(self, max_height, max_width):
        window = c.newwin(max_height - 2, 28, 1, max_width - 29)

        super().__init__(window)

        position = [1, get_center_column("PLAYER", self.height) - 2]
        self.add_elements(Writable(["PLAYER"], position), False)

        self.add_elements(Writable(["-" * 28], [2, 1]))

        position = [
            get_center_row(self.height),
            get_center_column("COMPUTER", self.height) - 2,
        ]
        self.add_elements(Writable(["COMPUTER"], position))

        position = [get_center_row(self.height) + 1, 1]
        self.add_elements(Writable(["-" * 28], position))

    def init_info(self, player_info, computer_info):
        """
        Este metodo inicializa la informacion de cada jugador
        """
        for i in range(len(player_info)):
            position = [4 + i, 1]
            self.add_elements(Writable([player_info[i]], position))

        for i in range(len(computer_info)):
            position = [get_center_row(self.height) + 3 + i, 1]
            self.add_elements(Writable([computer_info[i]], position))

    def update_info(self, info, player=PLAYER):
        """
        Este metodo actualiza la informacion de cada jugador
        """
        if player == PLAYER:
            for i in range(len(info)):
                self.elements[i + 4][0].text = [info[i]]

        if player == COMPUTER:
            for i in range(len(info)):
                self.elements[i + 7][0].text = [info[i]]
