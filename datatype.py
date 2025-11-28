n,k,a=input().split()
n=int(n)
k=int(k)
a=int(a)
if (n*k)%a==0:
    if(n*k)//a>=-2147483648 and (n*k)//a<=2147483647:
        print("int")
    else:
        print("long long")
    
else:
    print("double")