studentinfo = input("Student information: ")#"students1.csv" 
exercisescompleted = input("Exercises completed: ")#"exercises1.csv" 
exampoints1 = input("Exam points: ")#"exam_points1.csv" 
courseinformation = input("Course information: ") #course1.txt"

import math

grades = {}
names = {}
exampoints = {}
namesgradespoints = {}
totpoints = {}
totalstats = {}
numnamegrades = {}


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
        parts1 = line.split(';')
        if parts1[0] != 'id':
            names[parts1[0]] = parts1[1] + " " + parts1[2]
    print(names)


#exampoints
with open(f"{exampoints1}") as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts2 = line.split(';')
        if parts2[0] != 'id':
            exampoints[parts2[0]] = parts2[1:len(line)]
    #print(exampoints)

for k, v in grades.items():
    for a, b in names.items():
        for c, d in exampoints.items():
            if k == a == c:
                fingrade = []
                studentnumber = []
                namesgradespoints[b] = [list(map(int, v)), list(map(int,d)), fingrade, studentnumber]
#print(namesgradespoints)

#exercisepoints

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

for f,g in namesgradespoints.items():
    for h, i in names.items():
        if f == i:
            namesgradespoints[f][3].append(h)
print(namesgradespoints)

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

summing = f"{word6:30}{word1:10}{word2:10}{word3:10}{word4:10}{word5:10}"
for k, v in totalstats.items():
    scores = f"{k:30}{totalstats[k][0]:<10}{totalstats[k][1]:<10}{totalstats[k][2]:<10}{totalstats[k][3]:<10}{totalstats[k][4]:<10}"

with open(f"{courseinformation}") as courseinfo:
    course = []
    for line in courseinfo: 
        line = line.replace("\n", "")
        parts = line.split(': ')
        course.append(parts[1])
    descript = f"{course[0]}, {course[1]} credits"
with open("results.txt", "w") as results:
    results.write(f"{descript}\n")
    lineofequals = "="*len(descript)
    results.write(f"{lineofequals}\n")
    summing = f"{word6:30}{word1:10}{word2:10}{word3:10}{word4:10}{word5:10}"
    results.write(f"{summing}\n")
    for k, v in totalstats.items():
        scores = f"{k:30}{totalstats[k][0]:<10}{totalstats[k][1]:<10}{totalstats[k][2]:<10}{totalstats[k][3]:<10}{totalstats[k][4]:<10}"
        results.write(f"{scores}\n")
with open("results.csv", "w") as results1:
    for k, v in namesgradespoints.items():
        overall = f"{namesgradespoints[k][3][0]};{k};{namesgradespoints[k][2][0]}"
        results1.write(f"{overall}\n")

print("Results written to file results.txt and results.csv")
