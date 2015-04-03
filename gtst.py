__author__ = 'sereg'

print "Start"

from grab import Grab
g = Grab()
g.go('http://bbc.com')
print g.doc.select('//title').text()
print g.request_headers
#print g.response.cookies['sid']
#print g.response.cookies
#print g.response.headers['Content-Type']
#print g.response.code


print "End"