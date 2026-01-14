n = int(input())
l = list(map(int, input().split()))

mx = max(l)
mn = min(l)

# index of first max
pos_max = l.index(mx)

# index of last min
pos_min = n - 1 - l[::-1].index(mn)

# swaps to bring max to front
swaps = pos_max

# swaps to bring min to end
# if max is before min, one position shifts after moving max
if pos_max < pos_min:
    swaps += (n - 1 - pos_min)
else:
    swaps += (n - 1 - pos_min - 1)

print(swaps)