def maximum(arr,i,s=0):
    if i==len(arr):
        return 0
    else:
        s=arr[i] + maximum(arr,i+1)
        return s
N=int(input())
arr=list(map(int,input().split()))
print(maximum(arr,0,s=0))