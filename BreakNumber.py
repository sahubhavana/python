n=int(input())
l=list(map(int,input().split()))
max_f=0
for i in l:
    count=0
    while i%2==0:
            i=i//2
            count=count+1
    max_f=max(count,max_f)
print(max_f)