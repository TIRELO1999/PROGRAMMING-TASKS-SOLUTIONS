"""
--------RANDOM NUMBERS--------------

Write a program that allows the guess the number ( between 1 and 9)
as many times as they want. The program should also let the user know
whether they must guess higher or lower when they are wrong, appropriate
message should be printed whe wrong/right.

NOTE : YOU CAN USE 0 TO TERMINATE THE PROGRAM

========== CODING WITH CLIFFORD ==========

"""
import random

random_num=random.randint(1,9) # randomly assigns the number from (1,9) to random_num
guess_num=int(input("Enter the number you chose (1-9) :")) # reads the guessed number from the user

while guess_num!=0:
    if guess_num==random_num: # executes when the random number is correctly guessed
        print("********** You guessed the number **********")
        break
    else:
        if random_num<guess_num: #execute when the random number is below the guessed number
            print("********** Wrong number !!!  Guess lower **********")
        elif random_num>guess_num:#execute when the random number is below the guessed number
            print("********** Wrong number !!!  Guess higher **********")
    guess_num = int(input("Enter the number you chose (1-9) :"))
















#                                                          CODING WITH CLIFFORD
