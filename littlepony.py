import math
m,n=map(int,input().split())
ans=0.0
for i in range(1,m+1):
    ans=ans+1.0-math.pow((i-1)/m,n)

print(ans)