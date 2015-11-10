__author__ = 'srgtolm'

import urllib
import xml.etree.ElementTree as ET

#serviceurl = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_42.xml'
serviceurl = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_186409.xml'

#while True:
#address = raw_input('Enter location: ')
#if len(address) < 1 : break

#url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
url = serviceurl
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
#print data
tree = ET.fromstring(data)
comm = tree.findall('comments/comment')
print 'Count: ', len(comm)
sumval = 0
for item in comm:
    #print item.find('name').text
    val = item.find('count').text
    sumval += int(val)

print "Sum:", sumval

