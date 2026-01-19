def simpleArraySum(ar):
    s=0
    for i in ar:
        s=s+i
    return s
    
n=int(input())
arr=list(map(int,input().split()))
x=simpleArraySum(arr)
print(x)
