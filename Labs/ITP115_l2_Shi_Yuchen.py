# Yuchen Shi
# ITP 115, Spring 2018
# Lab L2
# Yuchensh@usc.edu

finalWords = ""
size = input("What size coffee do you want (S, M, L)? ")
temperature = int(input("What temperature would you like (in degrees)? "))
beans = input("What type of beans/blend would you like? ")
cream = input("Would you like room for cream (y/n)? ")

if size.lower() == "s":
    finalWords = finalWords + "small"
elif size.lower() == "m":
    finalWords = finalWords + "medium"
elif size.lower() == "l":
    finalWords = finalWords + "large"

if temperature > 100:
    finalWords = finalWords + " hot"
elif temperature <= 100:
    finalWords = finalWords + " cold"

finalWords = finalWords + " " + beans

if cream.lower() == "y":
    finalWords = finalWords + " with cream"
elif cream.lower() == "n":
    finalWords = finalWords + " with no cream"

print("You ordered a " + finalWords + ".")
