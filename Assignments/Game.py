# Yuchen Shi
# ITP 115, Spring 2018
# Assignment A11
# yuchensh@usc.edu

# Main portion of the program

from Human import Human
from Vampire import Vampire

def printHumans(humanList):
    print()
    counter=0  # use a counter to record the number of human objects
    for i in range(0, len(humanList)):  # print out information about all the human objects in the humanList
        print(str(counter) + ")", humanList[counter])
        counter=counter+1

def performFeeding(humanList, vamp):
    printHumans(humanList)
    index=int(input("Please select a human from the list: "))
    while index not in range(0, len(humanList)):  # error checking
        printHumans(humanList)
        index=int(input("Error, please try again.\nPlease select a human from the list: "))
    human=humanList[index]
    if human.isAlive() == True and vamp.isStuffed() == False:  # only if both the human is alive and the vampire is not stuffed
        vamp.suckBlood(human)
        print(human)
        print(vamp)
    elif vamp.isStuffed() == True and human.isAlive() == True:
        print(human)
        print(vamp)
        print(vamp.getName(), "cannot suck any more blood!")
    else:   # as long as human is not alive, print out "it is dead"
        print(human)
        print(human.getName(), "is dead! Cannot suck blood.")
        print(vamp)

def main():
    human1=Human("Eric Brooks", 5, "A-")
    human2=Human("Mina Harker", 7, "O+")
    human3=Human("Louis de Pointe du Lac", 4, "O+")
    human4=Human("Annie Sawyer", 3, "B-")
    humanList=[human1, human2, human3, human4]
    name=input("Please enter your name: ")
    animal=input("Please enter an animal: ")
    vamp=Vampire(name, 0, animal)
    selection=1
    while selection != -1:
        selection=int(input("\nMenu:\n1 --> Print All Humans\n2 --> Suck Blood\n-1 --> Quit\nEnter your choice: "))
        while selection not in [1, 2, -1]:  # error checking
            selection=int(input("Error, please try again!\n\nMenu:\n1 --> Print All Humans\n2 --> Suck Blood\n-1 --> Quit\nEnter your choice: "))
        if selection==1:
            printHumans(humanList)
        elif selection == 2:
            performFeeding(humanList, vamp)
    print(vamp.getName(), "transformed back into a", vamp.getAnimalForm())



main()
