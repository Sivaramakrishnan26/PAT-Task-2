x = 20
for i in range(x):  # Outer loop iterates from 0 to 19
    for j in range(i + 1):  # Inner loop iterates from 0 to i
        print(j + 1, end=" ")  # Print the output
    print()  # To print in a newline
