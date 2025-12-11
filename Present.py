n=int(input())
l=list(map(int,input().split()))
a=[0]*n
for i in range(n):
    s=l[i]
    a[s-1]=i+1
    
print(*a)