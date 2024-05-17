a = "Tear"  #Input 1
b = "Rate"  #Input 2
x = a.lower()  #Lowecase Input 1
y = b.lower()  #Lowecase Input 2
x = sorted(x)  #Sort Input 1 in a List in ascending order
y = sorted(y)  #Sort Input 2 in a List in ascending order
print(x == y)  #Returns True if it is an Anagram, else false
