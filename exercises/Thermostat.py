def isAbsolutValueValidate(x, a, b):
    """
    Verifica que el valor absoluto de dos numeros es mayor o igual a un numero determinado.

    :param x: int
    :param a: int
    :param b: int
    :return: boolean

    Example:
        >>> isAbsolutValueValidate(5, 8,10)
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
    elif isAbsolutValueValidate(x, r, b) or isAbsolutValueValidate(x, a, l):
        num = 2
    elif isAbsolutValueValidate(x, r, a) and isAbsolutValueValidate(x, l, b):
        num = 3
    return num


testCase = int(input())
for i in range(testCase):
    l = int(input())
    r = int(input())
    x = int(input())
    a = int(input())
    b = int(input())
    print(resolve(l, r, x, a, b))

isAbsolutValueValidateDocumentacion = isAbsolutValueValidate.__doc__
resolveDocumentacion = resolve.__doc__
print(isAbsolutValueValidateDocumentacion, "\n", )