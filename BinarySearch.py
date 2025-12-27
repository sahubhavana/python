N,Q=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()

for i in range(Q):
    target=int(input())
    st=0 
    end=N-1
    found=False
    while st<=end:
        mid=st+(end-st)//2
        if arr[mid]==target:
            found=True
            break 
        elif arr[mid]<target:
            st=mid+1
        else:
            end=mid-1
    if found:
        print("found")
    else:
        print("not found")