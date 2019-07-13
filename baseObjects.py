import curses as c


class Writable(object):
    """
    Esta clase representa algo que puede ser dibujado en pantalla, basicamente
    es texto o fichas

    Parametros
    ----------
    text(str): contiene el valor del string que representa
    position((int, int)): posicion
    """
    def __init__(self, text, position):
        self.text = text
        self.position = position

    def write(self, window, zeroPosition, colorLinter=None):
        """
        Este metodo escibe texto en alguna ventana

        Parametros
        ----------
        window: ventana en la que se escribira el texto
        zeroPosition: indica un corrimiento que se le debe hacer al texto
        colorLinter: si este valor no es None indica el color que se debe
            aplicar al text
        """
        if colorLinter is not None:
            window.attron(c.color_pair(colorLinter))

        height, width = window.getmaxyx()

        for x in range(len(self.text[0])):
            for y in range(len(self.text)):
                column = self.position[1] + x + zeroPosition[1]
                row = self.position[0] + y + zeroPosition[0]

                if 0 < row < height - 1 and 0 < column < width - 1:
                    window.addch(row, column, self.text[y][x])

        if colorLinter is not None:
            window.attroff(c.color_pair(colorLinter))


class BaseContainer(object):
    """
    Esta clase representa un panel, que no es mas que un contenedor para
    objetos que se pueden escribir en pantalla
    """
    def __init__(self, window):
        self.window = window

        self.height, self.width = self.window.getmaxyx()

        self.zeroPosition = [0, 0]

        self.elements = []

        self.linter = 0
        self.linterableObjects = 0

    def addElements(self, element, linterable=True):
        self.elements.append((element, linterable))

        if linterable:
            self.linterableObjects += 1

    def inputHandler(self, char):
        pass

    def write(self, borderColor=None):
        self.window.erase()

        if borderColor is not None:
            self.window.attron(c.color_pair(borderColor))

        self.window.box()

        if borderColor is not None:
            self.window.attroff(c.color_pair(borderColor))

        colorLinter = None
        for i in range(len(self.elements)):

            element, linterable = self.elements[i]

            if i == self.linter and linterable:
                colorLinter = 1

            element.write(self.window, self.zeroPosition, colorLinter)

            colorLinter = None

        self.window.refresh()
