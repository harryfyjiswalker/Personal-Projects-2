studentinfo = input("Student information: ")
exercisescompleted = input("Exercises completed: ")

grades = {}
names = {}
namesandgrades = {}
with open(f"{exercisescompleted}") as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(';')
        if parts[0] != 'id':
            grades[parts[0]] = parts[1:len(line)]
    #print(grades)

with open(f"{studentinfo}") as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(';')
        if parts[0] != 'id':
            names[parts[0]] = parts[1] + " " + parts[2]
    #print(names)

for k, v in grades.items():
    for a, b in names.items():
        if k == a:
            namesandgrades[b] = list(map(int, v))
#print(namesandgrades)
for k, v in namesandgrades.items():
    print(f"{k} {sum(v)}")


