4.Sum of n natural number 
def sumofn(n,sum):
    if n==0:return sum
    sum=sum+n
    return sumofn(n-1,sum)
n=int(input("enter a value of n="))
x=sumofn(n,sum=0)
print("sum of n natural number=",x)
