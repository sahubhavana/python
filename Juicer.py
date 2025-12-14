n,b,d=map(int,input().split())
l=list(map(int,input().split()))
throw=0
juicer=0
count=0
for i in range(len(l)):
    if l[i]<=b:
        juicer=juicer+1
        throw=throw+l[i]
        if throw>d:
            throw=0
            count=count+1
    else:
        if l[i]>b:
            continue      
print(count)