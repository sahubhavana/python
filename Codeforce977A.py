
n, k = map(int, input().split())

for i in range(k):
    num = n % 10

    if num != 0:
        n = n - 1
    else:
        n = n // 10

print(n)
