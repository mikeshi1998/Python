# Yuchen Shi
# ITP 115, Spring 2018
# Lab L16
# yuchensh@usc.edu

from Coffee import Coffee

class Barista(object):
    maxOrders=5
    def __init__(self, baristaName):
        self.__name=baristaName
        self.__order=[]

    def takeOrder(self):
        description=input("What drink do you want? ")
        sizeOfDrink=input("What size would you like? ")
        customerName=input("What is your name? ")
        coffee=Coffee(sizeOfDrink, description, customerName)
        self.__order.append(coffee)
        print(coffee)

    def isAcceptingOrders(self):
        if len(self.__order)<Barista.maxOrders:
            return True
        else:
            return False

    def makeDrinks(self):
        print("Here are the completed orders:")
        for coffee in self.__order:
            coffee.setCompleted()
            print("\t" + str(coffee))
        self.__order=[]

    def __str__(self):
        msg = "Hello, my name is " + self.__name + ", and I am your barista."
        return msg
