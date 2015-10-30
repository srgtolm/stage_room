__author__ = 'srgtolm'

from stats import *
from random import randint


class Sklad(object):
    def enter(self):
        print "You are in Sklad."
        print "Here held some war games"
        rpg_battle_start()
        return 'zala'

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
        df = []
        for x in range(0, 3):
            creating = False
            while creating == False:
                val = raw_input('Please enter the %x item [head][body[legs][hands]]>'%(x+1))
                if (val in df) or (val not in hero):
                    print 'mistake'
                    creating = False
                else:
                    creating = True
                df.insert(x,val)
                hero[df[x]] = 'def'
        print hero
        return hero



'''        creating = False
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
'''

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

        while (some1 == some2) or (some1 == some3):
            some1 = randint(1,4)
            some2 = randint(1,4)
            some3 = randint(1,4)

            str_some1 = str(some1)
            str_some2 = str(some2)
            str_some3 = str(some3)

            vrag[str_some1] = 'def'
            vrag[str_some2] = 'def'
            vrag[str_some3] = 'def'

        print vrag

        '''
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
        'SHOW ENEMY'
        #print vrag
        '''
        return vrag


def win():
    print "You are winner"
    prize = randint(1,20)
    print "Earn some money - %d" % prize
    param(prize,0)
def loose():
    print "You were KILLED."
    penalty = randint(1,20)
    print "Your penalty is %d" % penalty
    param(-penalty,0)

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
            print "YOU are MISS"
            return False
    elif who == 'pc':
        print "PC miss"
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
        return loose()
    else:
        mortal_kombat()


body_enemy = 0
body_player = 0

def rpg_battle_start():
    global body_enemy, body_player
    #print "############"
    initiateE = Enemy()
    initiateP = Player()
    body_enemy = initiateE.opponent()
    body_player = initiateP.warrior()
    mortal_kombat()
    #print body_enemy
    return 'zala'

#rpg_battle_start()

