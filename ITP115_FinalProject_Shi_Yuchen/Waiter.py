# Yuchen Shi
# ITP115, Spring 2018
# Final Project
# yuchensh@usc.edu

# Waiter Class

from Menu import Menu
from Diner import Diner

class Waiter(object):
    def __init__(self, menu):  # set the constructor
        self.__menu=menu
        self.__diner=[]

    def addDiner(self, diner):    # add a new diner to the list of diners
        self.__diner.append(diner)

    def getNumDiners(self):
        return len(self.__diner)

    def printDinerStatuses(self):
        print()
        for status in Diner.STATUSES:   # iterate through all the statuses
            print("Diners who are " + status + ":")
            for diner in self.__diner:
                if Diner.STATUSES[diner.getStatus()] == status:   # print all the diners in that status
                    print("\t" + str(diner))

    def takeOrders(self):
        for diner in self.__diner:
            if diner.getStatus() == 1:   # if the diner is ordering
                for type in Menu.MENU_ITEM_TYPES:   # print all the items by type
                    self.__menu.printMenuItemsByType(type)
                    index=int(input(diner.getName() + ", please select a " + type + " menu item number.\n> "))
                    while index not in range(0, self.__menu.getNumMenuItemsByType(type)):   # error checking
                        index = int(input("Invalid option. Please try again. "))
                    menuItem=self.__menu.getMenuItem(type, index)
                    diner.setOrder(menuItem)   # append the item to the diner's list of orders
                diner.printOrder()   # print all the orders of a diner

    def ringUpDiners(self):
        for diner in self.__diner:
            if diner.getStatus() == 3:   # if the diner is paying
                print("\n" + diner.getName() + ", your meal cost $" + str(diner.calculateMealCost()))   # calculateMealCost return a float, need to convert it to a string

    def removeDoneDiners(self):
        for diner in self.__diner:
            if diner.getStatus() == 4:   # if the diner is leaving
                print("\n" + diner.getName() + ", thank you for dining with us! Come again soon!")
        for i in range(len(self.__diner)-1, -1, -1):   # iterate through the list backwards, and delete the diner that is leaving using index
            if self.__diner[i].getStatus() == 4:
                del self.__diner[i]

    def advanceDiners(self):   # the procedure for one round
        self.printDinerStatuses()
        self.takeOrders()
        self.ringUpDiners()
        self.removeDoneDiners()
        for diner in self.__diner:
            diner.updateStatus()   # update every diner's status after one round








