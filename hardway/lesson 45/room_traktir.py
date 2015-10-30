__author__ = 'srgtolm'

from random import randint
from stats import *

class Traktir(object):



    def enter(self):
        print "You are at bank"
        print "You can keep your money here"
        print "Money  will be increased according to the percentage"
        print "Money - %d, Life - %d" % (param(0,0)[0], param(0,0)[1])
        print "You can choose: "
        print "1. Take money from bank account"
        print "2. Put money into bank account"
        print "3. Status about your money at bank account"
        print "4. Exit"

        global perc
        perc = randint(1,9)

        action = raw_input(">")
        decision = False
        while decision == False:
            if action == "1" or action == "take":
                return self.take_money()
            elif action == "2" or action == "put":
                return self.put_money()
            elif action == "3" or action == "stat":
                print "BANK", status(self)
                return 'traktir'
            elif action == "4" or action == "exit":
                return 'zala'
            else:
                print "Please type valid option"
                action = raw_input(">")

        return 'zala'

    def take_money(self):
        print "Take money:", param(0,0)[0]
        action = raw_input("Enter amount:")
        x = -int(action)
        self.bank(x)
        y = int(action)
        param(y,0)[0]
        return 'traktir'


    def put_money(self):
        print "Money:", param(0,0)[0]
        action = raw_input("Enter amount:")
        x = int(action)
        self.bank(x)
        return 'traktir'


    def status(self):
        return 'zala'

    def bank(self,x):
        global bank
        print x
        bank +=x
        print bank
        return bank

def increase(self):
    global bank
    if bank == 0:
        pass
    else:
        print perc
        bank = bank * perc/100 + bank
    print "After bank", bank
    return bank

def status(self):
    global bank
    return bank

