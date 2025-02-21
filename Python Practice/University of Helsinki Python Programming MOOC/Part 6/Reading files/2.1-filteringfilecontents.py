def filter_solutions():
    with open("solutions.csv") as new_file:
        # contents = new_file.read()
        # print(contents)
        with open("correct.csv", "w") as correct:
            with open("incorrect.csv", "w") as incorrect:
                for line in new_file:
                    line = line.replace("\n", "")
                    parts = line.split(";")
                    if eval(parts[1]) == int(parts[2]):
                        correct.write(f"{line}\n")
                    else:
                        incorrect.write(f"{line}\n")

if __name__ == "__main__":
    filter_solutions()
