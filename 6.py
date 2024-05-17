import os

x = str(input("Enter a String 1: "))  #Get 1st input from the user
y = str(input('Enter a String 2: '))  #Get 2nd input from the user

common_substring = os.path.commonprefix([x, y])  # Find the common substring

print("The common substring between", x, "and", y, "is", common_substring)  # Print the output
