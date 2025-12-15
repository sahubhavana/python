n,m=map(int,input().split())
l=list(map(int,input().split()))
l.sort()

ans=l[n-1]-l[0]

for i in range(m-n+1):
    ans=min(ans,l[i+n-1]-l[i])
    
print(ans)