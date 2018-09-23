# Yuchen Shi
# ITP115, Spring 2018
# Final Project
# yuchensh@usc.edu

# Diner Class

from MenuItem import MenuItem

class Diner(object):
    STATUSES=["seated", "ordering", "eating", "paying", "leaving"]   # class variable
    def __init__(self, name):  # set the constructor
        self.__name=name
        self.__order=[]   # the order is an empty list at first
        self.__status=0
    def getName(self):
        return self.__name
    def setName(self, name):
        self.__name=name
    def getOrder(self):
        return self.__order
    def setOrder(self, order):   # when customer order some item, append it to the list of orders
        self.__order.append(order)
    def getStatus(self):
        return self.__status
    def setStatus(self, status):
        self.__status=status

    def updateStatus(self):
        self.__status += 1

    def printOrder(self):
        print()
        print(self.__name, "ordered:")
        for item in self.__order:   # print all the items in the order list
            print("-", item)

    def calculateMealCost(self):
        cost=0
        for item in self.__order:   # use getPrice to add the price of each item in the order list
            cost += item.getPrice()
        return cost

    def __str__(self):
        msg="Diner " + self.__name + " is currently " + Diner.STATUSES[self.__status] + "."   # using self.__status as the index to the class variable (a list)
        return msg
