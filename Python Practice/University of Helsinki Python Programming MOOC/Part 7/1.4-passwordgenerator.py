import random
from string import ascii_lowercase

def generate_password(length=8):
    return ''.join(random.choice(ascii_lowercase) for _ in range(length))

if __name__ == "__main__":
    for i in range(10):
        print(generate_password(8))
