words = ["hi", "hello", "hey", "python"]

group = {}

for w in words:
    l = len(w)
    if l not in group:
        group[l] = []
    group[l].append(w)

print(group)
