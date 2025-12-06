import math
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())


cx1 = x1 + x2
cy1 = y1 + y2
cx2 = x3 + x4
cy2 = y3 + y4


r1_sq = (x2 - x1)**2 + (y2 - y1)**2
r2_sq = (x4 - x3)**2 + (y4 - y3)**2


d_sq = (cx2 - cx1)**2 + (cy2 - cy1)**2


if (r1_sq - 2*math.sqrt(r1_sq*r2_sq) + r2_sq) <= d_sq <= (r1_sq + 2*math.sqrt(r1_sq*r2_sq) + r2_sq):
    print("YES")
else:
    print("NO")