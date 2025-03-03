from random import shuffle

def roll(die:str):
    if die == "A":
        numbers = [3,3,3,3,3,6]
        shuffle(numbers)
        return numbers[0]
    if die == "B":
        numbers = [2,2,2,5,5,5]
        shuffle(numbers)
        return numbers[0]
    if die == "C":
        numbers = [1,4,4,4,4,4]
        shuffle(numbers)
        return numbers[0]
    
def play(die1: str, die2: str, times: int):
    list1 = []
    die1wins = 0
    die2wins = 0
    ties = 0
    for i in range(times):
        list1.append((roll(die1), roll(die2)))
    for i in range(len(list1)):
        if list1[i][0]>list1[i][1]:
            die1wins +=1
        if list1[i][0]<list1[i][1]:
            die2wins +=1
        if list1[i][0]==list1[i][1]:
            ties +=1
    return (die1wins, die2wins, ties)




if __name__ == "__main__":
    result = play("A","C",20)
    print(result)
