t=int(input())
for i in range(t):
    N=int(input())
    A=list(map(int, input().split()))
    sum=0
    for i in range(1,N):
        for j in range(i+1,N):
            sum=sum+(A[i]+A[j]+j-i)
           
        print(sum)        
                
         
    