#52.Ask user to input two numbers a, b. Write a program to 
#generate a random array of shape (a, b) and print the array and 
#average of the array.

a=int(input("enter a number="))
b=int(input("enter a number="))
arr=np.random.randint(0,100,(a,b))
np.mean(arr)
