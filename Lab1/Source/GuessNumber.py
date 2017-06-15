#importing random module to use randint() function.
import random

#function that chooses a random integer.
prgm_num=random.randint(0,9)

#printing the rules of the game.
print("Rules of number guess game:\n The program will randomly pick an intger from 0 to 9 and you need to guess a number from 0 to 9.\n If they both match you win !!")

#taking input from user.
user_num=int(input("Guess the digit: "))

#printing the number chosen by program.
print("The number choosen by the program is",prgm_num,"so")

#checking if both the numbers match and printing the result.
if prgm_num==user_num:
    print("your answer is perfect, congratulations :)!")
elif prgm_num>user_num:
    print("your answer is less than the actual number!")
else:
    print("your answer is more than the actual number!")