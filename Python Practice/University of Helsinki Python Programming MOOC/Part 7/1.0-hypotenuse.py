from math import sqrt

def hypotenuse(leg1: float, leg2: float):
    lengthsq = leg1**2 + leg2**2
    length = sqrt(lengthsq)
    return length
