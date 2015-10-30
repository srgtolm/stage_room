__author__ = 'srgtolm'

import urllib
from BeautifulSoup import *

'''
url = raw_input('Enter - ')
http = 'http://'
url = ''.join([http,url])
print url

url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Iria.html'
print "Enter URL: ",url
cnt = 4
print "Enter count, ",cnt
pos = 3
print 'Enter position, ',pos
url_list = [url]
url_visited = [url]
url_total = []


while len(url_list) < cnt:
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    for tag in tags:
        newurl = str(tag.get('href', None))
        url_total.append(newurl)
        #print url_total
        #if newurl not in url_visited:

            #url_visited.append(newurl)
        url_list.append(newurl)
        #print url_list
            #print newurl

print url_list
#print url_total
#print url_visited
'''
#url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html'
url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Morton.html'
print "Enter URL: ",url
cnt = 4
print "Enter count, ",cnt
pos = 3
print 'Enter position, ',pos
i = 0

while i <= cnt:
        html = urllib.urlopen(url).read()
        soup = BeautifulSoup(html)
        tags = soup('a')
        if i == 4:
            print "Last URL: ", i ,url
        else:
            print "Retrieving: ", i ,url
        tag_list = []
        for tag in tags:
            z = str(tag.get('href', None))
            tag_list.append(z)
        url = tag_list[2]
        i += 1




#print tag_list[2]

