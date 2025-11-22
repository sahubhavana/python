n,m,k=map(int,input().split())
use_mouth=min(n,m,k)
n-=use_mouth
m-=use_mouth
k-=use_mouth
use_no_mouth=min(n//2,k)
print(use_mouth+use_no_mouth)