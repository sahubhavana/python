n,k=map(int,input().split())
count=0
s=''
for i in range(1,k+1):
    s=s+str(i)
s=s+'0'
    
for i in range(n):
    t=input()
    if s in t:
        count=count+1
print(count)