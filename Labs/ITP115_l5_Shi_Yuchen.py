# Yuchen Shi
# ITP115, Spring 2018
# Lab L5
# yuchensh@usc.edu

import random
articles=["a", "the"]
nouns=["table", "California", "chef", "cow"]
verbs=["sing", "run", "hug", "nap"]
menuChoice=1

while menuChoice !=5:
    print("Welcome to Sentence Generator!")
    print("\t1) View")
    print("\t2) Add Words")
    print("\t3) Delete Words")
    print("\t4) Generate Sentence")
    print("\t5) Exit")
    menuChoice=int(input("What would you like? "))

    while menuChoice != 1 and menuChoice!=2 and menuChoice!=3 and menuChoice!=4 and menuChoice!=5:
        menuChoice=int(input("Invalid choice. Please enter again: "))

    if menuChoice==1: # View
        print("articles: ", articles)
        print("nouns: ", nouns)
        print("verbs: ", verbs)
    elif menuChoice==2: # Add
        choice=int(input("Enter 1) for nouns or 2) for verbs: "))
        word=input("Enter the word: ")
        if choice==1:
            nouns.append(word)
        elif choice==2:
            verbs.append(word)
    elif menuChoice==3: # Delete
        choice2=int(input("Enter 1) for nouns or 2) for verbs: "))
        if choice2==1:
            removeNoun=input("Enter the word: ")
            if removeNoun in nouns:
                nouns.remove(removeNoun)
            else:
                print("Word not in list.")
        if choice2==2:
            removeVerb=input("Enter the word: ")
            if removeVerb in verbs:
                verbs.remove(removeVerb)
            else:
                print("Word not in list.")

    elif menuChoice==4: # Generate sentence
        print(random.choice(articles).upper(), random.choice(nouns), random.choice(verbs), random.choice(articles), random.choice(nouns))

print("Program will exit\nHave a great day!")