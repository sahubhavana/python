n=int(input())
count=0
for i in range(n):
  a, b, c = map(int, input().split())
  if (a or b)==1 and (b or c)==1 and (a or c)==1):
    count=count+1
print(count)
