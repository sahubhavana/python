def countApplesAndOranges(s, t, a, b, apples, oranges):
  counta = 0
  counto = 0

    # Apples
  for d in apples:
    pos = a + d
    if s <= pos <= t:
        counta += 1

    # Oranges
  for d in oranges:
    pos = b + d
    if s <= pos <= t:
        counto += 1

  print(counta)
  print(counto)
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
   
