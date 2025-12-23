t=int(input())
sum=0
for i in range(t):
    l,r=map(int,input().split())
    if l>r:
        l,r=r,l
    total = (r - l + 1) * (l + r) // 2
    print(total)