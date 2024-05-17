def unique_characters(y):  # Define a function
    set1 = set(y)  # Creates a set from the input. Set automatically removes the duplicate character
    return len(set1)  # Return length of set1


x = str(input("Enter a String: "))  # Get an input from the user
print(unique_characters(x))  # Print the output
