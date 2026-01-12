import math

# Input
f1, f2 = input().split()

a1, b1 = map(int, f1.split('/'))
a2, b2 = map(int, f2.split('/'))

# LCM of numerators
lcm_num = (a1 * a2) // math.gcd(a1, a2)

# GCD of denominators
gcd_den = math.gcd(b1, b2)

num = lcm_num
den = gcd_den

# Reduce the fraction
g = math.gcd(num, den)
num //= g
den //= g

print(f"{num}/{den}")



