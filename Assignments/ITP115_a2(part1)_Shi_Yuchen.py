# Yuchen Shi
# ITP 115, Spring 2018
# Assignment 2
# Yuchensh@usc.edu

# Part 1: Vending Machine

# Define variables
price=0
finalPrice=0
coupon=0
bought=""
change=0

# Ask the first question
item=input("Please select an item from the vending machine:\n\ta) Butterbeer: 58 knuts\n\tb) Quill: 10 knuts\n\tc) The Daily Prophet: 7 knuts\n\td) Book of Spells: 400 knuts\n")
if item.lower()!= "a" and item.lower()!="b" and item.lower()!="c" and item.lower()!="d":
    print("You have entered an invalid option. You will be given a Butterbeer for 58 knuts.")
    item="a"

# Ask the second question
share=input("Will you share this on Instagram? (y/n): ")
if share.lower()!="y" and share.lower()!="n":
    print("You have entered an invalid option. No coupon will be used.")
    share="n"

# Check conditions
if share=="y":
    coupon=coupon+5
    print("Thanks! You get 5 knuts off your purchase.")
if item=="a":
    price=price+58
    bought=bought+"a Butterbeer"
elif item=="b":
    price=price+10
    bought=bought+"a Quill"
elif item=="c":
    price=price+7
    bought=bought+"the Daily Prophet"
elif item=="d":
    price=price+400
    bought=bought+"a Book of Spells"

finalPrice=finalPrice-coupon+price
change=str(change+493-finalPrice)
sickle=int(change)//29
knuts=int(change)%29

# Print final statement
print("\nYou bought", bought, "for", price, "knuts (with coupon of", coupon, "knuts) and paid with one galleon.\nHere is your change (" + change, "knuts):\nSickles:", sickle, "\nKnuts:", knuts)