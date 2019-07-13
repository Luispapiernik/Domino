from __future__ import division

# representacion de posiciones de las fichas

# +-----+
# |* * *|
# |* * *|
# |* * *|
# |-----|
# |* * *|
# |* * *|
# |* * *|
# +-----+

# +-----------+
# |* * *|* * *|
# |* * *|* * *|
# |* * *|* * *|
# +-----------+

# estas constantes definen la logica del juego
# posibles orientaciones para las fichas
VERTICAL = 0
HORIZONTAL = 1

# necesarios para la construccion del string que representa a las fichas
TOKENS_PARTS = [{}, {}]
TOKENS_PARTS[VERTICAL]['head'] = '+-----+'
TOKENS_PARTS[VERTICAL]['middle'] = '|-----|'
TOKENS_PARTS[VERTICAL][0] = ['|     |', '|     |', '|     |']
TOKENS_PARTS[VERTICAL][1] = ['|     |', '|  *  |', '|     |']
TOKENS_PARTS[VERTICAL][2] = ['|*    |', '|     |', '|    *|']
TOKENS_PARTS[VERTICAL][3] = ['|*    |', '|  *  |', '|    *|']
TOKENS_PARTS[VERTICAL][4] = ['|*   *|', '|     |', '|*   *|']
TOKENS_PARTS[VERTICAL][5] = ['|*   *|', '|  *  |', '|*   *|']
TOKENS_PARTS[VERTICAL][6] = ['|*   *|', '|*   *|', '|*   *|']
TOKENS_PARTS[VERTICAL][7] = ['|*   *|', '|* * *|', '|*   *|']
TOKENS_PARTS[VERTICAL][8] = ['|* * *|', '|*   *|', '|* * *|']
TOKENS_PARTS[VERTICAL][9] = ['|* * *|', '|* * *|', '|* * *|']

TOKENS_PARTS[HORIZONTAL]['head'] = '+|||+'
TOKENS_PARTS[HORIZONTAL]['middle'] = '-|||-'
TOKENS_PARTS[HORIZONTAL]['space'] = '-   -'
TOKENS_PARTS[HORIZONTAL][0] = ['-   -', '-   -', '-   -']
TOKENS_PARTS[HORIZONTAL][1] = ['-   -', '- * -', '-   -']
TOKENS_PARTS[HORIZONTAL][2] = ['-  *-', '-   -', '-*  -']
TOKENS_PARTS[HORIZONTAL][3] = ['-  *-', '- * -', '-*  -']
TOKENS_PARTS[HORIZONTAL][4] = ['-* *-', '-   -', '-* *-']
TOKENS_PARTS[HORIZONTAL][5] = ['-* *-', '- * -', '-* *-']
TOKENS_PARTS[HORIZONTAL][6] = ['-* *-', '-* *-', '-* *-']
TOKENS_PARTS[HORIZONTAL][7] = ['-* *-', '-***-', '-* *-']
TOKENS_PARTS[HORIZONTAL][8] = ['-***-', '-* *-', '-***-']
TOKENS_PARTS[HORIZONTAL][9] = ['-***-', '-***-', '-***-']

# estas constantes definen las posiibles configuraciones de cercania entre 2
# fichas
PROXIMITYCONFIGURACION_1 = 1
PROXIMITYCONFIGURACION_2 = 2
PROXIMITYCONFIGURACION_3 = 3
PROXIMITYCONFIGURACION_4 = 4
PROXIMITYCONFIGURACION_5 = 5
PROXIMITYCONFIGURACION_6 = 6
PROXIMITYCONFIGURACION_7 = 7
PROXIMITYCONFIGURACION_8 = 8
PROXIMITYCONFIGURACION_9 = 9
PROXIMITYCONFIGURACION_10 = 10
PROXIMITYCONFIGURACION_11 = 11
PROXIMITYCONFIGURACION_12 = 12
PROXIMITYCONFIGURACION_13 = 13
PROXIMITYCONFIGURACION_14 = 14

# especifica que parte tiene libre una ficha para realizar conexiones
NUMERATOR = 0
DENOMINATOR = 1
BOTH = 2

PLAYER = 0
COMPUTER = 1

# ============================================================================
# estas constantes definen como lucira el juego visualmente
# linter para la seleccion del elemento de alguna ventana
COLOR_SELECTED_ELEMENT = 1
COLOR_SELECTED_PANEL = 2

# ============================================================================
# estas constantes definen la logica del programa
# eventos que especifican a que pagina del programa se debe ir
NONE = 0
COVER = 1
PLAY = 2
OPTIONS = 3
HELP = 4
CREDITS = 5
QUIT = 6


def getCenterColumn(text, maxWidth):
    middleTex = len(text) // 2
    return maxWidth // 2 - middleTex


def getCenterRow(maxHeight):
    return (maxHeight - 2) // 2


def applyEvent(character, event):
    def decorator(function):
        def wrapper(self, char):
            if character == char:
                return event
            else:
                return function(self, char)

        return wrapper

    return decorator
