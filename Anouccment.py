n=int(input())
l=list(map(int,input().split()))
rc=0 
count=0 
for x in set(l):
    count=l.count(x)
    if count>1:
        rc=rc+(count-1)
if rc==0:
    print(-1)
else:
    print(rc)