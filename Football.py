n = int(input())
count = {}

for i in range(n):
    s = input()
    count[s] = count.get(s, 0) + 1
    
winner = max(count, key=count.get)
print(winner)
       

    