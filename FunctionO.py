def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):      
        if n % i == 0:
            return False
    return True
 
def count_primes(A):
    count = 0
    for x in A:
        if is_prime(x):
            count += 1
    return count
 
 
def maximum(L):
    print("The maximum number :",max(L))
def minimum(L):
    print("The minimum number :",min(L))
 
 
            
def palindrome(L):
    sum=0
    for i in L:
        if(str(i)==str(i)[::-1]):
            sum=sum+1
    print("The number of palindrome numbers :",sum )
            
         
def divisor_count(n):
    c = 0
    for i in range(1, n+1):
        if n % i == 0:
            c += 1
    return c
 
def max_divisor_number(A):
    best = A[0]
    best_div = divisor_count(A[0])
 
    for x in A:
        d = divisor_count(x)
        if d > best_div:
            best = x
            best_div = d
        elif d == best_div and x > best:
            best = x
    return best         
    
 
 
                
    
 
n=int(input())
L=list(map(int, input().split()))
 
maximum(L)
minimum(L)
print("The number of prime numbers :",count_primes(L))
palindrome(L)
print("The number that has the maximum number of divisors :",max_divisor_number(L))