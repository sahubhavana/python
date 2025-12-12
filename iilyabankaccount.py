n=input()
op=0 
op1=0
if  '-' not in n:
    print(int(n))
else:
    op=int(n[:-1])
    op1=int(n[:-2]+n[-1])
    print(max(op,op1))
    
