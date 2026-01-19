n=int(input())
s=input().strip()
l=list(map(int,input().split()))
xl=0
xr=0
ans=float('inf')
j=0
st=[]

for i in range(n):
    if s[i]=="R":
        st.append(l[i])
    elif s[i]=="L":
        if st:
            xr=st.pop()
            time=(l[i]-xr)//2
            ans=min(time,ans)
if ans == float('inf'):
    print(-1)
else:
    print(ans)