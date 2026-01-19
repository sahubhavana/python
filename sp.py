A=input().strip()
B = input().strip()

# 1. Length check
if len(A) != len(B):
    print("NO")
    exit()

# 2. Find mismatched positions
diff = []
for i in range(len(A)):
    if A[i] != B[i]:
        diff.append(i)

# 3. Case: already equal
if len(diff) == 0:
    # need exactly one swap → possible only if duplicate letters exist
    if len(set(A)) < len(A):
        print("YES")
    else:
        print("NO")

# 4. Case: exactly two mismatches
elif len(diff) == 2:
    i, j = diff
    if A[i] == B[j] and A[j] == B[i]:
        print("YES")
    else:
        print("NO")

# 5. Other cases
else:
    print("NO")
