__author__ = 'sereg'

from random import randint

def sleepingcow_room():
    """Sleeping cow room"""
    print "Here is room with sleeping cow"
    print "You can go out"
    print "Or to try to go not woke up it"

    global status
    choice = raw_input("> ")

    while status:
        if choice == "go out" or choice == "out":
            start_room()
        elif choice == "wake up" or choice == "wake":
            print "Mooo-moo-mooo"
            status = False
            treasure_room()
        else:
            print choice
            print"I got no idea what that means"

def monster_room():
    print "Here is monster"
    print "Run out"
    print "Attack it"

    global status
    choice = raw_input("> ")


    if choice == "run":
        print ""
        print "Clever opinion, you are alive"
        status = False
        start_room()
    elif choice == "attack":
        print ""
        print "you have NO chance to win"
        dead("Monster kill you.")
    else:
        print choice
        print"I got no idea what that means"
        monster_room()


def demon_room():
    print "Here Demon room , it prepare for you some tricky questions"
    print "Do you try to answer?"
    print "No, go out"

    status = True

    while status:
        choice = raw_input("> ")
        if choice == "try":
            print "Favourite programming language is?"
            choice = raw_input("> ")
            if choice == "python":
                print "It is wright answer"
                treasure_room()
            else:
                print "Wrong."
                status = False
                start_room()
        elif choice == "out":
            status = False
            start_room()
        else:
            print"I got no idea what that means"


def angel_room():
    print "wow its an angel, it offer to play game"
    print "Lets play"
    print "Or not?"

    choice = raw_input("> ")
    rnd = randint(1,5)

    if choice == "yes":
        print "So, lets guess a number from 1 to 5"
        print rnd
        choice = raw_input("> ")
        if int(choice) == rnd:
            print "You win, and can go to treasure room"
            treasure_room()
        else:
            print "Yoo loose game, go out now"
            start_room()
    elif choice == "not":
        start_room()
    else:
        print"I got no idea what that means"
        angel_room()


def treasure_room():
    print "Now you are in treasure room"
    print "What do you want to get, please say just three"
    print "There are: gold, diamonds, pearls, sapphires and ruby on rails"



def start_room():
    print "You are in ancient dragon nest"
    print "In search glory and richness "
    print "There is 4 doors, which one you want to go?"

    global status, cnt
    choice = raw_input("> ")

    if choice == "1" or choice == "one" or choice == "first":
        sleepingcow_room()
    elif choice == "2" or choice == "two" or choice == "second":
        monster_room()
    elif choice == "3" or choice == "three" or choice == "third":
        demon_room()
    elif choice == "4" or choice == "four":
        angel_room()
    else:
        print cnt
        if cnt == 3:
            dead("You cannot get out start room")
        elif not status:
            print "No another way, you have to choose door"
            print ""
            cnt = cnt + 1
            start_room()
        else:
            status = False
            cnt = cnt + 1
            start_room()

def dead(why):
    print why
    print "haha, you Looose!"
    exit(0)

status = True
cnt = 1
start_room()
