# Yuchen Shi
# ITP115, Spring 2018
# Assignment 3
# yuchensh@usc.edu

# Part 2: Largest number

again="y"
while again=="y":
    number = int(input("Input an integer greater than or equal to 0 or -1 to quit: "))
    while True:
        if number==-1:
            break
        number2=int(input("Input an integer greater than or equal to 0 or -1 to quit: "))
        if number2==-1:
            break
        if number>=number2:
            pass
        if number<number2:
            number=number2
    print("The largest number is", number)

    again=input("Would you like to find the largest number again? (y/n): ")

print("Goodbye!")