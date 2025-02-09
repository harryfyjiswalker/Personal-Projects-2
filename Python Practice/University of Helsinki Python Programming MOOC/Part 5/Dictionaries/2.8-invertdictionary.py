def invert(dictionary: dict):
    inverted = {v: k for k, v in dictionary.items()}
    dictionary.clear()  
    dictionary.update(inverted)  

if __name__ == "__main__":
    s = {1: 10, 2: 20, 3: 30}
    invert(s)  
    print(s)  
