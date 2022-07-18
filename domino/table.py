import curses
from typing import List, Optional, Union

from domino.board import Board
from domino.schemas import Key, TokenOrientations, TokenParts
from domino.tokens import LightToken, Token, getFreeSide


class Table(Board):
    """
    Esta clase representa el panel en donde iran las fichas jugadas
    """

    def __init__(self, max_height: int, max_width: int) -> None:
        window = curses.newwin(max_height - 13, max_width - 30, 1, 1)

        super().__init__(window)

        # esta variable especifica si el jugador esta posicionando una ficha
        self.is_locating_token = False
        self.linter = -1

        # estas variables indican las ultimas fichas jugadas en los extremos
        # del domino, right para un extremo y left para el extremo contrario
        # considere el siquiente caso [2 | 3][3 | 6][6 | 0][0 | 4] asi por
        # ejemplo right podria se [2 | 3] en tal caso left seria [0 | 4] pero
        # podria suceder que right sea [0 | 4] por tanto left seria  [2 | 3]
        # o en el siguiente caso [5 | 3] right y left toman el mismo valor,
        # esto es, [5 | 3]. Se inicializa su valor con None porque al principio
        # no hay fichas ubicadas en el tablero
        self.right: Optional[Token] = None
        self.left: Optional[Token] = None

    def get_tokens(self) -> List[Token]:
        """
        Este metodo retorna todas las fichas que han sido jugadas, es decir,
        las que estan en el tablero
        """
        tokens = []

        # se itera sobre los elementos
        for token, _ in self.elements:
            tokens.append(LightToken(token.numerator, token.denominator))

        return tokens

    def is_valid_position(self) -> bool:
        """
        Este metodo chequea si el jugador ha posicionado de forma correcta una
        ficha
        """
        # no se documenta porque debe ser escrito de forma mas elegante
        token = self.elements[self.linter][0]

        if self.right is None and self.left is None:
            self.right = LightToken(token.numerator, token.denominator)
            self.left = LightToken(token.numerator, token.denominator)

            self.right.orientation = token.orientation
            self.left.orientation = token.orientation

            self.right.position = token.position[:]
            self.left.position = token.position[:]

            return True

        other: Token
        if (self.right is not None) and self.right.are_compatible(token):
            temporal_token, other = self.right, self.left
        elif (self.left is not None) and self.left.are_compatible(token):
            temporal_token, other = self.left, self.right
        else:
            return False

        freeSide = getFreeSide(token, temporal_token)

        temporal_token.position = token.position[:]
        temporal_token.orientation = token.orientation

        if token.numerator == token.denominator:
            temporal_token.numerator = token.numerator
            temporal_token.denominator = token.denominator
        elif freeSide == TokenParts.NUMERATOR:
            temporal_token.numerator = token.numerator
            temporal_token.denominator = -1
        elif freeSide == TokenParts.DENOMINATOR:
            temporal_token.numerator = -1
            temporal_token.denominator = token.denominator
        else:
            pass

        if len(self.elements) == 2:
            freeSide = getFreeSide(other, token)

            if other.numerator == other.denominator:
                pass
            elif freeSide == TokenParts.NUMERATOR:
                other.denominator = -1
            elif freeSide == TokenParts.DENOMINATOR:
                other.numerator = -1
            else:
                pass

        return True

    def input_handler(self, char: Key) -> bool:
        super().input_handler(char)

        # si se presiona ENTER el jugador ha terminado de posicionar una ficha
        if char == 10:  # ENTER
            # en el caso que este posicionando una ficha
            if self.is_locating_token:
                # se revisa si la posicion es valida
                if self.is_valid_position():
                    # se ha terminado el proceso de posicionamiento
                    self.is_locating_token = False
                    # se debe cambiar de turno
                    return True
        elif char == 116:  # t
            # cuando se presiona la tecla t mientras se esta en el proceso de
            # seleccion de posicion para una ficha, esta ficha debe ser rotada
            if self.is_locating_token:
                self.elements[self.linter][0].rotate()
        else:
            pass

        # se maneja el movimiento de las fichas mientras se esta seleccionando
        # posicion para una ficha
        if self.is_locating_token:
            # para mover las fichas que estan ya posicionadas en el tablero
            if char == 259:  # UP
                self.elements[self.linter][0].position[0] += 1
            if char == 258:  # DOWN
                self.elements[self.linter][0].position[0] -= 1
            if char == 260:  # RIGHT
                self.elements[self.linter][0].position[1] += 1
            if char == 261:  # LEFT
                self.elements[self.linter][0].position[1] -= 1

            # i j k l - 105 106 107 108
            # para mover la ficha que se esta posicionando
            if char == 119:  # w
                self.elements[self.linter][0].position[0] -= 1
            if char == 115:  # s
                self.elements[self.linter][0].position[0] += 1
            if char == 97:  # a
                self.elements[self.linter][0].position[1] -= 1
            if char == 100:  # d
                self.elements[self.linter][0].position[1] += 1

        # no se cambia de turno
        return False

    def locate_token(self, token: Token) -> None:
        """
        Este metodo inicia el proceso de posicionamiento de una ficha del
        jugador en pantalla.
        """
        # se posiciona la ficha en la mitad de la pantalla
        token.position[0] = self.height // 2 - 7 - self.zero_position[0]
        token.position[1] = self.width // 2 - 13 - self.zero_position[1]

        # se agrega la ficha a los elementos propios
        self.add_elements(token, False)

        # ahora el jugador tiene que posicionar la ficha en el lugar correcto
        self.is_locating_token = True
        # se acaba de agregar un elemento mas, por tanto este numero debe
        # aumentar en uno
        self.linter += 1

    def locate_computer_token(self, token: Token) -> None:
        """
        Este metodo posiciona la ficha del computador en el tablero
        """
        # se agrega la ficha a los elementos propios
        self.add_elements(token, False)
        # se acaba de agregar un elemento mas, por tanto este numero debe
        # aumentar en uno
        self.linter += 1

        # se revisa a que extremo se deberia agregar la ficha
        temporal_token: Token
        if token.are_concatenable(self.right):
            temporal_token = self.right
        else:
            temporal_token = self.left

        # se asigna la misma posicion a los tokens
        token.position = temporal_token.position[:]

        # se orientan las fichas en la misma direccion
        if token.orientation != temporal_token.orientation:
            token.rotate()

        # lo siguiente no se documenta porque debe ser implementado de forma
        # mas clara
        if token.numerator == temporal_token.numerator:
            token.reflect()

            if token.orientation == TokenOrientations.VERTICAL:
                token.position[0] -= 9
            else:
                token.position[1] -= 13
        elif token.denominator == temporal_token.numerator:
            if token.orientation == TokenOrientations.VERTICAL:
                token.position[0] -= 9
            else:
                token.position[1] -= 13
        elif token.numerator == temporal_token.denominator:
            if token.orientation == TokenOrientations.VERTICAL:
                token.position[0] += 9
            else:
                token.position[1] += 13
        else:
            token.reflect()

            if token.orientation == TokenOrientations.VERTICAL:
                token.position[0] += 9
            else:
                token.position[1] += 13

    def is_valid_token(self, light_token: Union[LightToken, Token]) -> bool:
        """
        Este metodo retorna True si un token puede ser posicionado en pantalla.

        light_token: Union[LightToken, Token]
            Token que sera posicionado.
        """
        # un token es valido si se puede conectar a cualquiera de las 2 ramas
        # del domino

        # somos no optimistas y de entrada suponemos que el token no se puede
        # conectar
        is_valid = False

        # si no hay fichas en el tablero, entones cualquier token puede ser
        # posicionado en pantalla
        if self.right is None and self.left is None:
            is_valid = True

        # cuando self.right tiene un valor se debe chequear si es concatenable
        # con la ficha pasada
        if self.right is not None:
            is_valid = is_valid or self.right.are_concatenable(light_token)

        # en el caso de que la ficha no sea concatenable con self.right, se
        # debe chequear con self.left
        if self.left is not None:
            is_valid = is_valid or self.left.are_concatenable(light_token)

        return is_valid
