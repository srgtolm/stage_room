__author__ = 'srgtolm'

from stats import *
from random import randint

class Peshera(object):
    def enter(self):
        print "You are travel to near by cave with gold and treasures"
        print "But it is no so easy to find some gold"
        print "Try to guess where are the gold mine"
        print "Guess a number from 1 to 9"
        print "You have 3 turns, if you are unlucky you waste 10 hit points"
        print "Money - %d, Life - %d" % (param()[0], param()[1])
        guess = raw_input("[keypad]> ")
        guesses = 0
        #code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        code = "%d" % (randint(1,9))
        while guess != code and guesses < 5:
            if guess == 'hack':
                print code
                guesses += 1
                guess = raw_input("[keypad]> ")
            else:
                print "BZZZZEDDD!"
                guesses += 1
                guess = raw_input("[keypad]> ")

        if guess == code:
            print "You are good luck"
            prize = randint(1,9)
            print "Earn some money - %d" % prize
            param(prize,0)
            print param()[0]
            return "zala"
        else:
            print "Such a looser"
            penalty = randint(1,9)
            print "Your penalty is %d" % penalty
            return "zala"


