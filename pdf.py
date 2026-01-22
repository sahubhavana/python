def designerPdfViewer(h, word):
  alphabet = ['a','b','c','d','e','f','g','h','i','j',
            'k','l','m','n','o','p','q','r','s','t',
            'u','v','w','x','y','z']
  l = []
  for i in word:
    if i in alphabet:
        x = alphabet.index(i)
        l.append(h[x])   # a=1, b=2, c=3
    
  s = max(l) * len(word)
  return s  
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
