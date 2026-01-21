def gradingStudents(grades):
  nextmul=((grades)//5+1)*5 
  if grades<38:
    return grades
  else:
    if(nextmul-grades)<3:
        return nextmul
    else:
        return grades
        
        
        
n=int(input())
for i in range(n):
    x=int(input())
    y=gradingStudents(x)
    print(y)
            
     




            
     



