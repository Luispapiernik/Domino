    tokens = []

    for token, _ in manager.game.table.elements:
        tokens.append(token)

    print('==================================================================')
    print(manager.game.table.right, manager.game.table.left)
    print(manager.game.table.elements[0][0])
    print(manager.game.table.elements[1][0])

    print('==================================================================')
    print(areClose(tokens[0], tokens[1]))
    print(_areCompatible(tokens[0], tokens[1]))

    print(areClose(tokens[1], tokens[0]))
    print(_areCompatible(tokens[1], tokens[0]))

    print('==================================================================')
    print(areClose(manager.game.table.right, tokens[1]))
    print(_areCompatible(manager.game.table.right, tokens[1]))

    print(areClose(manager.game.table.left, tokens[1]))
    print(_areCompatible(manager.game.table.left, tokens[1]))

    print('==================================================================')
    print(areClose(tokens[1], manager.game.table.right))
    print(_areCompatible(tokens[1], manager.game.table.right))

    print(areClose(tokens[1], manager.game.table.left))
    print(_areCompatible(tokens[1], manager.game.table.left))

    print('==================================================================')
    print(tokens[0].areCompatible(tokens[1]))
    print(tokens[1].areCompatible(tokens[0]))

    print(manager.game.table.right.areCompatible(tokens[1]))
    print(manager.game.table.left.areCompatible(tokens[1]))

    print('RIGHT')
    print(manager.game.table.right.orientation)
    print(manager.game.table.right.position)
    print(manager.game.table.right.numerator)
    print(manager.game.table.right.denominator)

    print('LEFT')
    print(manager.game.table.left.orientation)
    print(manager.game.table.left.position)
    print(manager.game.table.left.numerator)
    print(manager.game.table.left.denominator)