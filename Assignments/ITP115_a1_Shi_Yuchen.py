# Yuchen Shi
# ITP 115, Spring 2018
# Assignment 1
# yuchensh@usc.edu

# Mad Libs
place = input("Enter a place: ")
adj1 = input("Enter an adjective: ")
adj2 = input("Enter another adjective: ")
verb = input("Enter a verb: ")
verbing = input("Enter a verb ending in 'ing': ")
int1 = input("Enter a number: ")
int2 = input("Enter a second number: ")
int3 = input("Enter a third number: ")
float = input("Enter a number with a decimal: ")
int4 = str(int(int2) + int(int3))

print("Today, the weather is \"" + adj1 + "\", \"" + int1 + "\" of my friends and I go to \"" + place +
      "\". It takes us \"" + float + "\" hours to go there.\nAfter we arrive, we \"" + verb +
      "\" for a while. Then, we see a group of \"" + int2 + "\" children \"" + verbing + "\".\nWe think it is very \""
      + adj2 + "\". When the sun goes down, \"" + int3 + "\" more children come to join them. Now there are \"" + int4
      + "\" children.")