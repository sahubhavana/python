def fibonaci(N):
    if N==1:
        return 0
    else:
        if N==2:
            return 1
        else:
            return fibonaci(N-1)+fibonaci(N-2)

T=int(input())
for i in range(T):
    n=int(input())
    x=fibonaci(n)
    
    if x <= 1:
        print("not prime")
    else:
        is_prime = True
        for i in range(2, int(x**0.5)+1):
            if x % i == 0:
                is_prime = False
                break

        if is_prime:
            print("prime")
        else:
            print("not prime")