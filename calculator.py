simple calculator 
a=eval(input("eneter a number"))
b=eval(input("eneter a second number"))
print("1-Addition")
print("2-Subtraction")
print("3-Multipilication")
print("4-Division")
choice=int(input("enter your choice="))
if choice==1:
    print("Addition of two numbers is ",a+b)
elif choice==2:
    print("Subtraction of two numbers is ",a-b)
elif choice==3:
    print("Multiplication of two number is",a*b)
elif choice==4:
    print("division of two nyumbers is",a//b)
else:
    print("Invalid choice")

