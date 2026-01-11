r,c=map(int,input().split())
for i in range(1,r+1):
    if(i%2==0):
        for j in range(1,c+1):
            if(j==c):
                print("#",end="")
                print()
            else:
                print(".",end="")
    else:
        for j in range(1,c+1):
            print("#",end="")
        print()