import math
n = int(input())
l = list(map(int, input().split()))

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

for x in l:
    root = int(math.sqrt(x))
    if root * root == x and is_prime(root):
        print("YES")
    else:
        print("NO")