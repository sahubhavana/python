lst = [10, 20, 5, 40, 25]

lst = list(set(lst))   # remove duplicates
lst.sort()

print("Second Largest =", lst[-2])
