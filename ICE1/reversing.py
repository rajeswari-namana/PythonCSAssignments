#Enter the number to be reversed
string1=input("enter the number to be reversed:")

#converting entered number into string
num1=int(string1)

reverse=0

# Using while loop
while num1>0:
    remainder=num1%10
    reverse=reverse*10+remainder
    num1=num1//10

#printing the output
print(reverse)

