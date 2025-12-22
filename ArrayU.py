N,M=map(int,(input().split()))
A=list(map(int, input().split()))
B=list(map(int, input().split()))
n=len(A)
m=len(B)    
i=0
j=0

while(i<n and j<m):
        if(A[i]==B[j]):
            j=j+1
        i=i+1
        
if j == m:
    print("YES")
else:
    print("NO") 
        
