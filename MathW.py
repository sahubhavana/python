import math
x1, y1, x2, y2 = map(int, input().split())

# Input for circle B
x3, y3, x4, y4 = map(int, input().split())

# Centers
cx1 = (x1 + x2) / 2
cy1 = (y1 + y2) / 2

cx2 = (x3 + x4) / 2
cy2 = (y3 + y4) / 2

# Radii
r1 = math.dist((x1, y1), (x2, y2)) / 2
r2 = math.dist((x3, y3), (x4, y4)) / 2

# Distance between centers
d = math.dist((cx1, cy1), (cx2, cy2))

# Intersection check
if abs(r1 - r2) <= d <= (r1 + r2):
    print("YES")
else:
    print("NO")