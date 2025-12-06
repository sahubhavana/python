X1,Y1=map(int,input().split())
X2,Y2=map(int,input().split())
X3,Y3=map(int,input().split())
area = abs(X1*(Y2 - Y3) + X2*(Y3 - Y1) + X3*(Y1 - Y2))
if area==0:
    print("YES")
else:
    print("NO")