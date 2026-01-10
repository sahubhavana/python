def summatrix(matrix1,matrix2,i=0,smatrix=[]):
    if i>len(matrix1) and len(matrix2):
        return smatrix
    else:
        s=s+matrix1[i]+matrix2[i]
        smatrix.append(s)
        summatrix(matrix1,matrix2,i=i+1,)
    
    



R,C=map(int,input().split())

matrix1=[]
for i in range(R):
    row=list(map(int,input().split()))
    matrix1.append(row)
    

matrix2=[]
for i in range(R):
    row=list(map(int,input().split()))
    matrix2.append(row)
    
print(matrix1)
print(matrix2)