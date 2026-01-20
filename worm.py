n=int(input())
l=list(map(int,input().split()))
s=int(input())
prefixsum=[0]*n
prefixsum[0]=l[0]
for i in range(1,n):
    prefixsum[i]=prefixsum[i-1]+l[i]
for i in range(s):
    x=int(input())
    ans=-1
    left=0 
    right=n-1
    while(left<=right):
            mid=(left+right)//2
            if prefixsum[mid]>=x:
                ans=mid
                right=mid-1
            else:
                left=mid+1
    print(ans+1)
            

