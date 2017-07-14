# Initialising a list for displaying positions on game board
board=[" "," "," "," "," "," "," "," "," "]
# global variable used for alternating turns between two players
turn=1
#class declaration
class game():
    def _init_(self):
        pass

    #fuction which prints the game board and the move
    def gameBoard(self):
        print(" ---"*3)
        print("|",board[0],"|",board[1],"|",board[2],"|")
        print(" ---" * 3)
        print("|", board[3], "|", board[4], "|", board[5], "|")
        print(" ---" * 3)
        print("|", board[6], "|", board[7], "|", board[8], "|")
        print(" ---" * 3)

    #function for win situation
    def gameWinSituation(self):
        if (board[0]=="x" and board[1]=="x" and board[2]=="x") or \
                (board[3]=="x" and board[4]=="x" and board[5]=="x") or \
                (board[6]=="x" and board[7]=="x" and board[8]=="x") or \
                (board[0]=="x" and board[3]=="x" and board[6]=="x") or \
                (board[1]=="x" and board[4]=="x" and board[7]=="x") or \
                (board[2]=="x" and board[5]=="x" and board[8]=="x") or \
                (board[0]=="x" and board[4]=="x" and board[8]=="x") or \
                (board[2]=="x" and board[4]=="x" and board[6]=="x"):
            print("CONGRATS, PLAYER 1 WIN !!!")
        elif (board[0]=="o" and board[1]=="o" and board[2]=="o") or \
                (board[3]=="o" and board[4]=="o" and board[5]=="o") or \
                (board[6]=="o" and board[7]=="o" and board[8]=="o") or \
                (board[0]=="o" and board[3]=="o" and board[6]=="o") or \
                (board[1]=="o" and board[4]=="o" and board[7]=="o") or \
                (board[2]=="o" and board[5]=="o" and board[8]=="o") or \
                (board[0]=="o" and board[4]=="o" and board[8]=="o") or \
                (board[2]=="o" and board[4]=="o" and board[6]=="o"):
            print("CONGRATS, PLAYER 2 WIN !!!")
        else:
            game.startGame(self)

    #function for the main logic of the game
    def startGame(self):
    #taking input from user and splitting into row and column value
        global turn
        p=input("enter the position in the form of row,col: ")
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
            #if position on game board is empty, user can enter his move
            if board[c]!="x" and board[c]!="o" and turn%2==1:
                board[c]="x"
                turn=turn+1
                game.gameBoard(self)
                game.gameWinSituation(self)
            #alternating move
            elif board[c]!="x" and board[c]!="o" and turn%2==0:
                board[c] = "o"
                turn = turn-1
                game.gameBoard(self)
                game.gameWinSituation(self)
        #dispalying already occupied position
            else:
                print("already occupied")
            break
#creating instance of class
game1=game()
game1.startGame()