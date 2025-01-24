# Write your solution here
list = []
how_many = int(input("How many items:"))
i = 0
while i < how_many:
    item = int(input(f"Item {i+1}:"))
    list.append(item)
    i+=1
print(list)
