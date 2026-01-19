def aVeryBigSum(ar):
    sum=0
    for i in ar:
        sum=sum+i
    return sum
n=int(input())
arr=list(map(int,input().split()))
x=aVeryBigSum(arr)
print(x)
