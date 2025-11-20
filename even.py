N=int(input())
flag=0
for i in range(1,N+1):
    if(i%2==0):
        flag=1
        print(i)
if flag==0:
    print(-1)    
        
  