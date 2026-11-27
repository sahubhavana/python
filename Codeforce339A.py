s=input()
l=s.split("+")
l1=[]
for i in l:
    l1.append(int(i))
l1.sort()

ans = "+".join(map(str, l1))

print(ans)
