def name(N):
    if N==0:
        return 
    else:
        print("I love Recursion")
        name(N-1)
    
    
N=int(input())
name(N)