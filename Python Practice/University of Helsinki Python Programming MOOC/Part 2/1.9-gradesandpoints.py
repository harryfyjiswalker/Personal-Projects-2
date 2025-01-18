points = int(input("How many points [0-100]:"))
if points > 100:
    print("Grade: impossible!")
if 90 <= points <= 100:
    print("Grade: 5")
if 80 <= points < 90:
    print("Grade: 4")
if 70 <= points < 80:
    print("Grade: 3")
if 60 <= points < 70:
    print("Grade: 2")
if 50 <= points < 60:
    print("Grade: 1")
if 0 <= points < 50:
    print("Grade: fail")
if points < 0:
    print("Grade: impossible!")
