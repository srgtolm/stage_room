__author__ = 'sereg'

from random import randint

class Player(object):

    def warrior(self):
        print "Welcome in battle"
        print "There are 4 types of targets to shoot"
        print "this is head, body, hands, legs"
        print "So please choose 2 for defence it"
        hero = {
                'head':'null',
                'body':'null',
                'hands':'null',
                'legs':'null'
        }

        creating = False
        p1 = False
        p2 = False

        while creating == False:
            def1 = raw_input('First one>')
            if def1 in hero:
                hero[def1] = 'def'
                p1 = True
            else:
                print "wrong"
                p1 = False
                p2 = False
            def2 = raw_input('Second one>')
            if def2 in hero:
                hero[def2] = 'def'
                p2 = True
            else:
                print "wrong"
                p1 = False
                p2 = False
#            print p1, p2
            creating = p1 and p2
        print hero
        return hero

class Enemy(object):
    def opponent(self):
        #print "Enemy is generating..."
        vrag ={
            '1':'null',
            '2':'null',
            '3':'null',
            '4':'null'
        }
        some1 = 1
        some2 = 1

        while some1 == some2:
            some1 = randint(1,4)
            some2 = randint(1,4)
            #print some1,some2

        #print str(some1)
        #print str(some2)
        if str(some1) == '1':
            vrag['1'] = 'def'
        elif str(some1) == '2':
            vrag['2'] = 'def'
        elif str(some1) == '3':
            vrag['3'] = 'def'
        elif str(some1) == '4':
            vrag['4'] = 'def'
        else:
            pass
        if str(some2) == '1':
            vrag['1'] = 'def'
        elif str(some2) == '2':
            vrag['2'] = 'def'
        elif str(some2) == '3':
            vrag['3'] = 'def'
        elif str(some2) == '4':
            vrag['4'] = 'def'
        else:
            pass
        print vrag
        return vrag


def win():
    print "You are winner"
def loose():
    print "You were KILLED."

def word_to_num(target):
    if target == "head":
        return '1'
    elif target == 'body':
        return '2'
    elif target == "hands":
        return '3'
    elif target == 'legs':
        return '4'
    else:
        print 'mistake in word_to_num'

def num_to_word(target):
    if target == "1":
        return 'head'
    elif target == '2':
        return 'body'
    elif target == "3":
        return 'hands'
    elif target == '4':
        return 'legs'
    else:
        print 'mistake in word_to_num'


def mortal_kombat():
    print "Player is shooting"
    print "head,body,hands,legs"

    shoot = raw_input("choose>")
    shoot = word_to_num(shoot)
    who = 'player'
    if compare(shoot,who):
        win()
    else:
       # print "HERE"
        enemy_strike()

def compare(choose,who):
    print 'choose:', choose
    print 'who is>', who
    choose = str(choose)
    #print start_game[choose]
    if who == 'player':
        if body_enemy[choose] != 'def':
            return True
        else:
            return False
    elif who == 'pc':
        print "BODY PLAYER:", body_player[choose]
        if body_player[choose] != 'def':
            return True
        else:
            return False
    else:
        pass

def enemy_strike():
    print "Now enemy time to shoot"
    shoot = randint(1,4)
    shoot = num_to_word(str(shoot))
    who = 'pc'
    if compare(shoot,who):
        print "PC kill you"
    else:
        mortal_kombat()


initiateE = Enemy()
initiateP = Player()
body_enemy = initiateE.opponent()
body_player =initiateP.warrior()
#print body_enemy

mortal_kombat()

