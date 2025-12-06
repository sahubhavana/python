T = int(input())  # number of test cases

for _ in range(T):
    N = int(input())
    
    # Initialize intersection boundaries
    intersect_x1 = -10**5
    intersect_y1 = -10**5
    intersect_x2 = 10**5
    intersect_y2 = 10**5
    
    for _ in range(N):
        x1, y1, x2, y2 = map(int, input().split())
        intersect_x1 = max(intersect_x1, x1)
        intersect_y1 = max(intersect_y1, y1)
        intersect_x2 = min(intersect_x2, x2)
        intersect_y2 = min(intersect_y2, y2)
    
    # Compute area
    width = max(0, intersect_x2 - intersect_x1)
    height = max(0, intersect_y2 - intersect_y1)
    area = width * height
    print(area)