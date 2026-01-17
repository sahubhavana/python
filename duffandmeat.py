n=int(input())
ans=0 
p=100
for i in range(n):
    a,b=map(int,input().split())
    p=min(p,b)
    ans=ans+(a*p)
print(ans)
    