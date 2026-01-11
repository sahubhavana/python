r,c=map(int,input().split())
m=[input() for i in range(r)]

rows=[i for i in range(r) if 'S' not in m[i]]
clos=[j for j in range(c) if all(m[i][j] != 'S' for i in range(r))]
ans = 0
for i in range(r):
    for j in range(c):
        if i in rows or j in clos:
            ans += 1

print(ans)