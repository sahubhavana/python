def palindrome(arr,i,r):
    if i>=r:
        print("YES")
    else:
       if arr[i]!= arr[r]:
           print("NO")
       else:
           palindrome(arr,i+1,r-1)
         
      
       
N=int(input())
arr=list(map(int,input().split()))
palindrome(arr,0,N-1)