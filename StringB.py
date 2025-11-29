S=input()
s="\\"
def getline(cin,s):
    l=cin.split()
    for i in l:
        if(i=='\\'):
            break
        else:
            print(i,end=" ")
   
    
    
getline(S,s)