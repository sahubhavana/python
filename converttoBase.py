T = int(input())
N, X = input().split()
X = int(X)

digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

if T == 1:
    # base X to decimal
    print(int(N, X))

else:
    # decimal to base X
    n = int(N)
    if n == 0:
        print(0)
    else:
        result = ""
        while n > 0:
            result = digits[n % X] + result
            n //= X
        print(result)
