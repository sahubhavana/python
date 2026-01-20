N=int(input())
n=list(map(int, input().split()))
x=int(input())
flag=0
for i in range(len(n)):
    if(n[i]==x):
        print(i)
        flag=1
        break
if(flag==0):
    print(-1)
     
            
            
                 
    