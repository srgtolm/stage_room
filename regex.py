__author__ = 'srgtolm'

import re
'''
hand = open('second.txt')
for line in hand:
    line = line.rstrip()
    if re.search("Ramm", line):
        print line
'''
x = "my e-mail is s@serjoker.ru now"
#'''1
y = re.findall('is \S+@\S+', x)
print y
#'''
'''2
locate_start = x.find('@')
print locate_start
locate_stop = x.find(" ",locate_start)
print locate_stop
host = x[locate_start+1:locate_stop]
print host
'''
'''3
words = x.split()
print words
email = words[3]
print email
pieces = email.split('@')
print pieces[1]
'''
'''
lin = "From stephen.marwuard@uct.ac.za Sat Jun 4 09-99-09 2008"
y = re.findall('@([^ ]*)',x)
print y
'''
x = 'From From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+@.+?a', x)
print y
y = re.findall('\S+@.+a', x)
print y
y = re.findall("\S+@\S*",x)
print y