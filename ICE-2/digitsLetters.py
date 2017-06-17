#taking input from user
string=input("Enter text")
alpha=0
dig=0
i = 0
#using two boolean functions to find whether char is a number or a string
while i < len(string):
    if string[i].isalpha():
        alpha=alpha+1
    elif string[i].isdigit():
        dig=dig+1
    i = i + 1
#printing the output
print("count of alphabets: ",alpha)
print("count of numbers: ",dig)
