import math
X,P=input().split()
X=float(X)
P=float(P)
print(round((P*(100/(100-X))),2))    
#### to find a price before discount=selling_price*(100/(100-discount_price))