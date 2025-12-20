a=list(input().split())
b=list(input().split())
j=0
l=[]
if len(a)!=len(b):
    print("NO")
for i in range(len(a)):
    if a[i]!=b[i]:
        l.append(i)
if len(l)==2:
    for i in l:
        a[i]=b[i]
if (a==b):
    print("YES")
else:
    print("NO")