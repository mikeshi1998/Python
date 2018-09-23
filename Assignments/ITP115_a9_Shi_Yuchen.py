# Yuchen Shi
# ITP 115, Spring 2018
# Assignment A9
# yuchensh@usc.edu

class Animal(object):
    def __init__(self, hungerValue, happinessValue, healthValue, energyValue, ageValue, nameValue, speciesValue):
        self.hunger=hungerValue
        self.happiness=happinessValue
        self.health=healthValue
        self.energy=energyValue
        self.age=ageValue
        self.name=nameValue
        self.species=speciesValue

    def play(self):
        if self.happiness>90:
            self.happiness=100
        else:
            self.happiness = self.happiness+10

        if self.hunger>95:
            self.hunger=100
        else:
            self.hunger = self.hunger+5

    def feed(self):
        if self.hunger<10:
            self.hunger=0
        else:
            self.hunger = self.hunger-10

    def giveMedicine(self):
        if self.happiness<20:
            self.happiness=0
        else:
            self.happiness=self.happiness-20
        if self.health>80:
            self.health=100
        else:
            self.health=self.health+20

    def sleep(self):
        if self.energy>80:
            self.energy=100
        else:
            self.energy=self.energy+20

        self.age=self.age+1

    def __str__(self):
        msg = "Name: " + self.name + " the " + self.species
        msg += "\nHealth: " + str(self.health)
        msg += "\nHappiness: " + str(self.happiness)
        msg += "\nHunger: " + str(self.hunger)
        msg += "\nEnergy: " + str(self.energy)
        msg += "\nAge: " + str(self.age)
        return msg

def loadAnimals(fileName):
    animalList=[]
    fileIn=open(fileName, "r")
    for line in fileIn:
        line=line.strip()
        delimiter=","
        dataList=line.split(delimiter)
        hungerValue=int(dataList[0])
        happinessValue=int(dataList[1])
        healthValue=int(dataList[2])
        energyValue=int(dataList[3])
        ageValue=int(dataList[4])
        nameValue=dataList[5]
        speciesValue=dataList[6]
        animal=Animal(hungerValue, happinessValue, healthValue, energyValue, ageValue, nameValue, speciesValue)
        animalList.append(animal)

    return animalList

def displayMenu():
    print("\n1) Play\n2) Feed\n3) Give Medicine\n4) Sleep\n5) Print an Animal's stats\n6) View All Animals\n7) Exit\n")

def selectAnimal(animalList):
    print("1) Ollie the Bunny\n2) Murdock the French Bulldog\n3) Socks the Cat\n4) Peewee the Turtle\n5) Milo the Labrador\n")
    selection=int(input("Please select an animal from the list (enter the 1-5): "))
    while selection not in [1, 2, 3, 4, 5]:
        selection=int(input("Invalid input, please try again!\n\nPlease select an animal from thew list (enter the 1-5): "))
    return animalList[selection-1]

def main():
    animalList=loadAnimals("animals.csv")
    print("Welcome to the Animal Daycare! Here is what we can do:")
    selection=1
    while selection !=7:
        displayMenu()
        selection=int(input("Please make a selection: "))
        while selection not in [1, 2, 3, 4, 5, 6, 7]:
            print("*Invalid selection, please try again.")
            displayMenu()
            selection=int(input("Please make a selection: "))
        if selection == 6:
            for animal in animalList:
                print(animal)
                print("********************************")
        elif selection == 1:
            animal=selectAnimal(animalList)
            animal.play()
            print("You played with " + animal.name + " the " + animal.species + "!")
        elif selection == 2:
            animal=selectAnimal(animalList)
            animal.feed()
            print("You fed " + animal.name + " the " + animal.species + "!")
        elif selection == 3:
            animal=selectAnimal(animalList)
            animal.giveMedicine()
            print("You gave " + animal.name + " the " + animal.species + " some medicine!")
        elif selection == 4:
            animal=selectAnimal(animalList)
            animal.sleep()
            print(animal.name + " the "+ animal.species + " took a nap!")
        elif selection == 5:
            animal=selectAnimal(animalList)
            print(animal)
            print("********************************")
    print("Goodbye!")

main()
