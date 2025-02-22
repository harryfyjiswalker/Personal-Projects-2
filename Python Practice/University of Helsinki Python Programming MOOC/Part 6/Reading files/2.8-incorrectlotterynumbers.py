import re

def filter_incorrect():
    dictionary = {}
    correct = {}
    with open("lottery_numbers.csv") as file:
        for line in file:
            line = line.replace("\n", "")
            parts = re.split(r'[;,]', line)
            weeks = parts[0][5:]
            try:
                weeksint = int(weeks)
            except ValueError:
                weeksint = weeks
            numbers = parts[1:]
            dictionary[weeksint] = numbers
        
        for k,v in dictionary.items():
            for i in range(len(v)):
                try:
                    v[i] = int(v[i])
                except ValueError:
                    v[i] = v[i]

    with open("correct_numbers.csv", "w") as file1:
        for k,v in dictionary.items():
                if k in range(1,53):
                    if len(v) == 7:
                        if all(isinstance(x, int) for x in v):
                            if all(x in range(1, 39) for x in v):
                                if len(set(v)) == len(v): #ensure no duplicates
                                    correct[k] = v

        for k,v in correct.items():
            file1.write(f"week {k};{','.join(map(str, v))}\n")
        
                
            
