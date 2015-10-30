__author__ = 'srgtolm'

import urllib

fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')

print fhand
for line in fhand:
    print line.rstrip()

counts = 0
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
print counts