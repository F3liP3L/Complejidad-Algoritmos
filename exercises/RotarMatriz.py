import random

numMatriz = int(input("Ingrese el numero de fila y columnas de tu matriz: "))

matriz = []

for i in range(numMatriz):
    matriz.append([])
    for j in range(numMatriz):
        matriz[i].append(random.randint(0, 100))
print(matriz)

def rotateMatrizNinetyDegrees(matrix):
    n = len(matrix)
    for i in range(n):  # Tranponemos la matriz usando una tupla
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):  # Se invierte la matriz ya traspuesta usando una tupla
        for j in range(n // 2):
            matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]
    return matrix


print("90 grados \n", rotateMatrizNinetyDegrees(matriz))  # 90
print("180 grados \n", rotateMatrizNinetyDegrees(matriz))  # 180
print("270 grados \n", rotateMatrizNinetyDegrees(matriz))  # 270
print("360 grados \n", rotateMatrizNinetyDegrees(matriz))  # 360
