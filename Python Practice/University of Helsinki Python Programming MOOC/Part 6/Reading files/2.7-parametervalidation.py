def new_person(name:str, age:int):
    numwords = len(name.split())
    if name == "" or numwords < 2 or len(name) > 40 or age < 0 or age > 150:
        raise ValueError
    else:
        tup = (name, age)
        return tup


if __name__ == "__main__":
    print(new_person("Daniel Atege", 40))
