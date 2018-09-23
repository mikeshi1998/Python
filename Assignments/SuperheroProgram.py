# Yuchen Shi
# ITP115, Spring 2018
# Assignment a10
# yuchensh@usc.edu

from Superhero import Superhero

def main():
    playAgain = "y"
    while playAgain.lower() == "y":
        name1=input("Enter fighter #1's name:\n")
        type1=input("Is fighter #1 a hero or a villain?:\n")
        attack1=int(input("Enter fighter #1's attack points:\n"))
        name2=input("Enter fighter #2's name:\n")
        type2=input("Is fighter #2 a hero or a villain?:\n")
        attack2=int(input("Enter fighter #2's attack points:\n"))
        player1=Superhero(name1, type1, attack1)
        player2=Superhero(name2, type2, attack2)
        print("\nFIGHTERS\n")
        print(player1)
        print(player2)
        print("\nBEGINNING BATTLE!")
        counter=0
        while player1.isDead() == False and player2.isDead() == False:
            counter=counter+1
            print("\n====== Round", counter, "======")
            attackValue1=player1.getAttack()
            attackValue2=player2.getAttack()
            player1.loseHealth(attackValue2)
            player2.loseHealth(attackValue1)
            print(player1)
            print(player2)
        if player1.isDead() == True and player2.isDead() == False:
            print("\n" + player2.getName() + " won!")
        elif player1.isDead() == False and player2.isDead() == True:
            print("\n" + player1.getName() + " won!")
        elif player1.isDead() == True and player2.isDead() == True:
            print("\nIt was a tie!")

        playAgain=input("\nWould you like to play again? (y/n): ")

    print("Goodbye!")

main()
