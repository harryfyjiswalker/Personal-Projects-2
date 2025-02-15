def largest():
    with open("numbers.txt") as new_file:
        n = 1
        largest = []
        for line in new_file:
            line = line.replace("\n", "")
            largest.append(int(line))
            n += 1
    return max(largest)
