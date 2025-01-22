num = int(input("Please type in a number: "))
i = 1
counter = 0

if num % 2 == 0:
    while True:
        print(i)
        print(num - (i - 1))
        i += 1
        counter += 1
        if counter == num / 2:
            break
else:
    while True:
        print(i)
        print(num - (i - 1))
        i += 1
        counter += 1
        if counter == (num - 1) / 2:
            break
    print((num + 1) // 2)

#Simpler:
number = int(input("Please type in a number: "))
 
left = 1
right = number
 
while left < right:
    print(left)
    print(right)
    left += 1
    right -= 1
 
if left == right:
    print(left)
