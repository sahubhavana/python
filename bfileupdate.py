def update():
     x=open(r"C:\Users\DELL\Documents\studentdata3.dat",'rb+')
     x1=pk.load(x)
     flag=False
     n=input("enter name=")
     for i in x1:
         if(i[0]==n):
             i[1]=int(input("input new class "))
     pk.dump(x1,x)
     print("record update successfully")
     x.close()
   
        
