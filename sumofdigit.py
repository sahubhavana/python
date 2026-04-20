 9.sum of digit 
def sumdigit(n,sum):
    if n==0: return sum
    sum=sum+n%10
    return sumdigit(n//10,sum)
x=int(input("eneter a number"))
y=sumdigit(x,sum=0)
print("sum of digit=",y)
