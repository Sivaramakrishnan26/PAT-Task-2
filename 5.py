# Palindrome
x = "Malayalam"  # Input
x = x.lower()  # Lowercase all the characters in the input
y = x[::-1]  # Reverse the input
# y = "".join(reversed(x))
print(x == y)  # To check input x is equal to reversed string y
