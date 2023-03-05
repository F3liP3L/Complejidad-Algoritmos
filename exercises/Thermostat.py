def isAbsolutValueValidate(x, a, b):
    """
    Verifica que el valor absoluto de dos numeros es mayor o igual a un numero determinado.

    :param x: int
    :param a: int
    :param b: int
    :return: boolean

    Example:
        >>> isAbsolutValueValidate(5,8,10)
    False

    """
    return abs(a - b) >= x


def resolve(l, r, x, a, b):
    """
    Realiza las respectivas validaciones para devolver el numero de operaciones.

    :param l: int
    :param r: int
    :param x: int
    :param a: int
    :param b: int
    :return: int

    """
    num = -1
    if a == b:
        num = 0
    elif isAbsolutValueValidate(x, a, b):
        num = 1
    elif isAbsolutValueValidate(x, r, max(a, b)) or isAbsolutValueValidate(x, min(a, b), l):
        num = 2
    elif (isAbsolutValueValidate(x, r, a) and isAbsolutValueValidate(x, b, l)) or (
            isAbsolutValueValidate(x, a, l) and isAbsolutValueValidate(x, r, b)):
        num = 3
    return num


try:
    testCase = int(input())
    if 0 < testCase <= 10**6:
        for i in range(testCase):
            l, r, x = map(int, input().split())
            a, b = map(int, input().split())
            print(resolve(l, r, x, a, b))
except EOFError:
    print("An unexpected error!!")

