l=list(map(int,input().split()))
a=max(l)
l.remove(a)
b=max(l)
l.append(a)
sum=0
for i in range(len(l)):
    if l[i]>b:
        sum=sum+l[i]-b
    else:
        sum=sum+(b-l[i])
print(sum)