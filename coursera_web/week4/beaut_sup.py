__author__ = 'srgtolm'

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
http = 'http://'
url = ''.join([http,url])
print url

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print type(tag)
    print tag.get('href', None)