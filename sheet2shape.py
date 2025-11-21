N=int(input())
for i in range(0,N):
    for k  in range(0,N-i):
        print(" ",end='')
    for  j in range(0,2*i+1):
        print("*",end='')
    print('')