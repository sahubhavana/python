def pyramid(n, row=0):
    if row == n:
        return

    # print spaces and stars
    print(" " * ( row) + "*" * (2 * (n- row)-1))

    # recursive call
    pyramid(n, row +1)

n = int(input())
pyramid(n)