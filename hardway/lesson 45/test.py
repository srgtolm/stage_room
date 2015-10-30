__author__ = 'srgtolm'

from random import randint

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
            print val,hide_list
            print "WINNER"
            print "Game OVER"
            exit()
        else:
            print "Wrong"
            creating = True
print "You challenge is over, try it next time"













'''
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

str_some1 = str(some1)
str_some2 = str(some2)

vrag[str_some1] = 'def'
vrag[str_some2] = 'def'


print str_some1,str_some2
print vrag
'''

''' Working code to select armor
df = []

hero = {
        'head':'null',
        'body':'null',
        'hands':'null',
        'legs':'null'
        }

for x in range(0, 3):
    creating = False
    while creating == False:
        val = raw_input('Please enter the %x item>'%(x+1))
        if (val in df) or (val not in hero):
            print ''
            creating = False
        else:
            creating = True
    df.insert(x,val)
    hero[df[x]] = 'def'

print df[0], df[1], df[2]
print hero
'''



