import curses
from random import choice, randint
from typing import List

from domino.config import settings
from domino.container import BaseContainer
from domino.info import GameInfo
from domino.playerboard import PlayerTable
from domino.players import Computer, Human
from domino.schemas import Events, Key, Players
from domino.table import Table
from domino.tokens import Token
from domino.utils import apply_event


class Game(BaseContainer):
    """
    This class manages all game cycle and resources.

    Parameters
    ----------
    height: int
        This represents the window height.
    width: int
        This represents the window width.
    """

    def __init__(
        self,
        height: int,
        width: int,
    ) -> None:
        window = curses.newwin(height, width, 0, 0)

        self.linter: int
        super().__init__(window)

        # se crean los diferentes paneles que se mostraran en la ventana del
        # juego
        self.table = Table(height, width)
        self.player_table = PlayerTable(height, width)
        self.info = GameInfo(height, width)

        # se agregan los paneles a la ventana
        self.add_elements(self.table)
        self.add_elements(self.player_table)
        self.add_elements(self.info, False)

        # se crean las fichas del juego
        self.tokens = [
            Token(i, j)
            for i in range(settings.token_max_number + 1)
            for j in range(i, settings.token_max_number + 1)
        ]

        self.player = Human(self.get_player_tokens())
        self.computer = Computer(self.get_player_tokens())
        self.turn = self.get_first()

        # como se esta en proceso de desarrollo, el jugador siempre hara la
        # primera jugada, si se quita esta linea la probabilidad de que el
        # jugador vaya primero es de 50%
        self.turn = Players.PLAYER

        # se agregan las fichas del jugador al tablero del jugador
        for element in self.player.tokens:
            self.player_table.add_elements(element)

        # se actualiza la informacion de los jugadores
        self.info.init_info(self.player.get_info(), self.computer.get_info())

    def get_first(self) -> Players:
        """
        This method returns the player with the first turn.
        """
        return choice([Players.PLAYER, Players.COMPUTER])

    def get_player_tokens(self) -> List[Token]:
        """
        This method returns a given number of token from all the possible tokens.
        """
        tokens: List[Token] = []

        while len(tokens) < settings.tokens_per_player:
            # se van elijiendo fichas de forma aleatoria
            tokens.append(self.tokens.pop(randint(0, len(self.tokens) - 1)))
            # se posicionan las fichas de forma que esten en la misma fila y
            # de forma consecutiva
            tokens[-1].position = [1, 1 + 8 * (len(tokens) - 1)]

        return tokens

    def make_computer_play(self):
        # se obtiene jugada del computador, si token toma el valor de None
        # es porque no habia jugada disponible
        token = self.computer.make_move(
            self.table.get_tokens(), self.table.right, self.table.left
        )

        if (token is not None) and self.table.is_valid_token(token):
            # cuando la jugada es valida se obtiene la ficha
            token = self.computer.get_token(token.numerator, token.denominator)

            # se ubica la ficha del computador
            self.table.locate_computer_token(token)

        # se actualiza la informacion de la maquina
        self.info.update_info(self.computer.get_info(), player=Players.COMPUTER)

        # ahora es turno del jugador
        self.turn = Players.PLAYER

    # When the key "Q" is pressed
    @apply_event(113, Events.COVER)
    def input_handler(self, char: Key) -> Events:
        if char == 9 and not self.table.is_locating_token:  # TAB
            self.linter += 1
            # para que self.linter no tome valores no posibles
            self.linter %= self.linterable_objects
            return Events.NONE

        if self.turn == Players.PLAYER:
            # cuando se presiona la tecla p el jugador ha cedido el turno
            if char == 112:  # p
                self.player.skipped_turns += 1
                self.turn = Players.COMPUTER
                self.make_computer_play()
                return Events.NONE

            # si el panel en el que se esta es el de las fichas del jugador
            if self.linter == 1:
                # se obtiene la ficha, si token toma el valor de None es porque
                # el jugador no ha realizado ninguna jugada
                token = self.player_table.input_handler(char)

                # se revisa si la jugada es valida
                if (token is not None) and self.table.is_valid_token(token):
                    # cuando la jugada es valida se obtiene la ficha
                    token = self.player.get_token(token.numerator, token.denominator)

                    # la ficha ya no esta en el panel del jugador
                    self.player_table.elements.remove((token, True))
                    # hay una ficha menos
                    self.player_table.linterable_objects -= 1

                    # la ficha debe estar en el panel de las fichas jugadas
                    self.table.locate_token(token)

                    # se cambia al panel de las fichas jugadas, para iniciar
                    # el posicionamiento de la nueva ficha
                    self.linter = 0
            # si el panel es el de las fichas jugadas
            else:
                # se gestiona las operaciones del jugador en el panel de fichas
                # jugadas, si nextTurn toma el valor de True, es porque el
                # jugador ha terminado su jugada, es decir, ha posicionado una
                # ficha
                nextTurn = self.table.input_handler(char)

                if nextTurn:
                    self.turn = Players.COMPUTER

            # se actualiza la informacion del jugador
            self.info.update_info(self.player.get_info(), player=Players.PLAYER)

        if self.turn == Players.COMPUTER:
            self.make_computer_play()

    def write(self) -> None:
        """
        This method draws all on screen.
        """
        # color of the panel to be hightlighted
        color_linter = None
        for i in range(len(self.elements)):
            element, is_linterable = self.elements[i]

            if i == self.linter and is_linterable:
                color_linter = 2

            element.write(color_linter)
            color_linter = None
