import math
numstudents = int(input("How many students on the course?"))
group = int(input("Desired group size?"))
print(f"Number of groups formed: {math.ceil(numstudents/group)}")
