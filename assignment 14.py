
def staircase(n):
    
    
    if n <= 0:
        print("Number of steps must be a positive integer.")
        return

    for i in range(1, n + 1):
        print("#" * i)

n=int(input("enter a value to print"))
staircase(n)				