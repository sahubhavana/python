#51.ou have a 7x7 grid representing scoreboard. Print the values 
# of the main diagonal (from top-left to bottom-right). 
l=[]
arr=np.arange(1,50).reshape(7,7)
for i in range(7):
    print(arr[i][i],end=" ")
