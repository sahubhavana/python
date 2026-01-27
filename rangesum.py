t=int(input())
for i in range(t):
	L,R=map(int,input().split())
	sum=0
	for i in range(L,R+1):
		sum=sum+i
	print(sum)