
def list_of_stars(listing):
    i=0
    while i < len(listing):
        print(listing[i]*"*")
        i+=1

if __name__ == "__main__":
    listing = [3, 7, 1, 1, 2]
    print(list_of_stars(listing))

#Model solution:

def list_of_stars(my_list: list):
    for number in my_list:
        print("*" * number)
