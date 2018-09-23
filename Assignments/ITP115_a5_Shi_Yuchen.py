# Yuchen Shi
# ITP 115, Spring 2018
# Assignment A5
# yuchensh@usc.edu

import TicTacToeHelper

def isValidMove(boardList, spot):
    if spot in boardList:
        return True
    else:
        return False

def updateBoard(boardList, spot, playerLetter):
    boardList[spot] = playerLetter

def playGame():
    boardList = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    move_counter=0
    TicTacToeHelper.printUglyBoard(boardList)
    while TicTacToeHelper.checkForWinner(boardList, move_counter) =="n":
        if move_counter%2==0:
            player="x"
        else:
            player="o"
        move_counter=move_counter+1
        spot=int(input("Player "+player+", pick a spot: "))
        while isValidMove(boardList, spot) is False:
            spot=int(input("Invalid move, please try again.\nPlayer "+player+", pick a spot: "))
        updateBoard(boardList, spot, player)
        TicTacToeHelper.printUglyBoard(boardList)
    if TicTacToeHelper.checkForWinner(boardList, move_counter)=="x":
        print("Game over!\nPlayer x is the winner!")
    elif TicTacToeHelper.checkForWinner(boardList, move_counter)=="o":
        print("Game over!\nPlayer o is the winner!")
    elif TicTacToeHelper.checkForWinner(boardList, move_counter)=="s":
        print("Game over!\nStalemate reached!")

def main():
    continuePlaying="y"
    while continuePlaying.lower()=="y":
        print("Welcome to Tic Tac Toe!")
        playGame()
        continuePlaying=input("Would you like to play another round? (y/n) ")
    print("Goodbye!")

main()