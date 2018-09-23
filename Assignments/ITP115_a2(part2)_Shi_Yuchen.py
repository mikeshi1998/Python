# Yuchen Shi
# ITP 115, Spring 2018
# Assignment 2
# Yuchensh@usc.edu

# Part 2: Choose Your Own Adventure

print("Welcome to choose your own adventure game.\n\nIt’s Friday night. You just finished 4 exams in this week, so you really want to have a rest. However, there are still a paper and a lab report due tomorrow noon.\nYour roommates ask you to go to a party together; while your girlfriend asks you to go out for a date together. Your parents just call you and they say you should focus on study.")
choice1=input("Do you:\na) Go to the party with your roommates\nb) Go for a date with your girlfriend\nc) Stay at home and do the homework\n")

# Deal with invalid options
while choice1.lower()!="a" and choice1.lower()!="b" and choice1.lower()!="c":
    choice1=input("You have entered an invalid option. Please try again. ")

# Choice a
if choice1.lower()=="a":
    join=input("\nYou go to the party and everyone is drinking. Do you want to join them?\na) Yes\nb) No\n")
    while join.lower()!= "a" and join.lower()!= "b" and join.lower()!="c":
        join=input("You have entered an invalid option. Please try again. ")
    if join.lower()=="a":
        print("\nYou are heavily drunk and sleep at the party house. Tomorrow when you wake up, you suddenly realize the homework has passed due already.\n\nTHE END")
    if join.lower()=="b":
        print("\nYou have fun chilling with your friends and after a few hours you go back home and finish your homework.\n\nTHE END")

# Choice b
if choice1.lower()=="b":
    pay=input("\nYou go to a Michelin 3-star restaurant with your girlfriend. You have a wonderful dinner and but it is also super expensive. When you are checking, do you:\na) Pay for everything by yourself\nb) Split the bill with your girlfriend\n")
    while pay.lower()!="a" and pay.lower()!="b":
        pay=input("You have entered an invalid option. Please try again. ")
    if pay.lower()=="a":
        print("\nYour girlfriend is very happy and you have a romantic night. She kiss you when you are going back home.\n\nTHE END")
    if pay.lower()=="b":
        print("\nYour girlfriend is astonished that you are so stingy, and she leaves with a disappointed face. At night, she texts you and says she is breaking up with you.\n\nTHE END")

# Choice c
if choice1.lower()=="c":
    homework=input("\nYou refuse both your roommates and your girlfriend. They are all very disappointed. You open your schoolbag and start to do the homework.\nDo you:\na) Write the paper first\nb) Write the lab report first\n")
    while homework.lower()!="a" and homework.lower()!="b":
        homework=input("You have entered an invalid option. Please try again. ")
    if homework.lower()=="a":
        print("\nYou spend a whole night on the paper and finish it on 10 am in the next day. When you are submitting it, you suddenly find that it is due next Monday…and you haven’t start your lab report yet.\n\nTHE END")
    if homework.lower()=="b":
        print("\nYou spend a whole night on the lab report and finish it on 1 am. After you submit the lab report and start look at the paper, you suddenly find that the paper is due next Monday! You are very happy and feel lucky that you choose to write the lab report first.\n\nTHE END")
