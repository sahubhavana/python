def palindrome(n):
    if(n==n[::-1]):
        print("YES")
    else:
        print("NO")
def bin(N):
    if(N%2==1):
        n=format(N, 'b')
        palindrome(n)
    else:
        print("NO")
        
        

N=int(input())    
bin(N)
        
        
