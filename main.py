import random


def displayMenu():
    print "Please select your life path:\n(T)rain\n(B)attle\n(W)ithdraw\n"

def getMenuChoice():
    choice = raw_input()
    valid = False
    while not valid:
        if choice == "T" or choice == "t" or choice == "B" or choice == "b" or choice == "W" or choice == "w":
            valid = True
        else:
            print "Incorrect life choice! \nYou have brought shame to your family. \nTry again..."
            choice = raw_input()

    return choice.capitalize()

def getAttackChoice():
    valid = False
    while not valid:
        choice = raw_input()
        if not choice.isdigit():
            print "This is not valid. Shame!\nTry again"
        else:
            choice = int(choice)
            if choice <= 0 or choice > 6:
                print "Incorrect life choice! \nYou have brought shame to your family. \nTry again..."
            else:
                valid = True
    return choice

def displayAttackChoice(choice, player):
    if choice == 1:
        print player + " chose: " + "(1) Punch of Fury\n"
    elif choice == 2:
        print player + " chose: " + "(2) Kick of Punishment\n"
    elif choice == 3:
        print player + " chose: " + "(3) Sword of Justice\n"
    elif choice == 4:
        print player + " chose: " + "(4) Shuriken of Vengeance\n"
    elif choice == 5:
        print player + " chose: " + "(5) Nunchucks of Anger\n"
    else: print player + " chose: " + "(6) Knife of Freedom\n"

def displayAttackMenu():
    print "(1) Punch of Fury \n(2) Kick of Punishment \n(3) Sword of Justice \n(4) Shuriken of Vengeance \n(5) Nunchucks of Anger \n(6) Knife of Freedom."

def battle(attackChoice):
    compAttack = random.randrange(1,7)
    displayAttackChoice(compAttack, "Super Inteligent AI")
    if compAttack == attackChoice:
        print "Tie"
    elif attackChoice == 1:
        if compAttack == 2 or compAttack == 3 or compAttack == 6:
            print "you lose\n"
        else:
            print "you won!\n"
    elif attackChoice == 2:
        if compAttack == 3 or compAttack == 4 or compAttack == 6:
            print "you lose\n"
        else:
            print "you won!\n"
    elif attackChoice == 3:
        if compAttack == 4 or compAttack == 5:
            print "you lose\n"
        else:
            print "you won!\n"
    elif attackChoice == 4:
        if compAttack == 1 or compAttack == 5:
            print "you lose"
        else:
            print "you won!\n"
    elif attackChoice == 5:
        if compAttack == 1 or compAttack == 2 or compAttack == 6:
            print "you lose\n"
        else:
            print "you won!\n"
    else:
        if compAttack == 3 or compAttack == 4:
            print "you lose\n"
        else:
            print "you won!\n"

print "\n\n Running imaginearing scripts...\n\n"

print "Welcome ninja warrior!"
name = raw_input("Submit your name to the death squad elite: ");

print "\nWelcome " + name + ".\n"

complete = False
while not complete:
    displayMenu()
    menuChoice = getMenuChoice()

    if menuChoice == "T":
        print "Welcome to Ultimate Ninja Battle Combat!!! \nYou will be fighting against the computer, and the winner gets bragging rights. \nFor each turn you will be asked to use one of the 6 attacks below:\n"
        displayAttackMenu()
        print "\nChoose wisely.\n"

    elif menuChoice == "B":
        displayAttackMenu()
        attackChoice = getAttackChoice()
        displayAttackChoice(attackChoice, "You")
        battle(attackChoice)
    elif menuChoice == "W":
        complete = True
