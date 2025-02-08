import math

def factorials(n: int):
    dict = {}
    for i in range(1,n+1):
        dict[i] = math.factorial(i)
    return dict
