def print_list(arr, i):
    # Base case
    if i <0:
       return 
    else:
        
      if(i%2==0):
        print(arr[i],end=" ")
    
 
    print_list(arr, i - 1)
  
    
    
n=int(input())
arr=list(map(int,input().split()))
print_list(arr,n-1)