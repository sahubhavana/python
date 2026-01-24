def pageCount(n, p):
    front=p//2
    back=n//2-p//2
    turn=min(front,back)
    return turn
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
