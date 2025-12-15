n=int(input())
m=list(map(int,input().split()))
mn=0 
mx=0 
for i in range(n):
    if i==0:
        mn=m[1]-m[0]
    elif i==n-1:
        mn=(m[n-1]-m[n-2])
    else:
        mn=min(m[i]-m[i-1],m[i+1]-m[i])
        
    mx=max(m[i]-m[0],m[n-1]-m[i])
    print(mn,mx)  