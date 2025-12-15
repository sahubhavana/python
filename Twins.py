n=int(input())
l=list(map(int,input().split()))
s=sum(l)

s2=0
count=0
l.sort(reverse=True)
for i in range(len(l)):
    s2=s2+l[i]
    count=count+1
    if(s2>s-s2):
        break
    
print(count)