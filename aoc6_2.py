import re
import math

def solve_equation(n, res):
    a = -1
    b = n
    c = -res

    if b**2 - 4*a*c < 0:
        return None, None

    discriminant = math.sqrt(b**2 - 4*a*c)
    x1 = (-b + discriminant) / (2*a)
    x2 = (-b - discriminant) / (2*a)

    return x1, x2

with open("in6.txt", "r") as file:
    time = int(re.sub(r'\s+', '', file.readline().split(':')[1]))
    distance = int(re.sub(r'\s+', '', file.readline().split(':')[1]))
    x1, x2 = solve_equation(time, distance)
    res = math.ceil(x2 - 1) - int(x1 + 1) + 1
    print(res)
    