lim = int(input("Upper limit:"))
nums=[]
num = 0
tot = 0
while tot < lim:
    num += 1
    tot += num
print(tot)
