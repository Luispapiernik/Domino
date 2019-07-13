#! -*- coding: utf-8 -*-

from __future__ import division

from utils import *
from baseObjects import *


class PageNotImplemented(BaseContainer):
    """
    Esta clase reprensenta alguna ventana que no ha sido implementada
    """
    def __init__(self, height, width):
        window = c.newwin(height, width, 0, 0)

        super(PageNotImplemented, self).__init__(window)

        centerPositionX = getCenterRow(height)

        self.addElements(Writable(['No implementado'], (centerPositionX,
                         getCenterColumn('No implementado', width))))

    @applyEvent(10, COVER)  # ENTER
    def inputHandler(self, char):
        pass


class Cover(BaseContainer):
    """
    Esta clase reprensenta la primera ventana del aplicacion, en ella estan las
    diferentes opciones que puede elejir un jugador: Jugar, Opciones,...

    Parametros
    ----------
    maxHeight(int): altura de la ventana
    maxWidth(int): ancho de la ventana
    """
    def __init__(self, maxHeight, maxWidth):
        # se crea la ventana en donde se dibujaran los elementos
        window = c.newwin(maxHeight, maxWidth, 0, 0)

        # se llama al inicializador del padre
        super(Cover, self).__init__(window)

        # para dibujar los elementos de forma centrada se obtiene la fila que
        # esta en el centro
        centerPositionX = getCenterRow(maxHeight)

        # se agregan los elementos
        self.addElements(Writable(['Jugar'], (centerPositionX,
                         getCenterColumn('Jugar', maxWidth))))

        self.addElements(Writable(['Opciones'], (centerPositionX + 1,
                         getCenterColumn('Opciones', maxWidth))))

        self.addElements(Writable(['Ayuda'], (centerPositionX + 2,
                         getCenterColumn('Ayuda', maxWidth))))

        self.addElements(Writable(['Credito'], (centerPositionX + 3,
                         getCenterColumn('Credito', maxWidth))))

    @applyEvent(c.KEY_RESIZE, QUIT)  # cuando se cambia dimension de la ventana
    @applyEvent(113, QUIT)  # q
    def inputHandler(self, char):
        """
        Este metodo se encarga de manejar entrada del usuario, la clase Cover
        solo gestiona el cambio de ventana
        """
        # self.linter esta apuntando al elmento que es resaltado, si se aumenta
        # o disminuye este valor en uno el objeto resaltado cambia, si se
        # preciona la tecla enter en uno de los elementos se pasa a la ventana
        # correspondiente
        if char == 259:  # UP
            self.linter -= 1
        elif char == 258:  # DOWN
            self.linter += 1
        elif char == 10:  # ENTER
            if self.linter == 0:
                return PLAY
            elif self.linter == 1:
                return OPTIONS
            elif self.linter == 2:
                return HELP
            elif self.linter == 3:
                return CREDITS
            else:
                return NONE
        else:
            pass

        # self.linter no debe estar por fuera de [0, 3], si esta por fuera con
        # operacion modulo se vuelve a poner en el conjunto [0, 3]
        self.linter %= self.linterableObjects


class Options(PageNotImplemented):
    pass


class Help(PageNotImplemented):
    pass


class Credits(PageNotImplemented):
    pass
