import math
for i in range(3):
    N,M=map(int,input().split())
    if N >0 and M>0:
        mx=max(N,M) 
        mn=min(N,M)
        sum=0
        for i in range(mn,mx+1):
            sum=sum+i
            print(i,end=" ")  
        print('sum ',  end="=",)
        print(sum)
        
    else:
        break