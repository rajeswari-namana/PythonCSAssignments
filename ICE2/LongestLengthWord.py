#Taking input from user
data = input("Enter a sentence to calculate the longest word:")
l = 0
str = ""
#splitting words based on spaces and comparing their lengths
for x in data.split(" "):
    if(l < len(x)):
        l = len(x)
        str = x
#output printing
print( str, "-", l)







