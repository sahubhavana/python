def maxsearch():
    max=0
    x=open(r"C:\Users\DELL\Documents\studentdata3.dat",'rb')
    x1=pk.load(x)

    # finding a maximum marks

    for i in x1:
        if(i[2]>max):
            max=i[2]
            z=i
    print("the student with maximum number is=",z)
        
    
    x.close()
