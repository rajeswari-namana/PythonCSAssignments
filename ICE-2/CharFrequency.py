#taking input from user
string1=input(print("Enter the string:"))
#Defining a function which uses dictionary to fine char frequency
def charfrequency(string1):
    dict = {}
    for i in string1:
        keys = dict.keys()
        if i in keys:
            dict[i] = dict[i]+ 1
        else:
            dict[i] = 1
    return dict
#calling the function and printing it
print(charfrequency(string1))