import curses

from domino.config import settings
from domino.game import Game
from domino.pages import Cover, Credits, Help, Options
from domino.schemas import Events


class Manager:
    """
    Esta clase se encarga de manejar todo el ciclo del programa, inicializa
    todo lo necesario para el juego todo en pantalla, recibe entrada
    del usuario, gestiona cambio de ventanas,...

    Parametros
    ----------
    args(namespace): namespace con los parametros pasados por el usuario
    """

    def __init__(self, args) -> None:
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

    def init(self) -> None:
        # se inicializa curses y se obtiene una referencia a la ventana
        # principal
        self.stdscr = curses.initscr()

        # para manejar colores
        curses.start_color()

        # para recibir codigo ascii de las teclas
        self.stdscr.keypad(True)
        # para controlar que se imprimira en pantalla
        curses.noecho()
        # para leer del teclado sin presionar la tecla enter
        curses.cbreak()

        # para no mostrar el cursor en pantalla
        curses.curs_set(0)

        # inicializacion de colores
        curses.init_pair(
            settings.color_selected_element, curses.COLOR_RED, curses.COLOR_BLACK
        )
        curses.init_pair(
            settings.color_selected_panel, curses.COLOR_GREEN, curses.COLOR_BLACK
        )

    def loop(self) -> None:
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
            if nextWindow == Events.COVER:
                self.current_window = self.cover
            elif nextWindow == Events.PLAY:
                self.current_window = self.game
            elif nextWindow == Events.OPTIONS:
                self.current_window = self.options
            elif nextWindow == Events.HELP:
                self.current_window = self.help
            elif nextWindow == Events.CREDITS:
                self.current_window = self.credits
            elif nextWindow == Events.QUIT:
                self.quit = True
            else:
                pass

    def end(self):
        curses.endwin()
