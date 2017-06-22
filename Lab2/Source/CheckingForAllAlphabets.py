# Declaring a string which contains all alphabets and an empty space.
str1='abcdefghijklmnopqrstuvwxyz '
# Declaring another string which contains all alphabets.
str2='abcdefghijklmnopqrstuvwxyz'
#Converting strings to sets.
set1=set(str1)
set2=set(str2)
#taking input from user.
str_input=input("Enter any string: ")
#converting input string to lower case letters.
str3=str_input.lower()
#converting input string into a set.
set3=set(str3)
#Using conditional statement to check for all alphabets.
if set3==set1 or set3==set2:
    print("The string contains all the alphabets in it!")
else:
    print("All alphabets are not present in the string entered.")