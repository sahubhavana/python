n=int(input())
s=input()
l=list(map(int,input().split()))
s1=s.split()
time=0
INF=10**18
ans=INF

for i in range(n-1):
    if(s[i]=='R' and s[i+1]=='L'):
        
        time=((l[i+1]-l[i])//2)
        ans=min(time,ans)
    
if ans==INF:
    print((-1))
    
else:
    print(ans)