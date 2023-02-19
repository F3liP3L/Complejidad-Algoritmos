# Ejercicio 2451 de Becrowd PacMan

def countMaxMeelConsume(road):
    '''
    Permite contar la mayor cantidad de comida consumida en el recorrido.
    Args:
        str road
    Returns:
        int
    '''
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


pacmanRoadReverse = ""
pacmanRoadTotal = ""
try:
    boardLength = int(input('Elige el tamaño del recorrido horizontal: '))
    for i in range(boardLength):
        pacmanRoad = input()[0:boardLength] #Se toma solo la cantidad de letras requeridas.
        if(i % 2 != 0):
            pacmanRoad = pacmanRoad[::-1] #Se invierte la cadena.
        pacmanRoadTotal += pacmanRoad
except Exception:
    print("An unexpected error!!")
finally:
    print(str(countMaxMeelConsume(pacmanRoadTotal))+"\n")

