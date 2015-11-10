__author__ = 'srgtolm'

import json
import urllib

#serviceurl = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_42.json'
serviceurl ='http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_186413.json'

print 'Retrieving', serviceurl
url = urllib.urlopen(serviceurl)
data = url.read()
print 'Retrived, ',len(data), 'charaters'
js = json.loads(str(data))
zz = 0
cnt = 0
for i in js['comments']:
    cnt += 1
    zz += i['count']
print 'Count', cnt
print 'Sum:', zz


