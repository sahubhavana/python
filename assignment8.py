# Find last digit of a^b

t = int(input("Enter number of test cases: "))
for i in range(t):
    a=int(input("enter value of a")) 
    b =int(input("Enter value of  b: "))
    print((a ** b) % 10)