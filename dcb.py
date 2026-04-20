5.Decimal to binary conversaion

def dectobin(n,result=""):
    if(n==0):return result
    
    
    return dectobin(n//2,str(n%2)+result)

n=int(input("enetr a value of n="))
x=dectobin(n)
print(x)
