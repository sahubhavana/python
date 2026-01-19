n=int(input())
l=list(map(int,input().split()))
count=1
maxlen=1
for i in range(1,n):
    if(l[i]>l[i-1]):
        count=count+1
    else:
        count=1
    
maxlen=max(maxlen,count)
print(maxlen)