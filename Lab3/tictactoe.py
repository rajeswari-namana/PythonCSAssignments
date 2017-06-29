# Initialising a list for displaying positions on game board
board=[" "," "," "," "," "," "," "," "," "]

# global variable used for alternating turns between two players
turn=1

#fuction which prints the game board and the move
def gameBoard():
    print(" ---"*3)
    print("|",board[0],"|",board[1],"|",board[2],"|")
    print(" ---" * 3)
    print("|", board[3], "|", board[4], "|", board[5], "|")
    print(" ---" * 3)
    print("|", board[6], "|", board[7], "|", board[8], "|")
    print(" ---" * 3)

#function for the main logic of the game
def startGame():
    #taking input from user and splitting into row and column value
    global turn
    p=input("enter the position: ")
    p1=p.split(",")
    p1=[int(i) for i in p1]
    #converting input entered to a position on game board
    if p1[0]==1 and p1[1]==1:
        c=0
    elif p1[0]==1 and p1[1]==2:
        c=1
    elif p1[0]==1 and p1[1]==3:
        c=2
    elif p1[0]==2 and p1[1]==1:
        c=3
    elif p1[0]==2 and p1[1]==2:
        c=4
    elif p1[0]==2 and p1[1]==3:
        c=5
    elif p1[0]==3 and p1[1]==1:
        c=6
    elif p1[0]==3 and p1[1]==2:
        c=7
    elif p1[0]==3 and p1[1]==3:
        c=8
    else:
        print("please enter valid values: ")
    while (turn):
        #if position on game board empty user move is entered
        if board[c]!="x" and board[c]!="o" and turn%2==1:
            board[c]="x"
            turn=turn+1
            gameBoard()
            startGame()
        #alternating move
        elif board[c]!="x" and board[c]!="o" and turn%2==0:
            board[c] = "o"
            turn = turn-1
            gameBoard()
            startGame()
        #dispalying already occupied position
        else:
            print("already occupied")
        break
#calling fuction
startGame()







