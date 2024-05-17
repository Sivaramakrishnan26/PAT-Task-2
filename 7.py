from collections import Counter

x = str(input("Enter a String: "))  # Get an input from the user

def freq_char(y):  # Define a function
    count1 = Counter(y)  # Count the occurrence of each character in the input
    count2 = max(count1, key=count1.get)  # Find the maximum count of the most frequent character
    return count2  # return the most frequent character


print("The most frequent character in", x, "is", freq_char(x))  #Print the output
