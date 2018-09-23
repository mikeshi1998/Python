# Yuchen Shi
# ITP115, Spring 2018
# Lab L14
# yuchensh@usc.edu

import random

class Die(object):
    def __init__(self, numSides=6):
        self.sides=numSides
        self.rollValue=0

    def roll(self):
        self.rollValue=random.randrange(1, self.sides+1)
        return self.rollValue

    def __str__(self):
        msg = str(self.rollValue)
        return msg

def main():
    defaultValue=input("Do you want to use a default dice for your first dice (y/n)? ")
    while defaultValue.lower() not in ["y", "n"]:
        defaultValue=input("Invalid choice. Please try again. ")
    if defaultValue.lower()=="y":
        die1=Die()
    else:
        numOfSides=int(input("How many sides would you like for your first dice? "))
        die1=Die(numOfSides)
    defaultValue2=input("Do you want to use a default dice for your second dice (y/n)? ")
    while defaultValue2.lower() not in ["y", "n"]:
        defaultValue2=input("Invalid choice. Please try again. ")
    if defaultValue2.lower()=="y":
        die2=Die()
    else:
        numOfSides2=int(input("How many sides would you like for your second dice? "))
        die2=Die(numOfSides2)
    die1.roll()
    die2.roll()
    print("Dice 1 rolled a " + str(die1) + ". Dice 2 rolled a " + str(die2) + ".")
    numRolls=int(input("How many rolls do you want to average the sum of? "))
    averageValue=calcDieSumAverage(die1, die2, numRolls)
    print("The average sum of Dice 1 and Dice 2 is " + str(averageValue))

def calcDieSumAverage(die1, die2, numRolls):
    sumValue=0
    counter=numRolls
    while counter>0:
        value1=die1.roll()
        value2=die2.roll()
        sumValue = sumValue+value1+value2
        counter=counter-1
    averageValue=sumValue/numRolls
    return averageValue

main()

