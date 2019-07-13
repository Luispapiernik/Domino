from random import choice


class Player(object):
    def __init__(self, tokens):
        self.tokens = tokens

        self.skippedTurns = 0
        self.stolenTokens = 0

    def getInfo(self):
        information = ['Tokens: %d' % len(self.tokens),
                       'Stolen Tokens: %d' % self.stolenTokens,
                       'Skipped Turns: %d' % self.skippedTurns]

        return information

    def getToken(self, numerator, denominator):
        for token in self.tokens:
            if token.numerator == numerator and \
                    token.denominator == denominator:
                self.tokens.remove(token)
                return token


class Human(Player):
    pass


class Computer(Player):
    def makeMove(self, tokens, right, left):
        # si no hay fichas en el tablero, se elijira una al azar
        if len(tokens) == 0:
            token = choice(self.tokens)
            return token

        # si hay fichas en el tablero, se debe verificar si se pueden hacer
        # alguna jugada
        posibleTokens = []

        for token in self.tokens:
            if token.areConcatenable(right) or \
                    token.areConcatenable(left):
                posibleTokens.append(token)

        # si no hay jugadas disponibles
        if len(posibleTokens) == 0:
            self.skippedTurns += 1

            return None

        # se escoge una ficha al azar entre todas las posibilidades
        token = choice(posibleTokens)

        return token
