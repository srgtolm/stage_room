__author__ = 'srgtolm'

import urllib
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = raw_input('Enter Address>')
    if len(address) < 1 or address == 'exit' : break
    url = serviceurl + urllib.urlencode({'sendor':'false', 'address':address})
    print 'Retreiving', url
    open_url = urllib.urlopen(url)
    read_url = open_url.read()
    print "Retrieved", len(read_url), 'charaters'

    json_url = json.loads(read_url)
    first_list = []
    placeid = json_url['results'][0]["place_id"]
    print "Place id is ", placeid
