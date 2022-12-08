with open('input.txt', 'r') as f:
    lines = f.readlines()
    values = [i.strip() for i in lines]

mapPuzzle = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors', 'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}
pointsShape = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
evaluation = {'Lose': 0, 'Draw': 3, 'Win': 6}


def calculatePoints(game):
    opponentShape = mapPuzzle[game[0]]
    currentShape = mapPuzzle[game[2]]

    if opponentShape == currentShape:
        return evaluation['Draw'] + pointsShape[currentShape]
    elif (opponentShape, currentShape) in [('Paper', 'Rock'), ('Rock', 'Scissors'), ('Scissors', 'Paper')]:
        # loss for us
        return evaluation['Lose'] + pointsShape[currentShape]
    else:
        return evaluation['Win'] + pointsShape[currentShape]

print(sum([calculatePoints(iterator) for iterator in values]))