studentinfo = input("Student information: ")
exercisescompleted = input("Exercises completed: ")
exampoints1 = input("Exam points: ")

import math

# studentinfo =  'students1.csv' #input("Student information: ") 
#exercisescompleted = 'exercises1.csv' #input("Exercises completed: ")
# exampoints = 'exam_points1.csv' #input("Exam points: ")

grades = {}
names = {}
exampoints = {}
namesgradespoints = {}
#exercises
with open(f'{exercisescompleted}') as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(';')
        if parts[0] != 'id':
            grades[parts[0]] = parts[1:len(line)]
    #print(grades)

#names
with open(f'{studentinfo}') as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(';')
        if parts[0] != 'id':
            names[parts[0]] = parts[1] + " " + parts[2]
    #print(names)

#exampoints
with open(f'{exampoints1}') as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(';')
        if parts[0] != 'id':
            exampoints[parts[0]] = parts[1:len(line)]
    #print(exampoints)

for k, v in grades.items():
    for a, b in names.items():
        for c, d in exampoints.items():
            if k == a == c:
                namesgradespoints[b] = list(map(int, v)), list(map(int,d))
#print(namesgradespoints)

#exercisepoints
#print(namesgradespoints)
for k, v in namesgradespoints.items():
    if 0 <= math.floor(0.25*sum(v[0])) + sum(v[1]) <= 14:
        print(f"{k} 0")
    elif 15 <= math.floor(0.25*sum(v[0])) + sum(v[1]) <= 17:
        print(f"{k} 1")  
    elif 18 <= math.floor(0.25*sum(v[0])) + sum(v[1]) <= 20:
        print(f"{k} 2")  
    elif 21 <= math.floor(0.25*sum(v[0])) + sum(v[1]) <= 23:
        print(f"{k} 3")
    elif 24 <= math.floor(0.25*sum(v[0])) + sum(v[1]) <= 27:
        print(f"{k} 4")
    elif 28 <= math.floor(0.25*sum(v[0])) + sum(v[1]):
        print(f"{k} 5")


