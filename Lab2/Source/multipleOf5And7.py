#taking input from user
numString=input("Enter any number between 1500 and 2700: ")
#converting input into an integer value.
num=int(numString)
#checking whether the integer is divisible by 5 and 7.
if 1500<num<2700:
    if (num%5==0 and num%7==0): #Checking for remainder 0.
        print(num,"is divisible by 7 and is a multiple of 5!")
    else:
        print(num, "is not divisible.")
else:
    print("Please enter number between 1500 and 2700.")