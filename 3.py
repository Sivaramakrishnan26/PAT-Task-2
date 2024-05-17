x = str(input("Enter a String: "))  #Get an input from the user
y = x
vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
for i in x:  # Iterates each character in the input
    if i in vowels:  # Check each character in the input is a vowel
        y = y.replace(i, "")  #Remove the vowel from the string
print(y)  #Print the output
