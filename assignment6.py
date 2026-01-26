def reverse_number(n):
    return int(str(n)[::-1])   # convert to string, reverse it, convert back to int

# take two numbers as input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# reverse both numbers
rev_a = reverse_number(a)
rev_b = reverse_number(b)

# add the reversed numbers
sum_rev = rev_a + rev_b

# reverse the sum
result = reverse_number(sum_rev)

print("Reversed Sum:", result)