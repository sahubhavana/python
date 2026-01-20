T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    result = []                                     


    for i in range(N):
        max_val = A[i]
        for j in range(i, N):
            max_val = max(max_val, A[j])
            result.append(max_val)

    print(*result)
        
