__author__ = 'srgtolm'

import os
from stats import *
from room_traktir import increase
from room_traktir import status

#print param(0,0)

class Zala(object):
    def enter(self):
        increase(self)
        print "You are in central Zala"
        print "Peacefuly place to take a rest"
        print "Make a decision what to do next"
        print "Money - %d, Life - %d, Bank - %d" % (param(0,0)[0], param(0,0)[1], status(self))
        print "You can choose: "
        print "1. Move to CAVE"
        print "2. Move to STORAGE"
        print "3. Move to Basement"
        print "4. Move to PUB"
        action = raw_input(">")
        decision = False

        while decision == False:
            if action == "1" or action == "cave" or action == "CAVE":
                return "peshera"
                print "1"
                decision = True
            elif action == "2" or action == "storage" or action == "STORAGE":
                return "sklad"
                print "2"
                decision = True
            elif action == "3" or action == "basement" or action == "BASEMENT":
                return "basement"
                print "3"
                decision = True
            elif action == "4" or action == "pub" or action == "PUB":
                return "traktir"
                print "4"
                decision = True
            else:
                print "Please type valid option"
                action = raw_input(">")

#z = Zala()
#print z.enter()


