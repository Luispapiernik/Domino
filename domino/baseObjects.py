import curses as c


class Writable:
    """
    Esta clase representa algo que puede ser dibujado en pantalla, basicamente
    es texto

    Parametros
    ----------
    text(str): contiene el valor del string que representa
    position((int, int)): posicion
    """

    def __init__(self, text, position):
        # texto que sera dibujado
        self.text = text
        # posicion en la que se dibujara el texto, es una dupla con primera
        # componente representando filas y segunda representando columnas
        self.position = position

    def write(self, window, zero_position, color_linter=None):
        """
        Este metodo escibe texto en alguna ventana

        Parametros
        ----------
        window: ventana en la que se escribira el texto
        zero_position: indica un corrimiento que se le debe hacer al texto
        color_linter(int | None): si este valor no es None indica el color que
            se debe aplicar al text
        """
        if color_linter is not None:
            # cuando se pasa un valor de color valido, se aplica el color
            window.attron(c.color_pair(color_linter))

        height, width = window.getmaxyx()

        for x in range(len(self.text[0])):
            for y in range(len(self.text)):
                column = self.position[1] + x + zero_position[1]
                row = self.position[0] + y + zero_position[0]

                # solo se debe dibujar lo que este dentro de la ventana
                if 0 < row < height - 1 and 0 < column < width - 1:
                    window.addch(row, column, self.text[y][x])

        if color_linter is not None:
            # cuando se aplico un color valido es necesario desactivarlo de la
            # ventana
            window.attroff(c.color_pair(color_linter))


class BaseContainer:
    """
    Esta clase representa un panel, que no es mas que un contenedor para
    objetos que se pueden escribir en pantalla

    Parametros
    ----------
    window(Window): Representa la ventana en donde se dibujaran los elementos
        del contenedor
    """

    def __init__(self, window):
        self.window = window

        self.height, self.width = self.window.getmaxyx()

        # especifica que corrimiento se debe hacer en filas y columnas al
        # momento de dibujar los elementos del contenedor
        self.zero_position = [0, 0]

        # lista con duplas, en la que la primera componente de cada dupla
        # representa al elemento y la segunda es un booleano que dice si el
        # elemento correspondiente es resaltable o no
        self.elements = []

        # variables que se usan para resaltar con algun color elementos del
        # contenedor
        self.linter = 0  # indice del elemento a resaltar
        self.linterable_objects = 0  # numero de elementos resaltables

    def add_elements(self, element, linterable=True):
        """
        Este Metodo agrega elementos al contenedor

        Parametros
        ----------
        element(Writable): elemento que sera agregado, debe ser un objeto de la
            clase Writable o de alguna clase que herede de esta
        linterable(bool): indica si el elemento es resaltable
        """
        self.elements.append((element, linterable))

        # si es linterable, se debe aumentar el nunmero de objetos resaltbles
        if linterable:
            self.linterable_objects += 1

    def input_handler(self, char):
        """
        Este metodo es simplemente una interfaz y debe ser redefinido por las
        clases que hereden a BaseContainer
        """
        pass

    def write(self, border_color=None):
        """
        Este metodo dibuja al contenedor en pantall

        Parametros
        ----------
        border_color(int | None): si este valor no es None indica el color que
            se debe aplicar al text
        """
        # se limpia la pantalla
        self.window.erase()

        # cuando se pasa un color valido se debe activar este atribut en la
        # pantalla
        if border_color is not None:
            self.window.attron(c.color_pair(border_color))

        # se dibuja un borde en la ventana
        self.window.box()

        # si se activo un color en la ventana, tambien se tiene que desactivar
        if border_color is not None:
            self.window.attroff(c.color_pair(border_color))

        # contiene el color con el que se debe dibujar el elemento,
        # inicialmente es None porque no todos los elementos son resaltables
        color_linter = None
        # se itera sobre la cantidad de elementos
        for i in range(len(self.elements)):

            element, linterable = self.elements[i]

            # si el elemento es linterable y ademas el indice del elemento
            # coincide con self.linter, entonces el elemento se debe resaltar
            if i == self.linter and linterable:
                color_linter = 1

            # se dibuja el elemento en pantalla
            element.write(self.window, self.zero_position, color_linter)

            # se desactiva el coloreado a los elementos
            color_linter = None

        # se cargan los cambios en pantalla
        self.window.refresh()
