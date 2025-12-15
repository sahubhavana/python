s = input()

if s == s[::-1]:
    print(len(s) - 1)
else:
    print(len(s))