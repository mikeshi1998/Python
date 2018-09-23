# Yuchen Shi
# ITP115, Spring 2018
# Final Project
# yuchensh@usc.edu

# MenuItem Class

class MenuItem(object):
    def __init__(self, name, typeName, price, description):   # set the constructor
        self.__name=name
        self.__type=typeName
        self.__price=price
        self.__description=description
    def getName(self):   # set the getter and setter for all the attirbutes
        return self.__name
    def setName(self, name):
        self.__name=name
    def getType(self):
        return self.__type
    def setType(self, typeName):
        self.__type=typeName
    def getPrice(self):
        return self.__price
    def setPrice(self, price):
        self.__price=price
    def getDescription(self):
        return self.__description
    def setDescription(self, description):
        self.__description=description
    def __str__(self):
        msg=self.__name + " (" + self.__type + "): $" + str(self.__price) + "\n\t" + self.__description
        return msg

