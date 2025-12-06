import math

R, S = map(int,input().split())

diagonal_square = S * math.sqrt(2)
diameter_circle = 2 * R

if diagonal_square <= diameter_circle:
    print("Circle")
elif diameter_circle <= S:
    print("Square")
else:
    print("Complex")
