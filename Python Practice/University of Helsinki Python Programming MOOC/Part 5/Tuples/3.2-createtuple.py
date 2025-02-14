import math

def create_tuple(x: int, y: int, z: int):
    numbers = [x,y,z]
    numbers.sort()
    tuple1 = (numbers[0], numbers[2], sum(numbers))
    return tuple1

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))
