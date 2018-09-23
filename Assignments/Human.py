# Yuchen Shi
# ITP 115, Spring 2018
# Assignment A11
# yuchensh@usc.edu

# Human Class

from Being import Being

class Human(Being):
    def __init__(self, name, quarts, bloodType):
        super().__init__(name, quarts)
        self.__bloodType=bloodType

    def getBloodType(self):
        return self.__bloodType

    def setBloodType(self, newBloodType):
        self.__bloodType=newBloodType

    def isAlive(self):
        if self.getQuarts()>0:
            return True
        else:
            return False

    def __str__(self):
        msg="Human " + self.getName() + " has " + str(self.getQuarts()) + " quarts of type " + self.getBloodType() + " blood."
        return msg
