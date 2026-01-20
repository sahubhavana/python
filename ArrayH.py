N=int(input())
A=list(map(int, input().split()))
for i in range(len(A)):
    for j in range(i + 1, len(A)):
        if A[i] > A[j]:
            A[i], A[j] = A[j], A[i]
for i in range(len(A)):
    print(A[i],end=" ")
  

            
        