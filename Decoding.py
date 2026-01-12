n=int(input())
s=input()
result = ""
i = 0
size = len(s)

while size > 0:
    if size % 2 == 0:
        result = s[i] + result     # add to front
    else:
        result = result + s[i]     # add to end
    i += 1
    size -= 1
print(result)