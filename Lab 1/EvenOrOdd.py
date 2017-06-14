#Taking input from user
numString=input("Enter a number:")

#Converting input from user into type integer
num=int(numString)

#using if conditonal statement to check if entered number is even or odd
if num%2==0:
    print('The entered number is even')
else:
    print('The entered number is odd')