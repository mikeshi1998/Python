# Yuchen Shi
# ITP115, Spring 2018
# Assignment 3
# yuchensh@usc.edu

# Part 1: Pig Elvish

import random
vowel=["a", "e", "i", "o", "u"]
print("Elcómewó óten heten Igpén Lvísheá ránslátórtë!\nWelcome to the Pig Elvish translator!")

goOn="y"
while goOn=="y":
    word=input("Please enter a word you would like to translate: ")
    listWord=list(word)
    firstLetter = listWord[0]
    listWord.append(listWord[0].lower())
    del listWord[0]
    if len(listWord)>=4:
        listWord.append(random.choice(vowel))
    if len(listWord)<4:
        listWord.append("en")

    delimiter=""
    newString=delimiter.join(listWord)
    newString2=newString.replace("k", "c")
    newList=list(newString2)
    if newList[len(newList)-1]=="e":
        del newList[len(newList)-1]
        newList.append("ë")

    finalWord=delimiter.join(newList)


    if firstLetter.isupper()==True:
        print("'"+word+"' in elvish is:", finalWord.capitalize())
    else:
        print("'"+word+"' in elvish is:", finalWord)


    goOn=input("Would you like to translate another word? (y/n): ")

print("Oodbyega! Aveha aen icenë ayden!\n(Goodbye! Have a nice day!)")

