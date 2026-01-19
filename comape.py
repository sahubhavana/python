
def compareTriplets(a, b):
    alice=0
    bob=0 
    i=0
    for i in range(3):
        
        if(a[i]<b[i]):
            bob=bob+1
        elif (a[i]>b[i]):
            alice=alice+1
       
       
    
   
    return [alice,bob]
    
a=list(map(int,input().split()))
b=list(map(int,input().split()))
x=compareTriplets(a,b)
for i in x:
    print(i,end=" ")
