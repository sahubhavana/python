from itertools import permutations

def calc(x, y, op):
    if op == '+':
        return x + y
    if op == '-':
        return x - y
    return x * y  # op == '*'

a, b, c, d = map(int, input().split())

ops = ['+', '-', '*']

# Try all permutations of two operators
for op1, op2 in permutations(ops, 2):
    # (a op1 b) op2 c
    if calc(calc(a, b, op1), c, op2) == d:
        print("YES")
        break

    # a op1 (b op2 c)
    if calc(a, calc(b, c, op2), op1) == d:
        print("YES")
        break
else:
    print("NO")