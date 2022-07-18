from random import choice
from typing import List, Optional

from domino.tokens import Token


class Player:
    """
    Esta clase representa a un jugador.

    Parametros
    ----------
    tokens: List[Token]
        Lista con las fichas del jugador.
    """

    def __init__(self, tokens: List[Token]) -> None:
        self.tokens = tokens

        self.skipped_turns = 0
        self.stolen_tokens = 0

    def get_info(self) -> List[str]:
        """
        Este metodo retorna toda la informacion asociada con un jugador.
        """
        information = [
            "Tokens: %d" % len(self.tokens),
            "Stolen Tokens: %d" % self.stolen_tokens,
            "Skipped Turns: %d" % self.skipped_turns,
        ]

        return information

    def get_token(self, numerator: int, denominator: int) -> Token:
        """
        Este metodo elimina y retorna una ficha del jugador.

        Parameters
        ----------
        numerator: int
            Valor del numerador de la ficha a eliminar.
        denominator: int
            Valor del denominador de la ficha a eliminar.
        """
        for token in self.tokens:
            if token.numerator == numerator and token.denominator == denominator:
                self.tokens.remove(token)
                return token


class Human(Player):
    """
    Esta clase representa a un jugador humano.
    """

    pass


class Computer(Player):
    """
    Esta clase representa a la maquina.
    """

    def make_move(
        self, tokens: List[Token], right: Token, left: Token
    ) -> Optional[Token]:
        """
        Este metodo realiza la jugada de la maquina.

        Parameters
        ----------
        tokens: List[Token]
            Lista con las fichas que han sido jugadas.
        right: Token
            Representa la ultima ficha jugada en uno de los lados del domino.
        left: Token
            Representa la ultima ficha jugada en el lado restante del domino.

        Returns
        -------
        out: Optional[Token]
            Retorna una ficha a jugar, retorna None si no ha jugadas posibles
        """
        # si no hay fichas en el tablero, se elijira una al azar entre las
        # fichas propias
        if len(tokens) == 0:
            token = choice(self.tokens)
            return token

        # si hay fichas en el tablero, se debe verificar si se pueden hacer
        # alguna jugada
        posible_tokens = []

        # se itera sobre las fichas propias
        for token in self.tokens:
            if token.are_concatenable(right) or token.are_concatenable(left):
                posible_tokens.append(token)

        # si no hay jugadas disponibles
        if len(posible_tokens) == 0:
            self.skipped_turns += 1

            return None

        # se escoge una ficha al azar entre todas las posibles jugadas
        token = choice(posible_tokens)

        return token
