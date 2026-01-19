def plusMinus(arr):
    pos=0
    neg=0
    zero=0 
    n=len(arr)
    for i in arr:
        if i>0:
            pos=pos+1
        elif i<0:
            neg=neg+1
        elif i==0:
            zero=zero+1
    print(pos/n) 
    print(neg/n)
    print(zero/n)


n=int(input())
arr=list(map(int,input().split()))
plusMinus(arr)
