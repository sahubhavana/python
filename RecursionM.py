def summi(arr,i,sum=0):
    if i==len(arr):
        return 0
    else:
        sum+=arr[i] + summi(arr,i+1)
        
        return sum
       
        
        
      
       
      
N,M=map(int,input().split())
arr=list(map(int,input().split()))
i=N-M
print(summi(arr,i,sum=0))