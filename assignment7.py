

amount = int(input("Enter the total amount: "))

# denominations
denominations = [100, 50, 20, 10, 5, 2, 1]

print("Number of notes:")

for n in denominations:
    match n:
        case 100:
            count = amount // 100
        case 50:
            count = amount // 50
        case 20:
            count = amount // 20
        case 10:
            count = amount // 10
        case 5:
            count = amount // 5
        case 2:
            count = amount // 2
        case 1:
            count = amount // 1
        case _:
            count = 0

    if count > 0:
        print(f"{n} : {count}")
        amount = amount % n