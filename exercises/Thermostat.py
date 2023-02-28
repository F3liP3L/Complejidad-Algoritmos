
def isValidData(x, a, b):
    '''
      Realiza la validacion correspondiente al valor absoluto.

      Args:
          str x, a, b
      Returns:
          boolean

      Example:
          >>> isValidData(5, 8,10)
          False
      '''
    return abs(a-b)>=x

def resolve(l,r,x,a,b):
    '''
    Realiza las respectivas validaciones para retornar la temperatura correcta.

    :param l: int
    :param r: int
    :param x: int
    :param a: int
    :param b: int
    :return: int

    '''
    num = -1
    if(a == b):
        num = 0
    elif(isValidData(x,a,b)):
        num = 1
    elif(isValidData(x,a,l) and isValidData(x,b,l) and isValidData(x,b,r)):
        num = 2
    elif(isValidData(x,a,l) and isValidData(x,l,r) and isValidData(x,b,r) or
         isValidData(x,a,r) and isValidData(x,l,r) and isValidData(x,b,l)):
        num = 3
    return num


testCase = int(input("Ingresa la cantidad de casos de prueba: "))
for i in range(testCase):
    l = int(input())
    r = int(input())
    x = int(input())
    a = int(input())
    b = int(input())
    print(resolve(l, r, x, a, b))





