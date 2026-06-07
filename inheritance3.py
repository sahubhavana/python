## question 3:

class order:
    def __init__(self,price):
        self.price=price
        
    def __gt__(self,other):
        return self.price>other.price
        
s1=order(90)
s2=order(80)
print(s1>s2)
