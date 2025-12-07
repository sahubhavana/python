def nTO(N):
    if N==0:
        return
    else:
        
        nTO(N-1)
        print(N)
        
N=int(input())
nTO(N)