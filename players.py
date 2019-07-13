#! -*- coding: utf-8 -*-

from random import choice


class Player(object):
    """
    Esta clase representa a un jugador

    Parametros
    ----------
    tokens(list(Token)): lista con las fichas del jugador
    """
    def __init__(self, tokens):
        self.tokens = tokens

        self.skippedTurns = 0
        self.stolenTokens = 0

    def getInfo(self):
        """
        Este metodo retorna toda la informacion asociada con un jugador
        """
        information = ['Tokens: %d' % len(self.tokens),
                       'Stolen Tokens: %d' % self.stolenTokens,
                       'Skipped Turns: %d' % self.skippedTurns]

        return information

    def getToken(self, numerator, denominator):
        """
        Este metodo elimina y retorna una ficha del jugador

        Parametros
        ----------
        numerator(int): valor del numerador de la ficha a eliminar
        denominator(int): valor del denominador de la ficha a eliminar
        """
        for token in self.tokens:
            if token.numerator == numerator and \
                    token.denominator == denominator:
                self.tokens.remove(token)
                return token


class Human(Player):
    """
    Esta clase representa a un jugador humano
    """
    pass


class Computer(Player):
    """
    Esta clase representa a la maquina
    """
    def makeMove(self, tokens, right, left):
        """
        Este metodo realiza la jugada de la maquina

        Parametros
        ----------
        tokens(list(Token)): lista con las fichas que han sido jugadas
        right(Token): representa la ultima ficha jugada en uno de los lados
            del domino
        left(Token): representa la ultima ficha jugada en el lado restante del
            domino

        Returns
        -------
        Token | None: retorna una ficha a jugar, retorna None si no ha jugadas
            posibles
        """
        # si no hay fichas en el tablero, se elijira una al azar entre las
        # fichas propias
        if len(tokens) == 0:
            token = choice(self.tokens)
            return token

        # si hay fichas en el tablero, se debe verificar si se pueden hacer
        # alguna jugada
        posibleTokens = []

        # se itera sobre las fichas propias
        for token in self.tokens:
            if token.areConcatenable(right) or \
                    token.areConcatenable(left):
                posibleTokens.append(token)

        # si no hay jugadas disponibles
        if len(posibleTokens) == 0:
            self.skippedTurns += 1

            return None

        # se escoge una ficha al azar entre todas las posibles jugadas
        token = choice(posibleTokens)

        return token
