#Taking input from user
inputList=input("Enter the list of numbers with spaces: ");
#Splitting the input based on white spaces
a=inputList.split(" ")
print("The input list is :",a)
#Function to create a new list which consist of first and last elements of input list
def newListfun():
    b=list(a[:1])
    c=list(a[-1:])
    newList=b+c
    print("The new list is:",newList)
#calling the function
newListfun()
