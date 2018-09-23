# Yuchen Shi
# ITP 115, Spring 2018
# Lab L16
# yuchensh@usc.edu

class Coffee(object):
    statuses=["ordered", "completed"]
    def __init__(self, sizeOfDrink, description, customerName):
        self.__size=sizeOfDrink
        self.__desc=description
        self.__customer=customerName
        self.__status=0

    def setCompleted(self):
        self.__status=1

    def __str__(self):
        msg = self.__size + " " + self.__desc + " for " + self.__customer + " (" + Coffee.statuses[self.__status] + ")"
        return msg






