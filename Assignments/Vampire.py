# Yuchen Shi
# ITP 115, Spring 2018
# Assignment A11
# yuchensh@usc.edu

# Vampire Class

from Being import Being

class Vampire(Being):
    MAX_BLOOD=5
    HUNGER_LEVELS=["starving", "hangry", "hungry", "content", "full", "stuffed"]
    def __init__(self, name, quarts, animalForm):
        super().__init__(name, quarts)
        self.__animalForm=animalForm

    def getAnimalForm(self):
        return self.__animalForm

    def setAnimalForm(self, newAnimalForm):
        self.__animalForm=newAnimalForm

    def isStuffed(self):
        if self.getQuarts()==Vampire.MAX_BLOOD:
            return True
        else:
            return False

    def suckBlood(self, human):
        human.decreaseQuarts()
        self.increaseQuarts()

    def __str__(self):
        msg=self.getName() + " is " + Vampire.HUNGER_LEVELS[self.getQuarts()]
        return msg
