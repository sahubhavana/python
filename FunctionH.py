def ntime(N,c):
    print(" ".join(c * N))
    
    
t=int(input())
for i in range(t):
    N,c=input().split()
    N=int(N)
    c=str(c)
    ntime(N,c)   