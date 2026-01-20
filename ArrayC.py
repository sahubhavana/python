N=int(input())
A=list(map(int, input().split()))
for i in range (len(A)):
    if(A[i]>0):
        A[i]=1
    elif(A[i]<0):
        A[i]=2
    else:
        if(A[i]==0):
            A[i]=0
for i in range(len(A)):
    print(A[i],end=" ")