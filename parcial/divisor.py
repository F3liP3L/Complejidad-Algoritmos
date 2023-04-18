
def listDivisor(number, n):
    divisores = []
    for x in range(1, n+1):
        if number % x == 0:
            divisores.append(x)
    return divisores

print(listDivisor(1, 10))
