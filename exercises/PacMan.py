# Ejercicio 2451 de Beecrowd PacMan

def countMaxMeelConsume(road):
    """
    Permite contar la mayor cantidad de comida consumida en el recorrido.
    Args:
        str road
    Returns:
        int
    """
    maxInsuredConsume = 0
    mealInsuredConsume = 0
    for letter in road:
        if (letter == 'A'):
            maxInsuredConsume = max(maxInsuredConsume, mealInsuredConsume)
            mealInsuredConsume = 0
        elif (letter == 'o'):
            mealInsuredConsume += 1
    maxInsuredConsume = max(maxInsuredConsume, mealInsuredConsume)
    return maxInsuredConsume

def validateRoad(road, roadValid):
    '''
    Permite validar si el camino ingresado es valido.
    :param road str:
    :param roadValid array:
    :return: boolean
    '''
    isValidate = True
    for letter in road:
        if letter not in roadValid:
            isValidate = False
    return isValidate


pacmanRoadReverse = ""
pacmanRoad = ""
pacmanRoadTotal = ""
try:
    boardLength = int(input())
    for i in range(boardLength):
        dataCorrect = False
        while not dataCorrect:
            pacmanRoad = input()
            if validateRoad(pacmanRoad, ['.', 'A', 'o']) and len(pacmanRoad) == boardLength:
                dataCorrect = True
        if i % 2 != 0:
            pacmanRoad = pacmanRoad[::-1]  # Se invierte la cadena haciendo uso de los indices inversos.
        pacmanRoadTotal += pacmanRoad
except Exception:
    print("An unexpected error!!")
finally:
    print(str(countMaxMeelConsume(pacmanRoadTotal)))


