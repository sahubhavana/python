arr = [12, 35, 1, 10, 34, 1]

largest = second = -1

for num in arr:
    if num > largest:
        second = largest
        largest = num

    elif num > second and num != largest:
        second = num

print("Second Largest:", second)
