with open('input.txt', 'r') as f:
    lines = f.readlines()
    values = [i.strip() for i in lines]

mapPuzzle = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors', 'X': 'Lose', 'Y': 'Draw', 'Z': 'Win'}
pointsShape = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
evaluation = {'Lose': 0, 'Draw': 3, 'Win': 6}


def calculatePoints(game):
    opponentShape = mapPuzzle[game[0]]
    currentShape = mapPuzzle[game[2]]

    if (opponentShape, currentShape) in [('Rock','Draw'), ('Paper','Lose'), ('Scissors','Win') ]:
        return evaluation[currentShape] + pointsShape['Rock']
    elif (opponentShape, currentShape) in [('Rock', 'Win'), ('Paper', 'Draw'), ('Scissors', 'Lose')]:
        return evaluation[currentShape] + pointsShape['Paper']
    else:
        return evaluation[currentShape] + pointsShape['Scissors']
        

print(sum([calculatePoints(iterator) for iterator in values]))