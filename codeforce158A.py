
n, k = map(int, input().split())
arr = list(map(int, input().split()))

count = 0
threshold = arr[k-1]

for i in arr:
    if i >= threshold and i > 0:
        count += 1

print(count)
