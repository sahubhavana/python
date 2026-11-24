
n = int(input())

for i in range(n):
    s = input()

    if len(s) > 10:
        count = len(s) - 2
        print(s[0] + str(count) + s[-1])
    else:
        print(s)
