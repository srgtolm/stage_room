__author__ = 'sereg'

from urllib2 import urlopen

u = urlopen("http://vz.ru")
words = {}

for line in u:
    line = line.strip(" \n")
    for word in line.split(" "):
        try:
            words[word] += 1
        except KeyError:
            words[word] = 1

pairs = words.items()

pairs.sort(key=lambda x: x[1], reverse=True)

#print pairs,
for p in pairs:
    print p[0], p[1]