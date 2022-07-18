import curses
from typing import List

from domino.container import BaseContainer
from domino.schemas import Players
from domino.utils import get_center_column, get_center_row
from domino.writable import Writable


class GameInfo(BaseContainer):
    """
    This class show player and computer information on screen.

    Parameters
    ----------
    max_height, max_width: int
        Dimensions of the entire screen.
    """

    def __init__(self, max_height: int, max_width: int) -> None:
        window = curses.newwin(max_height - 2, 28, 1, max_width - 29)

        super().__init__(window)

        position = [1, get_center_column("PLAYER", self.height) - 2]
        self.add_elements(Writable("PLAYER", position), False)
        self.add_elements(Writable("-" * 28, [2, 1]))

        position = [
            get_center_row(self.height),
            get_center_column("COMPUTER", self.height) - 2,
        ]
        self.add_elements(Writable("COMPUTER", position))

        position = [get_center_row(self.height) + 1, 1]
        self.add_elements(Writable("-" * 28, position))

    def init_info(self, player_info: List[str], computer_info: List[str]) -> None:
        """
        This method initialize the information of every player.
        """
        for i in range(len(player_info)):
            position = [4 + i, 1]
            self.add_elements(Writable(player_info[i], position))

        for i in range(len(computer_info)):
            position = [get_center_row(self.height) + 3 + i, 1]
            self.add_elements(Writable(computer_info[i], position))

    def update_info(self, info: List[str], player: Players = Players.PLAYER) -> None:
        """
        This method update the information of every player.
        """
        if player == Players.PLAYER:
            for i in range(len(info)):
                self.elements[i + 4][0].text = [info[i]]

        if player == Players.COMPUTER:
            for i in range(len(info)):
                self.elements[i + 7][0].text = [info[i]]
