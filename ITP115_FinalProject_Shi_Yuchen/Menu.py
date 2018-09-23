# Yuchen Shi
# ITP115, Spring 2018
# Final Project
# yuchensh@usc.edu

# Menu Class

from MenuItem import MenuItem

class Menu(object):
    MENU_ITEM_TYPES=["Drink", "Appetizer", "Entree", "Dessert"]  # class attribute
    def __init__(self, menu):   # set the constructor
        self.__menuItemDictionary={}
        fileIn=open(menu, "r")   # read from the file
        for line in fileIn:
            line=line.strip()
            lineList=line.split(",")   # split every line into a list
            item=MenuItem(lineList[0], lineList[1], float(lineList[2]), lineList[3])   # create the menu item
            if lineList[1] not in self.__menuItemDictionary.keys():   # if we have don't have this category yet, create a key value pair, and set the value to be a list of items
                self.__menuItemDictionary[lineList[1]]=[item]
            else:
                self.__menuItemDictionary[lineList[1]].append(item)  # if we have this category already, append the item to the list
        fileIn.close()   # close the file

    def getMenuItem(self, type, index):   # get a specific item from a category
        return self.__menuItemDictionary[type][index]

    def printMenuItemsByType(self, type):   # print all the items with index of a category
        print("\n-----" + type.upper() + "-----")
        for i in range(0, len(self.__menuItemDictionary[type])):
            print(str(i) + ") " + str(self.__menuItemDictionary[type][i]))

    def getNumMenuItemsByType(self, type):   # the length of the list is the number of items in that category
        return len(self.__menuItemDictionary[type])

