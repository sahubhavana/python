t=int(input())
x=0
for i in range(t):
    n = int(input())
    x=bin(n).count('1')
    y='1'*x
    result=int(str(y),2)
    print(result)