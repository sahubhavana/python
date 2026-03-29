# power of 2 using anonymous function
total_terms = int(input("Enter the Total Number of Terms: "))
anoms = lambda x: 2 ** x
for i in range(total_terms):
    print("2 raised to the power ", i, " is ", anoms(i))
