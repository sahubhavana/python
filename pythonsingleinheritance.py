single inheritance

class A:
    varA="A"
  @staticmethod
   def school():
       print("name of school=",A.varA)
    
    
class B(A):
 @ staticmethod
   def student():
        print("i am student of school")

a=B()
a.school()
a.student()
