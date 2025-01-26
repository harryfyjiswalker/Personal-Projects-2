def list_sum(a, b):
    new_list = []
    if len(a) == len(b):
        for i in range(len(a)):
            sum = a[i] + b[i]
            new_list.append(sum)
        return new_list

if __name__ == "__main__":
    a = [1,2,3]
    b=[7,8,9]
    print(list_sum(a,b))
        
