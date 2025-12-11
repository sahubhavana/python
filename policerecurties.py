n=int(input())
l=list(map(int,input().split()))
crime=0
police=0
for i in l:
    if i>0:
        police=police+i
    else: 
        if police>0:
            police=police-1
           
        else:
            crime=crime+1
        
   
     
print(crime)
        