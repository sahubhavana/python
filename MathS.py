import math
area=0
s=0
A,B,C=map(int,input().split())
if(A+B>C and B+C>A and C+A>B):
    s = (A + B + C) / 2
    area = math.sqrt(s * (s - A) *(s -B ) * (s - C))
    print("Valid")
    print(area)
else:
    print("Invalid")