X1,Y1,X2,Y2,X3,Y3,X4,Y4=map(int,input().split())
xmin = min(X1, X2, X3, X4)
xmax = max(X1, X2, X3, X4)
ymin = min(Y1, Y2, Y3, Y4)
ymax = max(Y1,Y2,Y3,Y4)

# Number of points
N = int(input())

# Check each point
for _ in range(N):
    px, py = map(int, input().split())
    if xmin <= px <= xmax and ymin <= py <= ymax:
        print("YES") # point lies inside or on the rectangle
    else:
        print("NO")   # point l