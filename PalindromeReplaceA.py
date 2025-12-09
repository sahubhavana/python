s=list(input().strip())
n=len(s)
j=n-1
i=0
p=True
while i<=j:
    if(s[i] =='?'and s[j]=='?'):
        s[i]='a'
        s[j]='a'
    elif s[i]=='?':
            s[i]=s[j]
    elif s[j]=='?':
        s[j]=s[i]
    elif s[i]!=s[j]:
         p=False
         break
    i=i+1
    j=j-1
a=""
if p:
    for i in s:
        a=a+i
    print(a)
      
else:
    print(-1)
