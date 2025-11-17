import math
a,b=input().split()
a=int(a)
b=int(b)
div=a/b

c=math.floor(div)
d=math.ceil(div)
e=math.floor(div+0.5)

print('floor',a,'/',b,'=',c)
print('ceil',a,'/',b,'=',d)
print('round',a,'/',b,'=',e)
