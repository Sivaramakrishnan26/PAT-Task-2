x = "Guvi Geeks Network Private Limited"  #Input
x = x.lower()  #Lowercase all the letters in the input
# vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

#Count each Vowels in individual
a = x.count("a")
e = x.count("e")
i = x.count("i")
o = x.count("o")
u = x.count("u")

print("a:", a, " e:", e, " i:", i, " o:", o, " u:", u)  #Print the count of each vowel
print("Total Number of Vowels:", (a + e + i + o + u))  #Print the total count of vowels
