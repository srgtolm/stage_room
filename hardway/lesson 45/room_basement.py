__author__ = 'srgtolm'

from random import randint
from stats import *

class Basement(object):

    def enter(self):
        print "Collect 100 gold"
        print "and you can try to win a treasure"
        print "three from ten"
        print "1.Give 100 gold to participate[give]"
        print "2.Go back[back]"

        action = raw_input(">")
        decision = False
        while decision == False:
            if action == "1" or action == "give":
                if param(0,0)[0] >= 100:
                    param(-100,0)[0]
                    return self.treasure()
                else:
                    print "not enouth"
                    return 'zala'
            elif action == "2" or action == "back":
                return 'zala'
            else:
                print "Please type valid option"
                action = raw_input(">")

    def treasure(self):
        hide_list = []
        for i in range(0,3):
            creating = False
            while creating == False:
                hide_num = randint(1,11)
                if hide_num in hide_list:
                    print "mistake"
                    creating = False
                else:
                    creating = True
                hide_list.append(hide_num)
        print hide_list

        for i in range(0,3):
            creating = False
            while creating == False:
                val = raw_input('Guess %i:'%i)
                if int(val) in hide_list:
                    print "WINNER"
                    print "Game OVER"
                    exit()
                else:
                    print "Wrong"
                    creating = True
        print "You challenge is over, try it next time"
        return 'zala'

