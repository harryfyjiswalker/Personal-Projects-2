studentinfo = input("Student information: ")
exercisescompleted = input("Exercises completed: ")
exampoints1 = input("Exam points: ")

import math

grades = {}
names = {}
exampoints = {}
namesgradespoints = {}
totpoints = {}
totalstats = {}
#exercises
with open(f"{exercisescompleted}") as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(';')
        if parts[0] != 'id':
            grades[parts[0]] = parts[1:len(line)]
    #print(grades)

#names
with open(f"{studentinfo}") as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(';')
        if parts[0] != 'id':
            names[parts[0]] = parts[1] + " " + parts[2]
    #print(names)

#exampoints
with open(f"{exampoints1}") as new_file:
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
                fingrade = []
                namesgradespoints[b] = [list(map(int, v)), list(map(int,d)), fingrade]
#print(namesgradespoints)

#exercisepoints
# print(namesgradespoints)
for d, e in namesgradespoints.items():
    total_points = math.floor(0.25 * sum(e[0])) + sum(e[1])
    # Check conditions and assign values to namesgradespoints[d][2]
    if 0 <= total_points <= 14:
        namesgradespoints[d][2].append(0)
    elif 15 <= total_points <= 17:
        namesgradespoints[d][2].append(1)
    elif 18 <= total_points <= 20:
        namesgradespoints[d][2].append(2)
    elif 21 <= total_points <= 23:
        namesgradespoints[d][2].append(3)
    elif 24 <= total_points <= 27:
        namesgradespoints[d][2].append(4)
    elif total_points >= 28:
        namesgradespoints[d][2].append(5)

for k, v in namesgradespoints.items():
    totalstats[k] = [sum(v[0]), math.floor(0.25*sum(v[0])), sum(v[1]), (math.floor(0.25*sum(v[0])) + sum(v[1])), *v[2]]
word1 = "exec_nbr"
word2 = "exec_pts."
word3 = "exm_pts."
word4 = "tot_pts."
word5 = "grade"
word6 = "name"

# print(f"{word6:30}{word1:10}{word2:10}{word3:10}{word4:10}{word5:10}")
# for k, v in totalstats.items():
#     print(f"{k:30}{totalstats[k][0]}{totalstats[k][1]:10}{totalstats[k][2]:10}{totalstats[k][3]:10}{totalstats[k][4]:10}")

print(f"{word6:30}{word1:10}{word2:10}{word3:10}{word4:10}{word5:10}")
for k, v in totalstats.items():
    print(f"{k:30}{totalstats[k][0]:<10}{totalstats[k][1]:<10}{totalstats[k][2]:<10}{totalstats[k][3]:<10}{totalstats[k][4]:<10}")


