# Yuchen Shi
# ITP 115, Spring 2018
# Lab L3
# Yuchensh@usc.edu

# Print Triangle

numSpaces = 18
numSymbols = 1
space = " "
symbol = " ^"

while numSpaces >= 0:
    print(space*numSpaces + symbol*numSymbols)
    numSpaces = numSpaces-2
    numSymbols = numSymbols+2
