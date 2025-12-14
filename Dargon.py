s,n=map(int,input().split())
dargon=[]
for i in range(n):
    x,y=map(int,input().split())
    dargon.append((x,y))
    
dargon.sort()
for x,y in dargon:
    if s>x:
        s=s+y
    else:
        print("NO")
        break
else:
    print("YES")    
    