def rightshift(L,X):
  
   shifted = L[-X:] + L[:-X]
   print(*shifted)
    
N,X=map(int,input().split())
X=X%N
L=list(map(int, input().split()))
rightshift(L,X)