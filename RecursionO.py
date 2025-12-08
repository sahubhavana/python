def fibonaci(N):
    if N==1:
        return 0
    else:
        if N==2:
            return 1
        else:
            return fibonaci(N-1)+fibonaci(N-2)


n=int(input())
print(fibonaci(n))