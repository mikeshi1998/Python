# Yuchen Shi
# ITP115, Spring 2018
# Lab L7
# yuchensh@usc.edu

import random
num=[0, 1, 2]
item=["rock", "paper", "scissor"]

def main():
    counterCWin=0
    counterYWin=0
    counterTie=0
    gameGoOn = True

    while gameGoOn is True:
        displayMenu()
        computerChoice=getComputerChoice()
        playerChoice=getPlayerChoice()
        if playRound(computerChoice,playerChoice)==0:
            counterTie=counterTie+1
        elif playRound(computerChoice,playerChoice)==1:
            counterYWin=counterYWin+1
        elif playRound(computerChoice, playerChoice)==-1:
            counterCWin=counterCWin+1
        print("You choose", item[playerChoice]+".\nThe computer choose", item[computerChoice]+".")
        if computerChoice==playerChoice:
            print("It's a tie.")
        elif computerChoice==0 and playerChoice==1:
            print("Paper covers rock. You win!")
        elif computerChoice==0 and playerChoice==2:
            print("Rock smashes scissor. Computer wins!")
        elif computerChoice==1 and playerChoice==0:
            print("Paper covers rock. Computer wins!")
        elif computerChoice==1 and playerChoice==2:
            print("Scissor cuts paper. You win!")
        elif computerChoice==2 and playerChoice==0:
            print("Rock smashes scissor. You win!")
        elif computerChoice==2 and playerChoice==1:
            print("Scissor cuts paper. Computer wins!")
        gameGoOn=continueGame()
    print("You won", counterYWin, "game(s).\nThe computer won", counterCWin, "game(s).\nYou tied with the computer", counterTie, "time(s).\nThanks for playing!")


def displayMenu():
    print("Welcome! Let's play rock, paper, scissors.\nThe rules of the game are:\n\tRock smashes scissors\n\tScissors cut paper\n\tPaper covers rock\n\tIf both the choices are the same, it's a tie")
def getComputerChoice():
    return random.choice(num)
def getPlayerChoice():
    choice=int(input("Please choose (0) for rock, (1) for paper or (2) for scissors\n"))
    while choice not in [0, 1, 2]:
        choice=int(input("Please choose (0) for rock, (1) for paper or (2) for scissors\n"))
    return choice
def playRound(int1, int2):
    if int1==int2:
        return 0
    elif int1==0 and int2==1:
        return 1
    elif int==0 and int2==2:
        return -1
    elif int==1 and int2==0:
        return -1
    elif int1==1 and int2==2:
        return 1
    elif int1==2 and int2==0:
        return 1
    elif int1==2 and int2==1:
        return -1
def continueGame():
    goOn=input("Do you want to continue playing? Enter (y) for yes or (n) for no.\n")
    while goOn.lower() not in ["y", "n"]:
        goOn = input("Do you want to continue playing? Enter (y) for yes or (n) for no.\n")
    if goOn.lower()=="y":
        return True
    else:
        return False

main()
