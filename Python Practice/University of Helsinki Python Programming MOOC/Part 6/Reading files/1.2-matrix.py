
# with open("/Users/harryfyjis-walker/Library/Application Support/tmc/vscode/mooc-programming-24/part06-03_matrix/matrix.txt") as new_file:
#     contents = new_file.read()
#     print(contents)

def matrix_sum():
    with open('matrix.txt') as new_file:
        sum = 0
        for line in new_file:
            line = line.replace("\n", "")
            elements = line.split(",")
            for element in elements:
                sum += float(element)
        return int(sum)

def matrix_max():
    with open('matrix.txt') as new_file:
        max = 0
        for line in new_file:
            line = line.replace("\n", "")
            elements = line.split(",")
            for element in elements:
                if float(element) > max:
                    max = float(element)
        return int(max)

def row_sums():
    list1 = []
    with open('matrix.txt') as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            elements = list(map(int,line.split(",")))
            list1.append(sum(elements))
        return list1



if __name__ == "__main__":
    print(matrix_sum())
    print(matrix_max())
    print(row_sums())
