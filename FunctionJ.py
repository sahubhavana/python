def average(L):
    n=len(L)
    avg=float(sum(L)/n)
    print("{:.6f}".format(avg))


    
    
n=int(input())
L=list(map(float, input().split()))
average(L)
