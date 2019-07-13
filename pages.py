from __future__ import division

from utils import *
from baseObjects import *


class Cover(BaseContainer):
    def __init__(self, maxHeight, maxWidth):
        window = c.newwin(maxHeight, maxWidth, 0, 0)

        super(Cover, self).__init__(window)

        centerPositionX = getCenterRow(maxHeight)

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

        self.linter %= self.linterableObjects


class Options(BaseContainer):
    def __init__(self, height, width):
        window = c.newwin(height, width, 0, 0)

        super(Options, self).__init__(window)

        centerPositionX = getCenterRow(height)

        self.addElements(Writable(['No implementado'], (centerPositionX,
                         getCenterColumn('No implementado', width))))

    def inputHandler(self, char):
        if char == 10:  # ENTER
            return COVER

        return NONE


class Help(BaseContainer):
    def __init__(self, height, width):
        window = c.newwin(height, width, 0, 0)

        super(Help, self).__init__(window)

        centerPositionX = getCenterRow(height)

        self.addElements(Writable(['No implementado'], (centerPositionX,
                         getCenterColumn('No implementado', width))))

    def inputHandler(self, char):
        if char == 10:  # ENTER
            return COVER

        return NONE


class Credits(BaseContainer):
    def __init__(self, height, width):
        window = c.newwin(height, width, 0, 0)

        super(Credits, self).__init__(window)

        centerPositionX = getCenterRow(height)

        self.addElements(Writable(['No implementado'], (centerPositionX,
                         getCenterColumn('No implementado', width))))

    def inputHandler(self, char):
        if char == 10:  # ENTER
            return COVER

        return NONE
