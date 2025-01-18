year = int(input("Give year:"))
original = year
nextyear = year+1
leap = nextyear % 4 == 0 and nextyear %100 != 0 or nextyear % 100 == 0 and nextyear % 400 ==0

while not leap:
    nextyear += 1
    leap = nextyear % 4 == 0 and nextyear %100 != 0 or nextyear % 100 == 0 and nextyear % 400 ==0

print(f"The next leap year after {original} is {nextyear}")

#Model solution:

start_year = int(input("Year: "))
year = start_year + 1
while True:
    if year % 100 == 0:
        if year % 400 == 0:
            break
    elif year % 4 == 0:
        break
 
    year += 1
 
print(f"The next leap year after {start_year} is {year}")
