# Yuchen Shi
# ITP 115, Spring 2018
# Lab L4
# Yuchensh@usc.edu


toDo=input("Would you like to:\na) see the ASCII code for the alphabet\nb) Translate a word into its ASCII\nSelect a or b: " )
while toDo.lower()!="a" and toDo.lower()!="b":
    toDo = input("**You have entered an invalid choice. Please try again. ")
if toDo.lower() == "a":
    toSee=input("Do you want to see the alphabet in upper (u) or lowercase (l)? ")
    while toSee.lower() != "u" and toSee.lower()!="l":
        toSee=input("**You have entered an invalid choice. Please try again. ")
    if toSee.lower()=="u":
        for i in range(65, 91, 1):
            print(i, chr(i))
    if toSee.lower()=="l":
        for g in range(97, 123, 1):
            print(g, chr(g))

if toDo.lower()=="b":
    word=input("Enter the word you would like to translate into ASCII: ")
    for ltr in word:
        print(ltr + ":", ord(ltr))


