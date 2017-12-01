from math import sqrt


def get_roots(a, b, c):
    quadrat = 2
    discriminant = b ** quadrat - 4 * a * c
    root1 = (-b - sqrt(abs(discriminant))) / (quadrat * a)
    root2 = (-b + sqrt(abs(discriminant))) / (quadrat * a)
    if discriminant == 0:
        return root1, None
    elif discriminant < 0:
        return None, None
    else:
        return root1, root2
