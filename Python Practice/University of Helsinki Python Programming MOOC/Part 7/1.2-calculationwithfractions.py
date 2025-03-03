from fractions import Fraction

def fractionate(amount:int):
    listofanswers = []
    answer = Fraction(1,amount)
    listofanswers.append(answer)
    listofanswers = listofanswers * amount
    return listofanswers

if __name__ == "__main__":
    for p in fractionate(3):
        print(p)

    print()

    print(fractionate(5))
