import math
import random
lcup=list(map(int,input().split()))
lmedal=list(map(int,input().split()))
n=int(input())
a=math.ceil(sum(lcup)/5)
b=math.ceil(sum(lmedal)/10)
if (a+b)<=n:
    print("YES")
else:
    print("NO")