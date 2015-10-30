import urllib
from BeautifulSoup import *

url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Morton.html'
print "Enter URL: ",url
cnt = 7
print "Enter count, ",cnt
pos = 18
print 'Enter position, ',pos
i = 0

while i <= cnt:
        html = urllib.urlopen(url).read()
        soup = BeautifulSoup(html)
        tags = soup('a')
        if i == cnt:
            print "Last URL: ", i ,url
        else:
            print "Retrieving: ", i ,url
        tag_list = []
        for tag in tags:
            z = str(tag.get('href', None))
            tag_list.append(z)
        url = tag_list[17]
        i += 1
