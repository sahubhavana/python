n,k=map(int,input().split())
a=list(map(int,input().split()))
threshold=a[k-1]
count=0 
for score in a:
    if score>=threshold and score>0:
        count=count+1
print(count)