# Taking board size from user
inputSize=int(input("Enter the size of game board: "));
#Defining functions to print horizontal lines
def print_horiz_line():
    print(" --- "*inputSize);
#Defining functions to print vertical lines
def print_vert_line():
    x=inputSize +1
    print("|    "*x)
#Using loop to print required game board
for i in range(inputSize):
    print_horiz_line()
    print_vert_line()
print_horiz_line()
