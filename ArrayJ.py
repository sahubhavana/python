N=int(input())
A=list(map(int, input().split()))
mn=min(A)
c=A.count(mn)
if(c%2!=0):
    print("Lucky")
else:
    print("Unlucky")