n,k=map(int,input().split())
total=0
for i in range(n):
    l,r=map(int,input().split())
    total=total+(r-l+1)
answer = (k - (total % k)) % k   
print(answer)