n = int(input())
l = list(map(int, input().split()))
l.sort()
i=0 
j=n-1
turn=0
ssum=0 
dsum=0 
for i in range(n):          
    if(i%2==0):
        ssum=ssum+l[j]
     
    else:
        dsum=dsum+l[j]
     
    j=j-1
 
print(ssum,dsum)
        
    
    
    