import random

def generarSudoku():
    """
    Metodo que genera un tablero de Sudoku válido y completo.
    """
    # Crear un tablero vacío
    tablero = [[0 for _ in range(9)] for _ in range(9)]  # Se llena un tablero de 9x9 con ceros.

    # Rellenar la diagonal principal con números aleatorios
    for i in range(0, 9, 3):
        rellenarCuadrante(tablero, i, i)

    # Resolver el tablero vacío
    resolverSudoku(tablero)

    # Quitar algunos números del tablero para obtener un Sudoku parcialmente lleno
    eliminarNumeros(tablero)

    return tablero


def rellenarCuadrante(tablero, fila, columna):
    """
    Metodo que se encarga de llenar un cuadrante de 3x3 del tablero con números aleatorios que cumplan las reglas del Sudoku.
    """
    numeros = list(range(1, 10))
    random.shuffle(numeros)  # Ordena la lista de forma aleatoria
    for i in range(3):
        for j in range(3):
            tablero[fila + i][columna + j] = numeros.pop()


def resolverSudoku(tablero):
    """
    Metodo que se encarga de resolver el tablero de Sudoku usando recursión y retroceso.
    Args: tablero matriz
    return: Boolean
    """
    vacio = encontrarCeldaVacia(tablero)
    if not vacio:
        return True  # El tablero está completo y resuelto
    fila, columna = vacio

    # Probar números del 1 al 9 en la celda vacía
    for num in range(1, 10):
        if esValido(tablero, fila, columna, num):
            tablero[fila][columna] = num
            if resolverSudoku(tablero):
                return True
            tablero[fila][columna] = 0  # Retroceder si no se encuentra solución
    return False  # No se encontró solución


def encontrarCeldaVacia(tablero):
    """
    Encuentra una celda vacía en el tablero de Sudoku.
    """
    for i in range(9):
        for j in range(9):
            if tablero[i][j] == 0:
                return (i, j)
    return None  # No hay celdas vacías


def esValido(tablero, fila, columna, num):
    """
    Comprueba si un número es válido para una celda dada en el tablero de Sudoku.
    """
    # Comprobar en la misma fila
    if num in tablero[fila]:
        return False

    # Comprobar en la misma columna
    if num in [tablero[i][columna] for i in range(9)]:
        return False

    # Comprobar en el mismo cuadrante de 3x3
    cuadranteFila = fila // 3 * 3
    cuadranteColumna = columna // 3 * 3
    for i in range(3):
        for j in range(3):
            if tablero[cuadranteFila + i][cuadranteColumna + j] == num:
                return False

    return True  # El número es válido

def eliminarNumeros(tablero):
    """
    Metodo que elimina números del tablero para obtener un Sudoku parcialmente lleno.
    """
    numAquitar = 45  # Número de celdas a quitar.
    while numAquitar > 0:
        fila = random.randint(0, 8)
        columna = random.randint(0, 8)
        if tablero[fila][columna] != 0:
            tablero[fila][columna] = 0
            numAquitar -= 1

sudoku = generarSudoku()
print(sudoku)
print("\t\n Sudoku: \n")
resolverSudoku(sudoku)
print(sudoku)
