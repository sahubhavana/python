X1,Y1,X2,Y2=map(int,input().split())
X3,Y3,X4,Y4=map(int,input().split())
if (Y1-Y2)*(X3-X4)==(Y3-Y4)*(X1-X2):
    print("YES")
else:
    print("NO")