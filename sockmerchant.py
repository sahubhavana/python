def sockMerchant(n, ar):
  d = {}
  count = 0
  for sock in ar:
    d[sock] = d.get(sock, 0) + 1
  for value in d.values():
    count += value // 2
  return count



  
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
