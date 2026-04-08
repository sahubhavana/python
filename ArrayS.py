N=input()
current=""
pointer=0
start=0
A=[]
for i in range(N):
    if A[i]=="L":
        pointer=pointer+1
    elif A[i]=="R":
        pointer=pointer-1
    if pointer==0:
        A.append(N[start:i+1])
        start=i+1

    

        
    
        