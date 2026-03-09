# Find partners with at least X skill

N = int(input("Enter number of people: "))
X = int(input("Enter minimum skill required: "))


for i in range(N):
    Y = int(input("Enter skill of person: "))
    if Y >= X:
    	print("YES")
    else:
    	print("No")