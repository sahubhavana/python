N = int(input())
S = input().strip()

count = 1  # first character is always taken

for i in range(1, N):
    if S[i] != S[i - 1]:
        count += 1

print(count)