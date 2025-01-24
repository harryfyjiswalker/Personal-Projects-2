# Write your solution here
def spruce(size):
    print ("a spruce!")
    i=0
    while True:
        if i < size:
           print((size-1-i)*" " + (2*i+1)*"*")
           i+=1
        if i==size:
           break
    print((size-1)*" "+ "*") 
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)
