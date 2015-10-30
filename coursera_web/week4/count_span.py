import urllib
import re
from BeautifulSoup import *

b = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_186412.html'

html = urllib.urlopen(b).read()
soup = BeautifulSoup(html)

#print soup
tags = soup('span')
z = 0
for tag in tags:
    a = tag.contents[0]
    z += int(a)
print z