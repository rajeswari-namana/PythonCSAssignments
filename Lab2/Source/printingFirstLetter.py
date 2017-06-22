# program to print first letter in my name.
print("My name is Rajeswari, hence the first letter in my name is 'R'")
# Using two for loops for printing 2 dimensional image i.e using rows and columns.
for row in range(7):
    for col in range(5):
        if((col==0) or (col==4 and row!=0 and row!=3) or (col in range(1,4) and (row==0 or row==3) ) ):
            print("*",end="") #if condition is true star symbol is printed.
        else:
            print(end=" ") #if condition is false space is printed.
    print("") #to print in the next line after execution of inner loop.
