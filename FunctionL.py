def newarray(L1,L2):
    for i in L2:
       print(i,end=" ")
    for i in L1:
        print(i,end=" ")
    
n=int(input())
L1=list(map(int, input().split()))
L2=list(map(int, input().split()))
newarray(L1,L2)