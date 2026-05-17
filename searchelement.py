def search():
    flag=False
    z=int(input("enter a class="))
    x=open(r"C:\Users\DELL\Documents\studentdata3.dat",'rb')
    x1=pk.load(x)
    for i in x1:
        if (i[1]==z):
            flag=True
            break
    if(flag==True):
            print("Found")
    else:
        print("NOT found")
