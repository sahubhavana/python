def binary(N):
    if N<=1:
        return str(N)
    else:
        return binary(N//2)+str(N%2)
    
    
n=int(input())
for i in range(n):
    N=int(input())
    print(binary(N))