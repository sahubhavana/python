
T = int(input())

for _ in range(T):
    n, s = map(int, input().split())

    max_sum = n * (n + 1) // 2
    if s > max_sum:
        print(-1)
        continue

    ans = []
    while s > 0 and n > 0:
        x = min(n, s)
        ans.append(x)
        s -= x
        n = x - 1

    print(len(ans), *ans)
