n=int(input())
l=list(map(int,input().split()))
ans=[0]*n
for i in range(n):
    giver=l[i]
    ans[giver-1]=i+1
print(*ans)