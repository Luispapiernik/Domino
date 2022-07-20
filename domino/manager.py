import curses
from argparse import Namespace

from domino.config import settings
from domino.game import Game
from domino.pages import Cover, Credits, Help, Options
from domino.schemas import Events


class Manager:
    """
    This class manage all the program cycle, initialize all the necessary
    resources for the game, gets user input, manage the window changes, ...

    Parameters
    ----------
    args: argparse.Namespace
        Namespace with the user parameters.
    """

    def __init__(self, _: Namespace) -> None:
        self.quit = False

        # Initialize the ncurses library
        self.init()

        # Initialize all program windows
        self.cover = Cover(*self.stdscr.getmaxyx())
        self.game = Game(*self.stdscr.getmaxyx())
        self.options = Options(*self.stdscr.getmaxyx())
        self.help = Help(*self.stdscr.getmaxyx())
        self.credits = Credits(*self.stdscr.getmaxyx())

        self.current_window = self.cover

    def init(self) -> None:
        # Get reference to the main window.
        self.stdscr = curses.initscr()

        # In order to get color controls.
        curses.start_color()

        # In order to get the ASCII code of every key input.
        self.stdscr.keypad(True)
        # To get more control in what is printed on screen.
        curses.noecho()
        # This allows to read input keys without waiting for a key being pressed.
        curses.cbreak()

        # This ocults the cursor on screen
        curses.curs_set(0)

        # Set main colors.
        curses.init_pair(
            settings.color_selected_element, curses.COLOR_RED, curses.COLOR_BLACK
        )
        curses.init_pair(
            settings.color_selected_panel, curses.COLOR_GREEN, curses.COLOR_BLACK
        )

    def loop(self) -> None:
        # Clean the screen
        self.stdscr.erase()

        # Draw a box around the screen.
        self.stdscr.box()

        # Load changes to screen.
        self.stdscr.refresh()

        while not self.quit:
            # Draw the current window.
            self.current_window.write()

            # Get user input.
            char = self.stdscr.getch()

            # Every window must returns what is the next window to be show, in
            # case that Events.NONE is returned, there is not transition of window
            nextWindow = self.current_window.input_handler(char)

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

    def end(self) -> None:
        curses.endwin()
