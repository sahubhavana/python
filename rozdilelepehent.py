n=int(input())
l=list(map(int,input().split()))
mn=min(l)
if l.count(mn)==1:
    print(l.index(mn)+1)
else:
    if l.count(mn)>1:
        print("Still Rozdil")