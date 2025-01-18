print("Please type in integer numbers. Type in 0 to finish.")
nums = []
numpos = []
numneg = []
while True:
    num = int(input("Number:"))
    if num > 0:
        numpos.append(num)
    if num < 0:
        numneg.append(num)
    if num == 0:
        break
    nums.append(num)
print(f"... the program asks for numbers\nNumbers typed in {len(nums)}")
print(f"The sum of the numbers is {sum(nums)}")
print(f"The mean of the numbers is {sum(nums)/len(nums)}")
print(f"Positive numbers {len(numpos)}")
print(f"Negative numbers {len(numneg)}")

#Model solution:

print("Please type in integer numbers. Type in 0 to finish.")
numbers = 0
sum = 0
positives = 0
 
while True:
    number = int(input("Number: "))
    if number == 0:
        break
    numbers += 1
    sum += number
    if number>0:
        positives += 1
 
print("Numbers typed in", numbers)
print("The sum of the numbers is", sum)
print("The mean of the numbers is", sum/numbers)
print("Positive numbers", positives)
print("Negative numbers", numbers-positives)
 
