import curses as c

from domino.game import Game
from domino.pages import Cover, Credits, Help, Options
from domino.utils import *


class Manager:
    """
    Esta clase se encarga de manejar todo el ciclo del programa, inicializa
    todo lo necesario para el juego todo en pantalla, recibe entrada
    del usuario, gestiona cambio de ventanas,...

    Parametros
    ----------
    args(namespace): namespace con los parametros pasados por el usuario
    """

    def __init__(self, args):
        # variables que mantienen la logica de la apliacion
        self.quit = False

        # se realiza inicializacion de todo lo relacionado con curses
        self.init()

        # se inicializan las posibles ventanas del juego
        self.cover = Cover(*self.stdscr.getmaxyx())
        self.game = Game(*self.stdscr.getmaxyx())
        self.options = Options(*self.stdscr.getmaxyx())
        self.help = Help(*self.stdscr.getmaxyx())
        self.credits = Credits(*self.stdscr.getmaxyx())

        # este atributo contiene referencia a la ventana que se muestra
        self.current_window = self.cover

    def init(self):
        # se inicializa curses y se obtiene una referencia a la ventana
        # principal
        self.stdscr = c.initscr()

        # para manejar colores
        c.start_color()

        # para recibir codigo ascii de las teclas
        self.stdscr.keypad(True)
        # para controlar que se imprimira en pantalla
        c.noecho()
        # para leer del teclado sin presionar la tecla enter
        c.cbreak()

        # para no mostrar el cursor en pantalla
        c.curs_set(0)

        # inicializacion de colores
        c.init_pair(COLOR_SELECTED_ELEMENT, c.COLOR_RED, c.COLOR_BLACK)
        c.init_pair(COLOR_SELECTED_PANEL, c.COLOR_GREEN, c.COLOR_BLACK)

    def loop(self):
        # se borra la pantalla
        self.stdscr.erase()

        # se dibuja un borde en la ventana
        self.stdscr.box()

        # se cargan los cambios
        self.stdscr.refresh()

        while not self.quit:
            # se dibuja la ventana, puede ser cover, game, options,...
            self.current_window.write()

            # se obtiene entrada del usuario
            char = self.stdscr.getch()

            # cada ventana debe retornar a que ventana pasara el programa en
            # el siguiente ciclo de aplicacion, si retorna NONE es que sigue
            # en la misma ventana
            nextWindow = self.current_window.input_handler(char)

            # se actualiza el valor de la ventana actual
            if nextWindow == COVER:
                self.current_window = self.cover
            elif nextWindow == PLAY:
                self.current_window = self.game
            elif nextWindow == OPTIONS:
                self.current_window = self.options
            elif nextWindow == HELP:
                self.current_window = self.help
            elif nextWindow == CREDITS:
                self.current_window = self.credits
            elif nextWindow == QUIT:
                self.quit = True
            else:
                pass

    def end(self):
        c.endwin()
