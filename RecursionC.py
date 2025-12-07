def nTO(N):
    if N <= 0:
        return
    if N == 1:
        print(1, end='')   
        return
    print(N, end=' ')
    nTO(N - 1)

       
        
N=int(input())
nTO(N)