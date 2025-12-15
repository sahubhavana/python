n = int(input())
arr = list(map(int, input().split()))

from collections import Counter

freq = Counter(arr)
mx = max(freq.values())
if mx>((n+1)//2):
    print("NO")
else:
    print("YES")