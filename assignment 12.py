import math
t=int(input("entet test case"))
for i in range(t):
	a,b=input().split()
	a=int(a)
	b=int(b)
    print(math.gcd(a,b))
    print(math.lcm(a,b))
