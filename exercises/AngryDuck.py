from math import cos
from math import sin

GRAVITY = 9.80665
PI = 3.14159


def convertDegreesToRadians(angle):
    """
    Converts a degree angle to radians.

    @param angle: float.
    @return: float.
    """
    return angle * PI / 180.0


while True:
    try:
        h = float(input())
        p1, p2 = map(int, input().split())
        n = int(input())
        for i in range(n):
            alpha, V = map(float, input().split())
            alpha = convertDegreesToRadians(alpha)
            vx = V * cos(alpha)
            vy = V * sin(alpha)
            ts = vy / GRAVITY
            hMax = (vy ** 2) / (2 * GRAVITY) + h
            vfy = (2 * GRAVITY * hMax) ** 0.5
            td = vfy / GRAVITY
            tv = td + ts
            xMax = vx * tv
            if xMax > p1 and xMax < p2:
                print("{:.5f} -> DUCK".format(xMax))
            else:
                print("{:.5f} -> NUCK".format(xMax))
    except EOFError:
        break
