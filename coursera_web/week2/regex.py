__author__ = 'srgtolm'

import re

hand = open('regex_sum_186407.txt')
numlist = list()
for line in hand:
    print type(line)
    line = line.rstrip()
    stuff = re.findall('[0-9]+',line)
    print stuff, len(stuff)
    if len(stuff) < 1 : continue
    #print 'hi'
    for i in range(0,len(stuff)):
        num = float(stuff[i])
        numlist.append(num)
print 'Maximum:', numlist, max(numlist), sum(numlist)
