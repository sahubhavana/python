    n=len(arr)
    i=0
    j=0
    sum=0
    while i<n:
        sum=sum+arr[i][j]
        i=i+1
        j=j+1
    i=0
    j=n-1
    sum1=sum
    sum=0
    while i<n:
        sum=sum+arr[i][j]
        i=i+1
        j=j-1
    return(abs(sum1-sum))
    
n=int(input())
m=[]
for i in range(n):
    row=list(map(int,input().split()))
    m.append(row)
x=diagonalDifference(m)
print(x)

