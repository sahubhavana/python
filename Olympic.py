n = int(input())
skills = list(map(int, input().split()))

c1 = skills.count(1)
c2 = skills.count(2)
c3 = skills.count(3)

teams = min(c1, c2, c3)
print(teams)

if teams == 0:
    exit()

used = [False] * n
i = 0

while teams > 0:
    team = []
    for skill in [1, 2, 3]:
        for j in range(n):
            if not used[j] and skills[j] == skill:
                team.append(j + 1)
                used[j] = True
                break
    print(*team)
    teams -= 1
    