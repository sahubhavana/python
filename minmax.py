
def miniMaxSum(arr):
    total=sum(arr)
    mn=total-max(arr)
    mx=total-min(arr)
    return mn,mx

        
arr=list(map(int,input().split()))
x,y=miniMaxSum(arr)
print(x,y)
