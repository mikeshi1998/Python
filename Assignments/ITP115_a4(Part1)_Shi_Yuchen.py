# Yuchen Shi
# ITP115, Spring 2018
# Assignment A4
# yuchensh@usc.edu

# Part 1: Word Jumble Game

import random
List=["python", "eat", "play", "kill", "study"]
word=random.choice(List)
wordList=list(word)
jumbledWordList=[]
counter=len(wordList)
while counter>0:
    number = random.randint(0, len(wordList) - 1)
    jumbledWordList.append(wordList[number])
    del wordList[number]
    counter=counter-1
delimiter=""
jumbledWord=delimiter.join(jumbledWordList)
print("The jumbled word is \"" + jumbledWord +"\".")
guess=input("Please enter your guess: ")
counter2=0
while guess.lower()!=word:
    print("Try again.")
    guess=input("Please enter your guess: ")
    counter2=counter2+1
print("You got it!\nIt took you", counter2+1, "tries.")

