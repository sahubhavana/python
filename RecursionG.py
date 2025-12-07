
    
    
def pyramid(n, row=1):
    if row > n:
        return

    # print spaces and stars
    print(" " * (n - row) + "*" * (2 * row - 1))

    # recursive call
    pyramid(n, row + 1)

n = int(input())
pyramid(n)