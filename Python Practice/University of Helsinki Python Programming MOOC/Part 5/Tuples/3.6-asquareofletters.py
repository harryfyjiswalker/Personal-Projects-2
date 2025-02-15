A = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 9:'J', 10:'K', 11:'L', 12:'M',
     13:'N', 14:'O', 15:'P', 16:'Q', 17:'R', 18:'S', 19:'T', 20:'U', 21:'V', 22:'W', 23:'X', 24:'Y', 25:'Z'}

L = int(input("Layers: "))
rows = 2*L-1
cols = 2*L-1
 
mat = [[0 for _ in range(cols)] for _ in range(rows)]

for i in range(rows):
    for j in range(cols):
        if i == 0 or i == 2*L-2 or j == 0 or j == 2*L-2:
            mat[i][j] = abs(L-1)
        for n in range(1,2*L-1):
            if i == 0+n or i == 2*L-2-n or j == 0+n or j==2*L-2-n:
                mat[i][j] = abs(L-1-n)
                n+=1
#print(f'modified matrix is {mat}')
res = [[A[ele] for ele in sub] for sub in mat]
#print(res)

for row in res:
    for element in row:
        print(element, end="")
    print()





 
