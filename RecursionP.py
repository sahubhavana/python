def logvalue(N):
    if N<=1:
        return 0
    else:
        return 1+logvalue(N//2)
         
n=int(input())
print(logvalue(n))