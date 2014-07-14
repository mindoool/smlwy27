from random import randint

board = ["rock", "scissors", "paper"]

print "Let\'s play rock scissors paper! Select one!"
print board

def random_one(board):
       return board[randint(0,2)]

computer = random_one(board)

check=[]
answer_one=""
number = 1
win = 0
draw = 0
lose = 0

while(len(check)<1):
    guess_one = str(raw_input("Guess One:"))
    if guess_one == computer:
        draw +=1
        print "computer\'s choice is " + computer
        print "Draw!"
        print "Do you wanna play more?"
        while(answer_one !="yes") and (answer_one !="no"):
            answer_one = str(raw_input("Answer:"))
            if answer_one =="no":
                check.append(1)
                print "Game Over!"
                break
            elif answer_one =="yes":
                number +=1 
            else:
                print "You have to answer yes or no!!!"
        answer_one="1"
    elif (guess_one == "rock" and computer == "scissors") or (guess_one == "scissors" and computer == "paper") or (guess_one == "paper" and computer == "rock"):
        win +=1
        print "computer\'s choice is " + computer
        print "You win!"
        print "Do you wanna play more?"
        while(answer_one !="yes") and (answer_one !="no"):
            answer_one = str(raw_input("Answer:"))
            if answer_one =="no":
                check.append(1)
                print "Game Over!"
                break
            elif answer_one =="yes":
                number +=1 
            else:
                print "You have to answer yes or no!!!"
        answer_one="1"
    elif (guess_one == "rock" and computer == "paper") or (guess_one == "scissors" and computer == "rock") or (guess_one == "paper" and computer == "scissors"):
        lose +=1
        print "computer\'s choice is " + computer
        print "You lose!"
        print "Do you wanna play more?"
        while(answer_one !="yes") and (answer_one !="no"):
            answer_one = str(raw_input("Answer:"))
            if answer_one =="no":
                check.append(1)
                print "Game Over!"
                break
            elif answer_one =="yes":
                number +=1 
            else:
                print "You have to answer yes or no!!!"
        answer_one="1"
    else:
        print "You have to answer rock, scissors or paper!!!"

print "You played " + str(number) + " games and your score is Win:" + str(win) + " Draw: " +str(draw) + " Lose: "+str(lose) +"!!!"