N, M = map(int, input().split())

matrix = []
for i in range(N):
    row = list(input().strip())
    matrix.append(row)

x, y = map(int, input().split())

directions = [
    (-1, 0), (1, 0), (0, -1), (0, 1),
    (-1, -1), (-1, 1), (1, -1), (1, 1)
]

found = False
for dx, dy in directions:
    nx = x + dx
    ny = y + dy
    if 0 <= nx < N and 0 <= ny < M:
        if matrix[nx][ny] == 'X':
            found = True
            break

if found:
    print("yes")
else:
    print("no")
    
            
