__author__ = 'srgtolm'

money = 0
life = 100
bank = 0
perc = 0

def param(m,l):
    global money,life
    money += m
    life += l
    return money,life


