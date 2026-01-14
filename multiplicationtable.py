n,x=map(int,input().split())
count=0
for i in range(1,n+1):
    if (x%i==0):
        if x//i<=n:
            count=count+1
print(count)