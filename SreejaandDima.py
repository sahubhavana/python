n = int(input())
l = list(map(int, input().split()))
l.sort(reverse=True)

sumS = sum(l[i] for i in range(0, n, 2))
sumD = sum(l[i] for i in range(1, n, 2))

print(sumS, sumD)
    
    