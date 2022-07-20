import curses
from typing import List

from domino.config import settings
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
        # TODO: parametrize the dimensions of the window
        window = curses.newwin(
            max_height - 2,
            settings.info_window_width,
            1,
            max_width - settings.info_window_width - 1,
        )
        super().__init__(window)

        position = [1, get_center_column("PLAYER", self.width) - 2]
        self.add_elements(Writable("PLAYER", position), False)
        self.add_elements(Writable("-" * settings.info_window_width, [2, 1]))

        position = [
            get_center_row(self.height),
            get_center_column("COMPUTER", self.width) - 2,
        ]
        self.add_elements(Writable("COMPUTER", position))

        position = [get_center_row(self.height) + 1, 1]
        self.add_elements(Writable("-" * settings.info_window_width, position))

    def init_info(self, player_info: List[str], computer_info: List[str]) -> None:
        """
        This method initialize the information of every player.

        Parameters
        ----------
        player_info: List[str]
            Information asociated with the user.
        computer_info: List[str]
            Information asociated with the computer.
        """
        for i in range(len(player_info)):
            position = [4 + i, 1]
            self.add_elements(Writable(player_info[i], position))

        for i in range(len(computer_info)):
            position = [get_center_row(self.height) + 3 + i, 1]
            self.add_elements(Writable(computer_info[i], position))

    def update_info(self, info: List[str], player: Players = Players.PLAYER) -> None:
        """
        This method update the information of every player in the game.

        Parameters
        ----------
        info: List[str]
            New information associated with a given user.
        player: Players.PLAYER
            Player which information will be updated.
        """
        offset = 4
        if player == Players.COMPUTER:
            offset == 7

        for i in range(len(info)):
            self.elements[i + offset][0].text = [info[i]]
