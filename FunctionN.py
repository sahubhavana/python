def zero(L):
    l=[]
    cz=0
    for i in L:
        if i!=0:
            l.append(i)
        else:
            cz=cz+1   
    for i in l:
        print(i,end=" ")
    for i in range(cz):
        print(0,end=" ")
        



n=int(input())
L=list(map(int, input().split()))
zero(L)