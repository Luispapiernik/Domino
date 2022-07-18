from enum import IntEnum
from typing import Tuple

Position = Tuple[int, int]
Key = int


class Events(IntEnum):
    NONE = 0
    COVER = 1
    PLAY = 2
    OPTIONS = 3
    HELP = 4
    CREDITS = 5
    QUIT = 6


class Players(IntEnum):
    PLAYER = 0
    COMPUTER = 1


class TokenParts(IntEnum):
    NUMERATOR = 0
    DENOMINATOR = 1
    BOTH = 2


class TokenOrientations(IntEnum):
    VERTICAL = 0
    HORIZONTAL = 1
