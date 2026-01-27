

n = int(input("Enter number of stones: "))

stones = 0
i = 1

while stones < n:
    # Ramesh puts i stones
    stones += i
    if stones >= n:
        print("Ramesh wins")
        break

    # Suresh puts i*2 stones
    stones += i * 2
    if stones >= n:
        print("Suresh wins")
        break

    i += 1