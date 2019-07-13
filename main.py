#!-*- encoding: utf-8 -*-

from argparse import ArgumentParser

from manager import Manager

from tokens import areClose, _areCompatible


DESCRIPCION = """Esta es una implementacion del juego de mesa domino.


En este juego hay 3 paneles diferentes, en 2 de los cuales se puede navegar
haciendo uso de la tecla TAB, el tercer panel es informativo, este muestra
en que panel esta(SCOPE). Tokens es el panel donde estan las fichas propias no
jugadas, Table es el panel donde estan las fichas jugadas por todos los
jugadores. con las teclas UP, DOWN, RIGHT, LEFT puede mover las fichas en ambos
paneles(se mueve las fichas del panel en el que este posicinado), si quiere
jugar una ficha, debe ubicarse en el panel Tokens y con las teclas a y d puede
navegar por las fichas disponibles, una vez posicionado en la ficha deseada la
puede seleccionar con la tecla ENTER, para elejir la ubicacion correcta de la
ficha en Table puede mover las fichas de la tabla con las teclas i, j, k, l o
mover la ficha seleccionada con las teclas UP, DOWN, RIGHT, LEFT, la
orientacion de la ficha seleccionada se puede cambiar con la tecla t y con la
tecla r puede trocar los numeros del domino ([2|3] -> [3|2]). Para pasar turno
use la tecla p y para salir del programa use la letra q
"""


def validateArgs(args):
    """
    Esta funcion lanza un error si los parametros no tienen valores validos
    """
    pass


def main():
    parser = ArgumentParser(description=DESCRIPCION)

    parser.add_argument('-t', '--tokens-per-player', type=int, default=9,
                        help='number of tokens per player')
    parser.add_argument('-m', '--max-number', type=int, default=9,
                        help='maximum number in the dominoes tokens')

    args = parser.parse_args()

    validateArgs(args)

    # se ejecuta la aplicacion
    manager = Manager(args)

    manager.loop()

    manager.end()


if __name__ == '__main__':
    main()
