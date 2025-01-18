lim = int(input("Upper limit:"))
text = ""
num = 1
tot = 0
while (1+tot) < lim:
    num += 1
    tot += num
    text += f"+ {num} "
print(f"The consecutive sum: 1 {text}= {1+tot}")
