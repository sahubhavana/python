N,K=map(int,input().split())
l=list(map(int,input().split()))
n=len(l)
mn=0
for i in range(0,N,K):
    group=l[i:i+K]
    print(min(group),end=" ")