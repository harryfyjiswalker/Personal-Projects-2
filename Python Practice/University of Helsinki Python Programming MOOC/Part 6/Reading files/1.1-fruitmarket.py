def read_fruits():
    with open("fruits.csv") as new_file:
        dict = {}
        lines = 0
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            fruits = parts[0]
            price = parts[1]
            dict[fruits] = round(float(price),2)
            lines += 1

            # for line in new_file:
            #     fruit = parts[0]
            #     price = parts[1]
        return dict
    
