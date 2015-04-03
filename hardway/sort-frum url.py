__author__ = 'sereg'

#!/usr/bin/python
import string
from urllib3 import urlopen

u = urlopen("http://python.org")
words = {}

for line in u.readlines():
    line = string.strip(line, " \n")
    for word in line.split(" "):
        try:
            words[word] += 1
        except KeyError:
            words[word] = 1




pairs = words.items()

pairs.sort(lambda a, b: b[1]-a[1])

for p in pairs[:10]:
    print p[0], p[1]
