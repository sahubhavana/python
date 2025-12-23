n = int(input())
b=[]
for i in range(n):
    a = int(input())
    b.append(a)
c=[]
odd_indices = []


for i in range(len(b)):
    val = b[i] // 2
    c.append(val)
    if b[i] % 2 != 0:
        odd_indices.append(i)

# Step 2: fix the sum
current_sum = sum(c)
need = -current_sum  # how much we need to add

# Step 3: increase some odd positions
for i in odd_indices:
    if need == 0:
        break
    c[i] += 1
    need -= 1

# Output result
for i in c:
    print(i)
    