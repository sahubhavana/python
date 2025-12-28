N,X,Y=map(int,(input().split()))
matrix=[]

for i in range(N):
    row=list(map(int,input().split()))
    matrix.append(row)
matrix[X-1],matrix[Y-1]=matrix[Y-1],matrix[X-1]
for row in matrix:
    row[X-1],row[Y-1]=row[Y-1],row[X-1]

for row in matrix:
    for ele in row:
        print(ele, end=" ")
    print()

    
    

    