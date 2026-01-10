import math
t=int(input())
for i in range(t):
    n,s=map(int,input().split())
    mx=max(n,s)
    mn=min(n,s)
    sum=0
    for i in range(mn,mx):
        if(i<=n):
            sum=sum+i
            if(sum==s):
                print(i,end=" ")
    
        
    