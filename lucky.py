N=int(input())
x=N//10 
x1=N%10 
if(x1%x==0 or x%x1==0):
    print("YES")
else:
    print("NO")