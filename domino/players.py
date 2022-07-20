from random import choice
from typing import List, Optional

from domino.tokens import Token


class Player:
    """
    This class represent a player.

    Parameters
    ----------
    tokens: List[Token]
        Token list of the player.
    """

    def __init__(self, tokens: List[Token]) -> None:
        self.tokens = tokens

        self.skipped_turns = 0
        self.stolen_tokens = 0

    def get_info(self) -> List[str]:
        """
        This method returns all the information associated with the user.
        """
        information = [
            "Tokens: %d" % len(self.tokens),
            "Stolen Tokens: %d" % self.stolen_tokens,
            "Skipped Turns: %d" % self.skipped_turns,
        ]
        return information

    def get_token(self, numerator: int, denominator: int) -> Optional[Token]:
        """
        This method removes and returns a player token.

        Parameters
        ----------
        numerator: int
            Numerator of the token to remove.
        denominator: int
            Denominator of the token to remove.
        """
        for token in self.tokens:
            if token.numerator == numerator and token.denominator == denominator:
                self.tokens.remove(token)
                return token
        return None


class Human(Player):
    """
    This class represents a human player.
    """

    ...


class Computer(Player):
    """
    This class represents the computer.
    """

    def make_move(
        self, tokens: List[Token], right: Token, left: Token
    ) -> Optional[Token]:
        """
        This method play a computer turn.

        Parameters
        ----------
        tokens: List[Token]
            List of tokens played during all the game.
        right, left: Token
            References to the lasts token played to both sides of the game.

        Returns
        -------
        out: Optional[Token]
            Token to be played, None in case of non possible options.
        """
        # si no hay fichas en el tablero, se elijira una al azar entre las
        # fichas propias
        if tokens == []:
            return choice(self.tokens)

        # si hay fichas en el tablero, se debe verificar si se pueden hacer
        # alguna jugada
        posible_tokens = []
        for token in self.tokens:
            if token.are_concatenable(right) or token.are_concatenable(left):
                posible_tokens.append(token)

        # si no hay jugadas disponibles
        if posible_tokens == []:
            self.skipped_turns += 1
            return None

        # se escoge una ficha al azar entre todas las posibles jugadas
        return choice(posible_tokens)
