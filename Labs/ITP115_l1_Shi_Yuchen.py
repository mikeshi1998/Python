# Yuchen Shi
# ITP 115, Spring 2016
# Lab L1
# yuchensh@usc.edu

# Print box
print(" _\n| |\n| |\n|_|")

# Print quote
print("You don't frighten us, English pig-dogs!\nGo and boil your bottoms, sons of a silly person!\n\t-“Monty Python and the Holy Grail\"")

# Print date
month = input("What month are we in? ")
date = input("What is today's date? ")
day = int(input("What day of the month is today? "))
tomorrow = day + 1
print("Today is", date, month, day, "and Tomorrow will be", month, tomorrow)

# This could break when today is the last day of a month. For example, today is Jan.31, tomorrow should be Feb.1, but not Jan.32.
# We might fix this in the future by using some conditional statements.