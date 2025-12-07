def print_digits(n):
    
    if n < 10:
        print(n, end=" ")
        return
   
    print_digits(n // 10)
    
    print(n % 10, end=" ")

t = int(input())

for _ in range(t):
    n = int(input())
    if n == 0:
        print(0)
    else:
        print_digits(n)
        print()  
        
    