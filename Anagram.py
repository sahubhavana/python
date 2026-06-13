def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

a = input("Enter first string: ")
b = input("Enter second string: ")

if is_anagram(a, b):
    print("Anagram")
else:
    print("Not Anagram")
