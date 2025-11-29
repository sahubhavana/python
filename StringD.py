A=input()
B=input()
print(len(A), len(B))
print(A+B)
c=[]
c1=[]
a=A[0]
b=B[0]
for i in range(len(A)):
    c.append(A[i])
    
for i in range(len(B)):
    c1.append(B[i])
c1[0]=a 
c[0]= b  
S="" 
S1=""
for i in c:
    S=S+i
   
for i in c1:
   S1=S1+i
   
print(S, S1)