import math
while True:
    num = int(input("Please type in a number:"))
    if num > 0:
        i = 1
        nums = []
        while i <= num:
            nums.append(i)
            i += 1
        print(f"The factorial of the number {num} is {math.prod(nums)}")
    else:
        break
print("Thanks and bye!")

